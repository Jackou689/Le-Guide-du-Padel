document.addEventListener('DOMContentLoaded', () => {
    const themeToggleBtn = document.getElementById('theme-toggle');
    if (!themeToggleBtn) return;

    const setThemeButtonState = (isDark) => {
        const nextAction = isDark ? 'Activer le mode clair' : 'Activer le mode sombre';
        themeToggleBtn.setAttribute('aria-label', nextAction);
        themeToggleBtn.setAttribute('title', nextAction);
        themeToggleBtn.setAttribute('aria-pressed', String(isDark));
        themeToggleBtn.innerHTML = `<span aria-hidden="true">${isDark ? '☀️' : '🌙'}</span>`;
    };

    let savedTheme = null;
    try {
        savedTheme = localStorage.getItem('theme');
    } catch (error) {
        console.warn('La préférence de thème ne peut pas être lue.', error);
    }

    const isInitiallyDark = savedTheme === 'dark';
    document.body.classList.toggle('dark-mode', isInitiallyDark);
    setThemeButtonState(isInitiallyDark);

    themeToggleBtn.addEventListener('click', () => {
        const isDark = document.body.classList.toggle('dark-mode');
        setThemeButtonState(isDark);
        try {
            localStorage.setItem('theme', isDark ? 'dark' : 'light');
        } catch (error) {
            console.warn('La préférence de thème ne peut pas être enregistrée.', error);
        }
    });
});

document.addEventListener('DOMContentLoaded',()=>{const o=document.getElementById('mobile-menu-toggle'),c=document.getElementById('mobile-menu-close'),m=document.getElementById('mobile-menu'),v=document.getElementById('mobile-menu-overlay');if(!o||!c||!m||!v)return;let last=null;const close=()=>{m.classList.remove('is-open');v.classList.remove('is-open');m.setAttribute('aria-hidden','true');m.setAttribute('inert','');o.setAttribute('aria-expanded','false');o.setAttribute('aria-label','Ouvrir le menu');document.documentElement.classList.remove('mobile-menu-open');document.body.classList.remove('mobile-menu-open');setTimeout(()=>{v.hidden=true;if(last)last.focus()},200)},open=()=>{last=document.activeElement;v.hidden=false;m.classList.add('is-open');v.classList.add('is-open');m.setAttribute('aria-hidden','false');m.removeAttribute('inert');o.setAttribute('aria-expanded','true');o.setAttribute('aria-label','Fermer le menu');document.documentElement.classList.add('mobile-menu-open');document.body.classList.add('mobile-menu-open');requestAnimationFrame(()=>c.focus())};o.addEventListener('click',()=>m.classList.contains('is-open')?close():open());c.addEventListener('click',close);v.addEventListener('click',close);m.querySelectorAll('a').forEach(a=>a.addEventListener('click',close));document.addEventListener('keydown',e=>{if(!m.classList.contains('is-open'))return;if(e.key==='Escape'){e.preventDefault();close()}if(e.key==='Tab'){const q=[...m.querySelectorAll('a[href],button:not([disabled])')],f=q[0],l=q[q.length-1];if(e.shiftKey&&document.activeElement===f){e.preventDefault();l.focus()}else if(!e.shiftKey&&document.activeElement===l){e.preventDefault();f.focus()}}});window.addEventListener('resize',()=>{if(innerWidth>=768&&m.classList.contains('is-open'))close()})});

// Affiche les emplacements publicitaires de test uniquement en preview ou en local.
document.addEventListener('DOMContentLoaded', () => {
    const hostname = window.location.hostname;
    const isPreview = hostname === 'localhost' || hostname === '127.0.0.1' || hostname.endsWith('.workers.dev');
    document.body.classList.toggle('preview-mode', isPreview);
});


// Lot 8D : filtrage des categories de la page d accueil.
document.addEventListener('DOMContentLoaded', function() {
            const buttons = document.querySelectorAll('.category-btn');
            const cards = document.querySelectorAll('.article-card');

            buttons.forEach(button => {
                button.addEventListener('click', function() {
                    // Gestion de la classe active
                    buttons.forEach(btn => {
                        btn.classList.remove('active');
                        btn.setAttribute('aria-pressed', 'false');
                    });
                    this.classList.add('active');
                    this.setAttribute('aria-pressed', 'true');

                    const filter = this.getAttribute('data-filter');

                    cards.forEach(card => {
                        const category = card.getAttribute('data-category');
                        if (filter === 'all' || category === filter) {
                            card.classList.remove('is-filtered-out');
                        } else {
                            card.classList.add('is-filtered-out');
                        }
                    });
                });
            });
        });


// 10A.16 revisee : header fixe, compatible tactile et mobile.
document.addEventListener('DOMContentLoaded', function () {
  const header = document.querySelector('.header');
  if (!header) return;
  let lastY = Math.max(window.pageYOffset || document.documentElement.scrollTop || 0, 0);
  let accumulated = 0;
  let ticking = false;
  function readY() { return Math.max(window.pageYOffset || document.documentElement.scrollTop || document.body.scrollTop || 0, 0); }
  function update() {
    const y = readY();
    const delta = y - lastY;
    if ((delta > 0 && accumulated < 0) || (delta < 0 && accumulated > 0)) accumulated = 0;
    accumulated += delta;
    header.classList.toggle('header-scrolled', y > 12);
    if (y <= 90) { header.classList.remove('header-hidden'); accumulated = 0; }
    else if (accumulated > 18) { header.classList.add('header-hidden'); accumulated = 0; }
    else if (accumulated < -10) { header.classList.remove('header-hidden'); accumulated = 0; }
    lastY = y; ticking = false;
  }
  function requestUpdate() { if (!ticking) { ticking = true; requestAnimationFrame(update); } }
  window.addEventListener('scroll', requestUpdate, {passive:true});
  window.addEventListener('touchmove', requestUpdate, {passive:true});
  window.addEventListener('pageshow', function(){ header.classList.remove('header-hidden'); lastY=readY(); });
});
