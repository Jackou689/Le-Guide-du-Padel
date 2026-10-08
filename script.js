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
