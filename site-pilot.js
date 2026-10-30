(()=>{
'use strict';
const d=document,b=d.body,root=d.documentElement;
const qs=(s,c=d)=>c.querySelector(s),qsa=(s,c=d)=>[...c.querySelectorAll(s)];
let focusReturn=null;
function setTheme(value,persist=true){
 const dark=value==='dark';b.classList.toggle('is-dark',dark);root.style.colorScheme=dark?'dark':'light';
 qsa('[data-theme]').forEach(x=>{const active=x.dataset.theme===value;x.classList.toggle('is-active',active);x.setAttribute('aria-pressed',String(active))});
 const logo=qs('[data-brand-main]');if(logo)logo.src=dark?'assets/brand/logo-main-sombre.webp':'assets/brand/logo-main-clair.webp';
 const mobile=qs('[data-brand-mobile]');if(mobile)mobile.src=dark?'assets/brand/logo-mobile-lgp-sombre.webp':'assets/brand/logo-mobile-lgp-clair.webp';
 const signature=qs('[data-signature]');if(signature)signature.src=dark?'assets/brand/signature-editoriale-sombre.webp':'assets/brand/signature-editoriale-clair.webp';
 if(persist)try{localStorage.setItem('theme',value)}catch(e){}
}
let saved=null;try{saved=localStorage.getItem('theme')}catch(e){}
setTheme(saved||((matchMedia('(prefers-color-scheme:dark)').matches)?'dark':'light'),false);
qsa('[data-theme]').forEach(x=>x.addEventListener('click',()=>setTheme(x.dataset.theme)));
const header=qs('.site-header');let prevY=scrollY,travel=0,ticking=false;
function updateHeader(){const y=Math.max(scrollY,0),delta=y-prevY;if((delta>0&&travel<0)||(delta<0&&travel>0))travel=0;travel+=delta;header?.classList.toggle('is-compact',y>16);if(y<90){header?.classList.remove('is-hidden');travel=0}else if(travel>22){header?.classList.add('is-hidden');travel=0}else if(travel<-12){header?.classList.remove('is-hidden');travel=0}prevY=y;ticking=false}
addEventListener('scroll',()=>{if(!ticking){requestAnimationFrame(updateHeader);ticking=true}},{passive:true});
const drawer=qs('#mobile-drawer'),scrim=qs('#drawer-scrim');
function openDrawer(){focusReturn=d.activeElement;drawer.hidden=false;scrim.hidden=false;requestAnimationFrame(()=>{drawer.classList.add('is-open');scrim.classList.add('is-open')});b.classList.add('no-scroll');qs('[data-drawer-close]')?.focus()}
function closeDrawer(){drawer.classList.remove('is-open');scrim.classList.remove('is-open');setTimeout(()=>{drawer.hidden=true;scrim.hidden=true},200);b.classList.remove('no-scroll');focusReturn?.focus()}
qs('[data-drawer-open]')?.addEventListener('click',openDrawer);qsa('[data-drawer-close]').forEach(x=>x.addEventListener('click',closeDrawer));
const search=qs('#search-dialog'),searchInput=qs('#site-search'),results=qs('#search-results');
const guides=[
['Matériel','Choisir sa première raquette','Formes, poids et mousse pour trouver une raquette adaptée.','raquette-debutant'],['Débuter','Les règles du padel','Terrain, service, score et vitres expliqués clairement.','regles-padel'],['Matériel','Choisir ses chaussures','Stabilité, adhérence et confort pour jouer en sécurité.','chaussures-padel'],['Technique','Les coups techniques essentiels','Bandeja, vibora, lob et chiquita.','techniques-padel'],['Tactique','Dominer le filet en double','Placement, coordination et décisions à deux.','tactique-filet'],['Matériel','Bien choisir ses balles','Pression, durée de vie et différences utiles.','balles-padel'],['Santé','Échauffement en 10 minutes','Une routine progressive avant le match.','echauffement-padel'],['Santé','Préserver son coude','Choisir une raquette plus confortable.','raquette-tendinite']];
const norm=s=>s.normalize('NFD').replace(/[\u0300-\u036f]/g,'').toLowerCase();
function renderSearch(q=''){const n=norm(q.trim()),list=n?guides.filter(x=>norm(x.join(' ')).includes(n)):guides;results.innerHTML=list.length?list.map(x=>`<a href="${x[3]}"><span>${x[0]}</span><strong>${x[1]}</strong><small>${x[2]}</small></a>`).join(''):'<p class="empty-search">Aucun guide ne correspond à cette recherche.</p>'}
function openSearch(){focusReturn=d.activeElement;search.hidden=false;b.classList.add('no-scroll');renderSearch();setTimeout(()=>searchInput.focus(),0)}function closeSearch(){search.hidden=true;b.classList.remove('no-scroll');focusReturn?.focus()}
qsa('[data-search-open]').forEach(x=>x.addEventListener('click',openSearch));qsa('[data-search-close]').forEach(x=>x.addEventListener('click',closeSearch));searchInput?.addEventListener('input',e=>renderSearch(e.target.value));
d.addEventListener('keydown',e=>{if(e.key==='Escape'){if(!search.hidden)closeSearch();else if(!drawer.hidden)closeDrawer()}});
const tocLinks=qsa('.toc a'),sections=tocLinks.map(a=>qs(a.getAttribute('href'))).filter(Boolean);if('IntersectionObserver'in window){const io=new IntersectionObserver(entries=>{entries.forEach(e=>{if(e.isIntersecting){tocLinks.forEach(a=>a.classList.toggle('is-current',a.getAttribute('href')==='#'+e.target.id))}})},{rootMargin:'-20% 0px -68%'});sections.forEach(s=>io.observe(s))}
qsa('a[href^="#"]').forEach(a=>a.addEventListener('click',e=>{const t=qs(a.getAttribute('href'));if(t){e.preventDefault();t.scrollIntoView({behavior:matchMedia('(prefers-reduced-motion:reduce)').matches?'auto':'smooth',block:'start'})}}));
})();
