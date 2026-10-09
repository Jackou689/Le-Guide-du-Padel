from pathlib import Path
from bs4 import BeautifulSoup
from urllib.parse import unquote
from lxml import etree
import json,re,sys
root=Path('.')
pages=sorted(root.glob('*.html'))
errors=[]; canon=[]; missing=[]; broken=[]; amazon_bad=[]
style_tags=style_attrs=func_inline=beacons=0
for p in pages:
    s=BeautifulSoup(p.read_text(),'html.parser')
    style_tags += len([x for x in s.find_all('style') if x.get_text(strip=True)])
    style_attrs += len(s.select('[style]'))
    beacons += sum('cloudflareinsights.com/beacon.min.js' in (x.get('src') or '') for x in s.find_all('script'))
    for x in s.find_all('script'):
        if not x.get('src') and x.get('type')!='application/ld+json' and x.get_text(strip=True): func_inline += 1
    for c in s.find_all('link',rel='canonical'): canon.append(c.get('href'))
    for tag in s.find_all(src=True):
        v=tag['src'].split('?')[0]
        if v and not v.startswith(('http:','https:','data:','//')) and not (root/unquote(v)).exists(): missing.append(f'{p}:{v}')
    for a in s.find_all('a',href=True):
        h=a['href']; target=h.split('#')[0].split('?')[0]
        if 'amazon.fr' in h and not {'nofollow','sponsored'}.issubset(set(a.get('rel') or [])): amazon_bad.append(f'{p}:{h}')
        if target and not h.startswith(('#','mailto:','tel:','http:','https:','javascript:','/')):
            f=(target+'.html') if not Path(target).suffix else target
            if not (root/unquote(f)).exists(): broken.append(f'{p}:{h}')
if len(pages)!=14: errors.append(f'{len(pages)} pages, 14 attendues')
if style_tags or style_attrs: errors.append(f'{style_tags} balises style, {style_attrs} attributs style')
if func_inline: errors.append(f'{func_inline} script(s) fonctionnel(s) inline')
if beacons!=14: errors.append(f'{beacons} beacons Cloudflare, 14 attendus')
if len(canon)!=13 or len(set(canon))!=13: errors.append(f'canoniques {len(canon)}/{len(set(canon))}')
if any((u or '').endswith('.html') for u in canon): errors.append('canonique .html restante')
try: etree.parse('sitemap.xml')
except Exception as e: errors.append(f'sitemap invalide: {e}')
if '.html</loc>' in Path('sitemap.xml').read_text(): errors.append('URL .html dans sitemap')
headers=Path('_headers').read_text()
if "style-src 'self';" not in headers or "style-src 'self' 'unsafe-inline'" in headers: errors.append('CSP style-src non stricte')
if "script-src 'self' 'unsafe-inline' https://static.cloudflareinsights.com" not in headers: errors.append('CSP script incompatible avec JSON-LD/beacon')
wr=json.loads(Path('wrangler.jsonc').read_text())
if wr.get('assets',{}).get('html_handling')!='auto-trailing-slash': errors.append('html_handling absent')
if wr.get('assets',{}).get('not_found_handling')!='404-page': errors.append('404 handling absent')
errors += missing+broken+amazon_bad
print(f'Pages: {len(pages)}; styles locaux: {style_tags}; attributs style: {style_attrs}; scripts fonctionnels inline: {func_inline}')
print(f'Canoniques: {len(canon)} uniques: {len(set(canon))}; beacons: {beacons}')
print(f'Actifs manquants: {len(missing)}; liens internes cassés: {len(broken)}; liens Amazon non conformes: {len(amazon_bad)}')
if errors:
    print('\n'.join(errors)); sys.exit(1)
print('AUDIT 8E REUSSI')
