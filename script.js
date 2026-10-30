/* Le Guide du Padel — script 2026 : thème, menu mobile, filtre d'accueil, retour en haut. Sans dépendance. */
(function () {
  var d = document, root = d.documentElement;
  function ready(f) { d.readyState !== 'loading' ? f() : d.addEventListener('DOMContentLoaded', f); }
  ready(function () {
    /* Thème : slider (role=switch) */
    var sw = d.getElementById('theme-toggle');
    function apply(dark) {
      root.setAttribute('data-theme', dark ? 'dark' : 'light');
      d.body.classList.toggle('dark-mode', dark);
      if (sw) sw.setAttribute('aria-checked', String(dark));
    }
    apply(root.getAttribute('data-theme') === 'dark');
    if (sw) sw.addEventListener('click', function () {
      var dark = root.getAttribute('data-theme') !== 'dark';
      apply(dark);
      try { localStorage.setItem('theme', dark ? 'dark' : 'light'); } catch (e) {}
    });

    /* Menu mobile accessible */
    var b = d.getElementById('lgp-burger'), m = d.getElementById('lgp-menu'), o = d.getElementById('lgp-overlay'), c = d.getElementById('lgp-close');
    if (b && m && o && c) {
      var last = null;
      var close = function () {
        m.classList.remove('is-open'); o.hidden = true;
        m.setAttribute('aria-hidden', 'true'); m.setAttribute('inert', '');
        b.setAttribute('aria-expanded', 'false'); b.setAttribute('aria-label', 'Ouvrir le menu');
        root.classList.remove('lgp-lock');
        if (last) last.focus();
      };
      var open = function () {
        last = d.activeElement; o.hidden = false; m.classList.add('is-open');
        m.setAttribute('aria-hidden', 'false'); m.removeAttribute('inert');
        b.setAttribute('aria-expanded', 'true'); b.setAttribute('aria-label', 'Fermer le menu');
        root.classList.add('lgp-lock'); c.focus();
      };
      b.addEventListener('click', function () { m.classList.contains('is-open') ? close() : open(); });
      c.addEventListener('click', close); o.addEventListener('click', close);
      m.addEventListener('click', function (e) { if (e.target.closest('a')) close(); });
      d.addEventListener('keydown', function (e) {
        if (!m.classList.contains('is-open')) return;
        if (e.key === 'Escape') { e.preventDefault(); close(); }
        if (e.key === 'Tab') {
          var q = m.querySelectorAll('a[href],button:not([disabled])'), f = q[0], l = q[q.length - 1];
          if (e.shiftKey && d.activeElement === f) { e.preventDefault(); l.focus(); }
          else if (!e.shiftKey && d.activeElement === l) { e.preventDefault(); f.focus(); }
        }
      });
      window.addEventListener('resize', function () { if (innerWidth > 860 && m.classList.contains('is-open')) close(); });
    }

    /* Filtre des guides (accueil) */
    var bar = d.querySelector('.lgp-filters');
    if (bar) {
      var cards = [].slice.call(d.querySelectorAll('.lgp-card[data-category]')), btns = [].slice.call(bar.querySelectorAll('.lgp-filter'));
      bar.addEventListener('click', function (e) {
        var btn = e.target.closest('.lgp-filter'); if (!btn) return;
        var f = btn.getAttribute('data-filter');
        btns.forEach(function (x) { x.setAttribute('aria-pressed', String(x === btn)); });
        cards.forEach(function (card) { card.hidden = !(f === 'all' || card.getAttribute('data-category') === f); });
      });
    }

    /* Emplacements de test visibles uniquement en local / preview */
    var h = location.hostname;
    d.body.classList.toggle('preview-mode', h === 'localhost' || h === '127.0.0.1' || /\.workers\.dev$/.test(h));


    /* En-tête : se masque en descendant, réapparaît en remontant */
    var hd = d.querySelector('.lgp-header');
    if (hd) {
      var lastY = window.scrollY, ticking = false;
      var setHidden = function (v) { hd.classList.toggle('is-hidden', v); };
      var onScroll = function () {
        var y = window.scrollY, dy = y - lastY;
        var menuOpen = d.documentElement.classList.contains('lgp-lock');
        if (y < hd.offsetHeight || menuOpen || hd.contains(d.activeElement)) setHidden(false);
        else if (dy > 8) setHidden(true);
        else if (dy < -8) setHidden(false);
        if (Math.abs(dy) > 8 || y < hd.offsetHeight) lastY = y;
        ticking = false;
      };
      window.addEventListener('scroll', function () { if (!ticking) { ticking = true; requestAnimationFrame(onScroll); } }, { passive: true });
      hd.addEventListener('focusin', function () { setHidden(false); });
    }

    /* Barre de progression de lecture (articles) */
    var art = d.querySelector('main.article-content');
    if (art) {
      var bar = d.createElement('div'); bar.className = 'lgp-progress'; bar.setAttribute('aria-hidden', 'true'); d.body.appendChild(bar);
      var pt = false;
      var upd = function () {
        var r = art.getBoundingClientRect(), total = r.height - window.innerHeight;
        var p = total > 0 ? Math.min(1, Math.max(0, -r.top / total)) : 0;
        bar.style.transform = 'scaleX(' + p + ')'; pt = false;
      };
      window.addEventListener('scroll', function () { if (!pt) { pt = true; requestAnimationFrame(upd); } }, { passive: true });
      upd();
    }

    /* Retour en haut */
    var top = d.getElementById('lgp-top');
    if (top) {
      var tick = false;
      window.addEventListener('scroll', function () {
        if (tick) return; tick = true;
        requestAnimationFrame(function () { top.classList.toggle('is-on', window.scrollY > 900); tick = false; });
      }, { passive: true });
      top.addEventListener('click', function () {
        var reduce = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;
        window.scrollTo({ top: 0, behavior: reduce ? 'auto' : 'smooth' });
      });
    }
  });
})();
