/* Human-Agent Decision Making — Main JS */
(function() {
  'use strict';

  // Smooth scroll for anchor links
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
      const target = document.querySelector(this.getAttribute('href'));
      if (target) {
        e.preventDefault();
        target.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
    });
  });

  // Active nav link highlighting
  const currentPath = window.location.pathname;
  document.querySelectorAll('.nav-links a').forEach(link => {
    if (link.classList.contains('active')) return;
    const href = link.getAttribute('href');
    if (href && currentPath.includes(href) && href !== 'index.html') {
      link.style.color = 'var(--text)';
    }
  });
})();
