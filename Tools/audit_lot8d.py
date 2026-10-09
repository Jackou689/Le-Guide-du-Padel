from pathlib import Path
from bs4 import BeautifulSoup
from urllib.parse import unquote, urlparse
from lxml import etree
import re, sys
pages=sorted(Path('.').glob('*.html'))
errors=[]; missing=[]; broken=[]; canon=[]; amazon_bad=[]; inline_style=0; beacons=0
for p in pages:
 text=p.read_text(); s=BeautifulSoup(text,'html.parser')
 inline_style += len(s.select('[style]'))
 beacons += sum(1 for x in s.find_all('script') if 'cloudflareinsights.com/beacon.min.js' in (x.get('src') or ''))
 for c in s.find_all('link',rel='canonical'): canon.append(c.get('href'))
 for tag,attr in [('script','src'),('img','src'),('source','srcset')]:
  for el in s.find_all(tag):
   raw=el.get(attr)
   if not raw: continue
   vals=[x.strip().split()[0] for x in raw.split(',')] if attr=='srcset' else [raw]
   for v in vals:
    v=v.split('?')[0]
    if v and not v.startswith(('http:','https:','data:','//')) and not Path(unquote(v)).exists(): missing.append(f'{p}:{v}')
 for a in s.find_all('a',href=True):
  h=a['href']
  if 'amazon.fr' in h and not {'nofollow','sponsored'}.issubset(set(a.get('rel') or [])): amazon_bad.append(f'{p}:{h}')
  if h.startswith(('#','mailto:','tel:','http:','https:','javascript:','/')): continue
  target=h.split('#')[0].split('?')[0]
  if target and not Path(unquote(target)).exists(): broken.append(f'{p}:{h}')
 for script in s.find_all('script'):
  if not script.get('src') and script.get('type')!='application/ld+json' and script.get_text(strip=True): errors.append(f'{p}: script fonctionnel inline')
if len(pages)!=14: errors.append(f'{len(pages)} pages au lieu de 14 avec 404')
if inline_style: errors.append(f'{inline_style} styles inline')
if beacons!=14: errors.append(f'{beacons} beacons Cloudflare au lieu de 14')
if len(canon)!=13 or len(set(canon))!=13: errors.append(f'canoniques: {len(canon)} total, {len(set(canon))} uniques')
s404=BeautifulSoup(Path('404.html').read_text(),'html.parser')
if not s404.find('meta',attrs={'name':'robots','content':'noindex, follow'}): errors.append('404 sans noindex, follow')
if s404.find('link',rel='canonical'): errors.append('404 avec canonical')
for required in ['_headers','_redirects','robots.txt','sitemap.xml','wrangler.jsonc']:
 if not Path(required).exists(): errors.append(f'{required} absent')
try: etree.parse('sitemap.xml')
except Exception as e: errors.append(f'sitemap invalide: {e}')
js=Path('script.js').read_text()
if 'category-btn' not in js: errors.append('filtre categories absent du JS partage')
if re.search(r'adsbygoogle|googlesyndication|doubleclick', ' '.join((x.get('src') or '') for p in pages for x in BeautifulSoup(p.read_text(),'html.parser').find_all(['script','iframe'])),re.I): errors.append('ressource publicitaire active')
errors += missing+broken+amazon_bad
print(f'{len(pages)} pages HTML analysees')
print(f'{len(canon)} canoniques uniques attendues: {len(set(canon))}')
print(f'{beacons} beacons Cloudflare')
print(f'{inline_style} style inline')
print(f'{len(missing)} actif local manquant')
print(f'{len(broken)} lien interne casse')
print(f'{len(amazon_bad)} lien Amazon non conforme')
print('AdSense inactif')
if errors:
 print('\n'.join(errors)); sys.exit(1)
print('404 valide')
print('Sitemap valide')
print('Audit 8D reussi')
