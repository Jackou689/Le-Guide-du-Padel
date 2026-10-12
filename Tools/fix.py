from bs4 import BeautifulSoup
from pathlib import Path
# warmup
p=Path('echauffement-padel.html');s=BeautifulSoup(p.read_text(encoding='utf-8'),'html.parser');m=s.select_one('main.article-content')
for x in m.select('.step-visual'):x.decompose()
steps=[h for h in m.find_all('h3') if h.get_text(' ',strip=True).startswith('Étape ')]
alts=['Marche, petit trot et pas latéraux progressifs','Mobilité contrôlée des chevilles, hanches, genoux et épaules','Activation des appuis et freinage progressif','Gestes souples avec raquette, volées et services progressifs']
caps=['Faites monter le rythme sans chercher la vitesse.','Mobilisez les articulations sans forcer en fin d’amplitude.','Réveillez les appuis et les changements de direction.','Retrouvez progressivement les gestes de raquette.']
for i,h in enumerate(steps,1):h.insert_after(BeautifulSoup(f'<figure class="step-visual"><img src="images/echauffement-etape-{i}.webp" alt="{alts[i-1]}" width="680" height="430" loading="lazy" decoding="async"><figcaption><span class="visual-label">Étape en image</span><strong>{caps[i-1]}</strong></figcaption></figure>','html.parser'))
p.write_text(str(s),encoding='utf-8')
# techniques
p=Path('techniques-padel.html');s=BeautifulSoup(p.read_text(encoding='utf-8'),'html.parser');m=s.select_one('main.article-content')
for x in m.select('.technique-mini-visual,.technique-learning-visual'):x.decompose()
intro=m.select_one('.human-intro');intro.insert_after(BeautifulSoup('<figure class="inline-learning-visual technique-learning-visual"><img src="images/schema-trajectoires-techniques.webp" alt="Vue aérienne d’une piste de padel avec plusieurs trajectoires" width="1050" height="700" loading="lazy" decoding="async"><figcaption><strong>Vue d’ensemble :</strong> hauteur, profondeur, angles et vitres donnent une intention différente à chaque coup.</figcaption></figure>','html.parser'))
sl=['position','fond-court','lob','volees','bandeja','vibora','smash','chiquita','vitre-fond','double-vitre','bajada','transition-filet'];lb=['Position d’attente','Coup droit et revers','Lob défensif','Volées au filet','Bandeja de contrôle','Víbora avec effet','Choix du smash','Chiquita basse','Rebond sur vitre du fond','Lecture de la double vitre','Bajada après la vitre','Montée coordonnée au filet']
al=['Position d’attente avec raquette devant le corps','Coups compacts depuis le fond de court','Lob haut pour repousser les adversaires','Volées compactes près du filet','Bandeja contrôlée vers le fond','Víbora avec trajectoire latérale','Zones possibles pour choisir le smash','Chiquita basse dans les pieds','Attente du rebond sur la vitre du fond','Trajectoire utilisant deux vitres','Bajada après un rebond haut sur la vitre','Deux partenaires avançant ensemble']
heads=[h for h in m.find_all('h2') if h.get_text(' ',strip=True).split('.')[0].isdigit() and int(h.get_text(' ',strip=True).split('.')[0])<=12]
for i,h in enumerate(heads):
 stop=heads[i+1] if i+1<len(heads) else next((x for x in h.find_all_next('h2') if x not in heads),None);nodes=[];cur=h
 while cur and cur is not stop:nxt=cur.find_next_sibling();nodes.append(cur);cur=nxt
 sec=s.new_tag('section');sec['class']=['technique-section',f'technique-section-{i+1}'];h.insert_before(sec)
 for n in nodes:sec.append(n.extract())
 sec.select_one('h2').insert_after(BeautifulSoup(f'<figure class="technique-specific-visual"><img src="images/technique-{sl[i]}.webp" alt="{al[i]}" width="760" height="460" loading="lazy" decoding="async"><figcaption><span class="visual-label">Le geste en image</span><strong>{lb[i]}</strong></figcaption></figure>','html.parser'))
p.write_text(str(s),encoding='utf-8')
# balls
p=Path('balles-padel.html');s=BeautifulSoup(p.read_text(encoding='utf-8'),'html.parser');m=s.select_one('main.article-content')
heads=[h for h in m.find_all('h2') if h.get_text(' ',strip=True).split('.')[0].isdigit()]
for i,h in enumerate(heads):
 stop=heads[i+1] if i+1<len(heads) else next((x for x in h.find_all_next('h2') if x not in heads),None);nodes=[];cur=h
 while cur and cur is not stop:nxt=cur.find_next_sibling();nodes.append(cur);cur=nxt
 sec=s.new_tag('section');sec['class']=['ball-content-card',f'ball-card-{i%4+1}'];h.insert_before(sec)
 for n in nodes:sec.append(n.extract())
 b=s.new_tag('span');b['class']=['section-kicker'];b.string=['Comprendre','Choisir','Observer','Conserver'][i%4];sec.select_one('h2').insert_before(b)
for par in m.find_all('p'):
 if par.find('strong') and not par.find_parent('figure') and not par.find_parent(class_='human-intro'):par['class']=(par.get('class') or [])+['practical-takeaway']
p.write_text(str(s),encoding='utf-8')
for p in Path('.').glob('*.html'):
 t=p.read_text(encoding='utf-8').replace('style.css?v=10A2','style.css?v=10A4').replace('script.js?v=10A2','script.js?v=10A4');p.write_text(t,encoding='utf-8')
