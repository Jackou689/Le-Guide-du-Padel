// script.js - Gestion globale du site Le Guide du Padel

document.addEventListener('DOMContentLoaded', () => {
    const themeToggleBtn = document.getElementById('theme-toggle');
    const body = document.body;
    
    // Si la page n'a pas le bouton, on ne fait rien
    if (!themeToggleBtn) return;

    // Fonction pour mettre à jour l'icône (Soleil/Lune)
    const updateIcon = () => {
        if (body.classList.contains('dark-mode')) {
            themeToggleBtn.innerHTML = '☀️'; // Soleil éclatant quand il fait sombre
        } else {
            themeToggleBtn.innerHTML = '🌙'; // Lune jaune quand il fait jour
        }
    };

    // 1. Appliquer le thème mémorisé lors du chargement de la page
    if (localStorage.getItem('theme') === 'dark') {
        body.classList.add('dark-mode');
    }
    
    // Mettre la bonne icône dès le chargement
    updateIcon();

    // 2. Écouter le clic sur le bouton de thème
    themeToggleBtn.addEventListener('click', () => {
        body.classList.toggle('dark-mode');
        
        // Mettre à jour l'icône immédiatement après le clic
        updateIcon();
        
        // 3. Sauvegarder le nouveau choix
        if (body.classList.contains('dark-mode')) {
            localStorage.setItem('theme', 'dark');
        } else {
            localStorage.setItem('theme', 'light');
        }
    });
});