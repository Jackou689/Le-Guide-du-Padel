from pathlib import Path
from bs4 import BeautifulSoup
from urllib.parse import urlparse, unquote
import re, sys
root=Path('.')
pages=sorted(root.glob('*.html'))
errors=[]
beacons=0
inline_styles=0
adsense=0
doubleclick=0
missing=[]
amazon_bad=[]
for p in pages:
    text=p.read_text()
    s=BeautifulSoup(text,'html.parser')
    b=sum(1 for x in s.find_all('script') if 'cloudflareinsights.com/beacon.min.js' in (x.get('src') or ''))
    beacons+=b
    if b!=1: errors.append(f'{p}: {b} beacon(s) Cloudflare')
    inline_styles += len(s.select('[style]'))
    active_urls=' '.join((x.get('src') or '') for x in s.find_all(['script','iframe']))
    adsense += len(re.findall(r'adsbygoogle|googlesyndication',active_urls,re.I))
    doubleclick += len(re.findall(r'doubleclick',active_urls,re.I))
    for tag in s.find_all(src=True):
        src=tag.get('src','').split('?')[0]
        if src and not src.startswith(('http://','https://','data:','//')) and not (root/unquote(src)).exists(): missing.append(f'{p}:{src}')
    for tag in s.find_all(href=True):
        href=tag.get('href','').split('#')[0].split('?')[0]
        if href and not href.startswith(('http://','https://','mailto:','tel:','javascript:','/')) and Path(href).suffix and not (root/unquote(href)).exists(): missing.append(f'{p}:{href}')
    for a in s.find_all('a',href=re.compile(r'amazon\.fr')):
        rel=set(a.get('rel') or [])
        if not {'nofollow','sponsored'}.issubset(rel): amazon_bad.append(f'{p}:{a.get("href")}')
print(f'{len(pages)} pages analysees')
print(f'{beacons} beacons Cloudflare uniques')
print(f'{adsense} script AdSense actif')
print(f'{doubleclick} ressource DoubleClick active')
print(f'{inline_styles} style inline')
print(f'{len(missing)} actif local manquant')
print(f'{len(amazon_bad)} lien Amazon sans rel nofollow sponsored')
if len(pages)!=13 or beacons!=13 or adsense or doubleclick or inline_styles or missing or amazon_bad:
    print('\n'.join(errors+missing+amazon_bad)); sys.exit(1)
