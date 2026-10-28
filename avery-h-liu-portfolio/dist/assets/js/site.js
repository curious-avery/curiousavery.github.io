(() => {
  const header = document.querySelector('[data-header]');
  const menuButton = document.querySelector('[data-menu-button]');
  const nav = document.querySelector('[data-nav]');
  const navLinks = [...document.querySelectorAll('.site-nav a[href^="#"]')];
  const sections = [...document.querySelectorAll('main section[id]')];
  const filters = [...document.querySelectorAll('[data-filter]')];
  const projects = [...document.querySelectorAll('[data-project-card]')];
  const slides = [...document.querySelectorAll('[data-slide]')];
  const currentLabel = document.querySelector('[data-gallery-current]');
  let currentSlide = 0;

  const setSlide = (next) => {
    currentSlide = (next + slides.length) % slides.length;
    slides.forEach((slide, index) => {
      const active = index === currentSlide;
      slide.classList.toggle('is-active', active);
      slide.setAttribute('aria-hidden', String(!active));
    });
    if (currentLabel) currentLabel.textContent = String(currentSlide + 1);
  };

  document.querySelector('[data-gallery-prev]')?.addEventListener('click', () => setSlide(currentSlide - 1));
  document.querySelector('[data-gallery-next]')?.addEventListener('click', () => setSlide(currentSlide + 1));

  menuButton?.addEventListener('click', () => {
    const open = menuButton.getAttribute('aria-expanded') === 'true';
    menuButton.setAttribute('aria-expanded', String(!open));
    nav?.classList.toggle('is-open', !open);
  });

  navLinks.forEach((link) => link.addEventListener('click', () => {
    menuButton?.setAttribute('aria-expanded', 'false');
    nav?.classList.remove('is-open');
  }));

  filters.forEach((button) => button.addEventListener('click', () => {
    const selected = button.dataset.filter;
    filters.forEach((item) => {
      const active = item === button;
      item.classList.toggle('is-active', active);
      item.setAttribute('aria-pressed', String(active));
    });
    projects.forEach((project) => {
      const tags = project.dataset.tags.split(' ');
      project.hidden = selected !== 'all' && !tags.includes(selected);
    });
  }));

  const revealObserver = new IntersectionObserver((entries, observer) => {
    entries.forEach((entry) => {
      if (!entry.isIntersecting) return;
      entry.target.classList.add('is-visible');
      observer.unobserve(entry.target);
    });
  }, { threshold: .12, rootMargin: '0px 0px -4% 0px' });
  document.querySelectorAll('.reveal').forEach((element) => revealObserver.observe(element));

  const sectionObserver = new IntersectionObserver((entries) => {
    const visible = entries.filter((entry) => entry.isIntersecting).sort((a, b) => b.intersectionRatio - a.intersectionRatio)[0];
    if (!visible) return;
    navLinks.forEach((link) => link.classList.toggle('is-active', link.getAttribute('href') === `#${visible.target.id}`));
  }, { threshold: [0.2, 0.5], rootMargin: '-22% 0px -55% 0px' });
  sections.forEach((section) => sectionObserver.observe(section));

  const year = document.querySelector('[data-year]');
  if (year) year.textContent = new Date().getFullYear();

  window.addEventListener('scroll', () => header?.classList.toggle('is-scrolled', window.scrollY > 16), { passive: true });
})();
