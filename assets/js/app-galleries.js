/* Progressive enhancement for the app screenshot shelves. No stored state or tracking. */
(() => {
  'use strict';
  const galleries = Array.from(document.querySelectorAll('[data-gallery]'));
  if (!galleries.length) return;
  const reducedMotion = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const dialog = document.querySelector('.screenshot-lightbox');
  const canOpenViewer = dialog && typeof dialog.showModal === 'function';
  let viewerItems = [];
  let viewerIndex = 0;
  let viewerTrigger = null;
  let previousOverflow = '';

  function showImage(index) {
    viewerIndex = (index + viewerItems.length) % viewerItems.length;
    const source = viewerItems[viewerIndex].querySelector('img');
    const image = dialog.querySelector('img');
    const status = dialog.querySelector('[data-viewer-status]');
    status.textContent = 'Loading screenshot…';
    image.onload = () => { status.textContent = ''; };
    image.onerror = () => { status.textContent = 'This screenshot could not be loaded. Use Open image to try it directly.'; };
    image.alt = source.alt;
    image.src = source.src;
    dialog.querySelector('[data-viewer-original]').href = source.src;
    dialog.querySelector('[data-viewer-count]').textContent = `${viewerIndex + 1} / ${viewerItems.length}`;
  }

  function closeViewer() {
    document.body.style.overflow = previousOverflow;
    dialog.close();
  }

  if (canOpenViewer) {
    dialog.querySelector('[data-viewer-close]').addEventListener('click', closeViewer);
    dialog.addEventListener('cancel', () => { document.body.style.overflow = previousOverflow; });
    dialog.addEventListener('close', () => {
      document.body.style.overflow = previousOverflow;
      viewerTrigger?.focus({ preventScroll: true });
    });
    dialog.querySelectorAll('[data-viewer-step]').forEach(button => {
      button.addEventListener('click', () => showImage(viewerIndex + Number(button.dataset.viewerStep)));
    });
    dialog.addEventListener('keydown', event => {
      if (!['ArrowLeft', 'ArrowRight'].includes(event.key) || event.altKey || event.ctrlKey || event.metaKey) return;
      event.preventDefault();
      showImage(viewerIndex + (event.key === 'ArrowRight' ? 1 : -1));
    });
  }

  galleries.forEach(gallery => {
    const rails = Array.from(gallery.querySelectorAll('[data-rail]'));
    if (!rails.length) return;
    const currentRail = () => rails.find(rail => !rail.hidden);
    const itemsIn = rail => Array.from(rail.querySelectorAll('.store-shot'));
    const offsetIn = (shot, rail) => shot.getBoundingClientRect().left - rail.getBoundingClientRect().left + rail.scrollLeft;
    const currentIndex = rail => {
      const items = itemsIn(rail);
      return items.reduce((best, shot, index) => Math.abs(offsetIn(shot, rail) - rail.scrollLeft) < Math.abs(offsetIn(items[best], rail) - rail.scrollLeft) ? index : best, 0);
    };
    function updateControls() {
      const rail = currentRail();
      if (!rail?.clientWidth) return;
      const count = itemsIn(rail).length;
      gallery.querySelector('.gallery-count').textContent = `${currentIndex(rail) + 1} / ${count}`;
      gallery.querySelector('[data-gallery-step="-1"]').disabled = rail.scrollLeft < 4;
      gallery.querySelector('[data-gallery-step="1"]').disabled = rail.scrollLeft + rail.clientWidth >= rail.scrollWidth - 4;
    }
    function step(direction) {
      const rail = currentRail();
      const items = itemsIn(rail);
      const index = Math.max(0, Math.min(items.length - 1, currentIndex(rail) + direction));
      rail.scrollTo({ left: offsetIn(items[index], rail) - 4, behavior: reducedMotion ? 'instant' : 'smooth' });
    }
    gallery.querySelectorAll('[data-gallery-controls]').forEach(controls => { controls.hidden = false; });
    gallery.querySelectorAll('[data-gallery-step]').forEach(button => {
      button.addEventListener('click', () => step(Number(button.dataset.galleryStep)));
    });
    gallery.querySelectorAll('[data-platform]').forEach(button => {
      button.addEventListener('click', () => {
        rails.forEach(rail => { rail.hidden = rail.dataset.rail !== button.dataset.platform; });
        gallery.querySelectorAll('[data-platform]').forEach(option => {
          const selected = option === button;
          option.setAttribute('aria-pressed', String(selected));
          option.classList.toggle('is-active', selected);
        });
        const source = gallery.querySelector('.store-gallery__source a');
        const android = button.dataset.platform === 'android';
        source.href = android ? gallery.dataset.androidSource : gallery.dataset.appleSource;
        source.textContent = android ? 'View on Google Play ↗' : 'View on the App Store ↗';
        updateControls();
      });
    });
    rails.forEach(rail => {
      let scheduled = false;
      rail.addEventListener('scroll', () => {
        if (scheduled) return;
        scheduled = true;
        requestAnimationFrame(() => { updateControls(); scheduled = false; });
      }, { passive: true });
      rail.addEventListener('keydown', event => {
        if (event.target !== rail || !['ArrowLeft', 'ArrowRight'].includes(event.key)) return;
        event.preventDefault();
        step(event.key === 'ArrowRight' ? 1 : -1);
      });
      rail.querySelectorAll('img').forEach(image => image.addEventListener('load', updateControls));
      if (canOpenViewer) {
        rail.querySelectorAll('[data-lightbox]').forEach(link => {
          link.addEventListener('click', event => {
            if (event.metaKey || event.ctrlKey || event.shiftKey || event.altKey) return;
            event.preventDefault();
            viewerTrigger = link;
            viewerItems = itemsIn(rail);
            previousOverflow = document.body.style.overflow;
            dialog.querySelector('#screenshot-viewer-title').textContent = gallery.getAttribute('aria-label');
            showImage(viewerItems.indexOf(link));
            dialog.showModal();
            document.body.style.overflow = 'hidden';
            dialog.querySelector('[data-viewer-close]').focus();
          });
        });
      }
    });
    if (typeof ResizeObserver === 'function') {
      new ResizeObserver(updateControls).observe(gallery);
    } else {
      window.addEventListener('resize', updateControls, { passive: true });
    }
    requestAnimationFrame(updateControls);
  });
})();
