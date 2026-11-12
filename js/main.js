/* CyberSec Wiki — optional progressive enhancement. No network requests. */
(() => {
  'use strict';

  document.documentElement.classList.add('js-enabled');

  // Home: search and category filtering. Cards stay visible without JavaScript.
  const search = document.querySelector('#topic-search');
  const cards = Array.from(document.querySelectorAll('[data-topic-card]'));
  const filterButtons = Array.from(document.querySelectorAll('[data-category-filter]'));
  const categoryLinks = Array.from(document.querySelectorAll('[data-category-link]'));
  const count = document.querySelector('#result-count');
  const empty = document.querySelector('#empty-state');
  const reset = document.querySelector('#reset-filters');
  let category = 'all';

  function normalize(text) {
    return (text || '').normalize('NFKC').toLocaleLowerCase().trim();
  }

  function updateFilters() {
    if (!search) return;
    const query = normalize(search.value);
    let matches = 0;

    cards.forEach((card) => {
      const categoryMatch = category === 'all' || card.dataset.category === category;
      const textMatch = !query || normalize(card.dataset.search).includes(query);
      const visible = categoryMatch && textMatch;
      card.hidden = !visible;
      if (visible) matches++;
    });

    filterButtons.forEach((button) => {
      const active = button.dataset.categoryFilter === category;
      button.setAttribute('aria-pressed', String(active));
      button.classList.toggle('is-active', active);
    });
    if (count) count.textContent = `顯示 ${matches} 篇文章`;
    if (empty) empty.hidden = matches !== 0;
  }

  function setCategory(next) {
    category = next;
    updateFilters();
  }

  if (search) {
    search.addEventListener('input', updateFilters);
    filterButtons.forEach((button) => {
      button.addEventListener('click', () => setCategory(button.dataset.categoryFilter));
    });
    categoryLinks.forEach((link) => {
      link.addEventListener('click', () => setCategory(link.dataset.categoryLink));
    });
    if (reset) {
      reset.addEventListener('click', () => {
        search.value = '';
        setCategory('all');
        search.focus();
      });
    }
    updateFilters();
  }

  // Article: active table-of-contents section while scrolling.
  const tocLinks = Array.from(document.querySelectorAll('.toc-list a[href^="#"]'));
  if (tocLinks.length && 'IntersectionObserver' in window) {
    const sections = tocLinks
      .map((link) => document.getElementById(link.hash.slice(1)))
      .filter(Boolean);
    const observer = new IntersectionObserver((entries) => {
      const showing = entries.filter((entry) => entry.isIntersecting);
      if (!showing.length) return;
      showing.sort((a, b) => a.boundingClientRect.top - b.boundingClientRect.top);
      const id = showing[0].target.id;
      tocLinks.forEach((link) => {
        const active = link.hash === `#${id}`;
        link.classList.toggle('is-current', active);
        if (active) link.setAttribute('aria-current', 'location');
        else link.removeAttribute('aria-current');
      });
    }, { rootMargin: '-16% 0px -68% 0px', threshold: 0 });
    sections.forEach((section) => observer.observe(section));
  }
})();
