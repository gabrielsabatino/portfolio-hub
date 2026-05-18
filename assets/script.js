// ============================================
// PORTFOLIOHUB - Interatividade
// ============================================

// Animação de entrada ao rolar a página
const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
};

const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.opacity = '1';
            entry.target.style.transform = 'translateY(0)';
        }
    });
}, observerOptions);

// Aplicar animação a cards e seções
document.addEventListener('DOMContentLoaded', () => {
    const animatedElements = document.querySelectorAll('.projeto-card, .skill-card, .stat, .contato-card');

    animatedElements.forEach(el => {
        el.style.opacity = '0';
        el.style.transform = 'translateY(30px)';
        el.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
        observer.observe(el);
    });

    // Console message para quem inspecionar
    console.log('%c👋 Bem-vindo ao PortfolioHUB!', 'color: #6366f1; font-size: 20px; font-weight: bold;');
    console.log('%cProjeto desenvolvido com HTML, CSS e JavaScript.', 'color: #94a3b8;');
    console.log('%cVersão: 1.0', 'color: #10b981; font-weight: bold;');
});

// Destacar link ativo na navegação
window.addEventListener('scroll', () => {
    const sections = document.querySelectorAll('section[id]');
    const navLinks = document.querySelectorAll('.nav-links a');

    let current = '';
    sections.forEach(section => {
        const sectionTop = section.offsetTop - 100;
        if (window.scrollY >= sectionTop) {
            current = section.getAttribute('id');
        }
    });

    navLinks.forEach(link => {
        link.style.color = '';
        if (link.getAttribute('href') === `#${current}`) {
            link.style.color = 'var(--color-primary)';
        }
    });
});
