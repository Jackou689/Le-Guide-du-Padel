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

document.addEventListener('DOMContentLoaded', () => {
    const openButton = document.getElementById('mobile-menu-toggle');
    const closeButton = document.getElementById('mobile-menu-close');
    const menu = document.getElementById('mobile-menu');
    const overlay = document.getElementById('mobile-menu-overlay');

    if (!openButton || !closeButton || !menu || !overlay) return;

    let lastFocusedElement = null;

    const focusableElements = () => Array.from(
        menu.querySelectorAll('a[href], button:not([disabled]), [tabindex]:not([tabindex="-1"])')
    );

    const openMenu = () => {
        lastFocusedElement = document.activeElement;
        menu.classList.add('is-open');
        overlay.classList.add('is-open');
        overlay.hidden = false;
        menu.setAttribute('aria-hidden', 'false');
        openButton.setAttribute('aria-expanded', 'true');
        openButton.setAttribute('aria-label', 'Fermer le menu');
        document.documentElement.classList.add('mobile-menu-open');
        document.body.classList.add('mobile-menu-open');
        window.requestAnimationFrame(() => closeButton.focus());
    };

    const closeMenu = () => {
        menu.classList.remove('is-open');
        overlay.classList.remove('is-open');
        menu.setAttribute('aria-hidden', 'true');
        openButton.setAttribute('aria-expanded', 'false');
        openButton.setAttribute('aria-label', 'Ouvrir le menu');
        document.documentElement.classList.remove('mobile-menu-open');
        document.body.classList.remove('mobile-menu-open');
        window.setTimeout(() => {
            overlay.hidden = true;
            if (lastFocusedElement) lastFocusedElement.focus();
        }, 200);
    };

    openButton.addEventListener('click', () => {
        if (menu.classList.contains('is-open')) closeMenu();
        else openMenu();
    });
    closeButton.addEventListener('click', closeMenu);
    overlay.addEventListener('click', closeMenu);
    menu.querySelectorAll('a').forEach(link => link.addEventListener('click', closeMenu));

    document.addEventListener('keydown', event => {
        if (!menu.classList.contains('is-open')) return;
        if (event.key === 'Escape') {
            event.preventDefault();
            closeMenu();
            return;
        }
        if (event.key === 'Tab') {
            const items = focusableElements();
            if (!items.length) return;
            const first = items[0];
            const last = items[items.length - 1];
            if (event.shiftKey && document.activeElement === first) {
                event.preventDefault();
                last.focus();
            } else if (!event.shiftKey && document.activeElement === last) {
                event.preventDefault();
                first.focus();
            }
        }
    });

    window.addEventListener('resize', () => {
        if (window.innerWidth >= 768 && menu.classList.contains('is-open')) closeMenu();
    });
});
