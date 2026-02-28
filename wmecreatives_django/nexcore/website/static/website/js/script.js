/**
 * NexCore Technologies — Main JavaScript
 * Handles: Navbar, Hamburger, Scroll Reveal, Smooth Scroll,
 *          Active Nav Links, AJAX Contact Form, Counter, Parallax
 */

document.addEventListener('DOMContentLoaded', () => {
  initNavbar();
  initHamburger();
  initScrollReveal();
  initSmoothScroll();
  initActiveNavLinks();
  initContactForm();
  initCounters();
  initParallax();
});

/* ── 1. Navbar Scroll ─────────────────────────────────────── */
function initNavbar() {
  const navbar = document.getElementById('navbar');
  if (!navbar) return;
  const onScroll = () => navbar.classList.toggle('scrolled', window.scrollY > 40);
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();
}

/* ── 2. Hamburger Menu ────────────────────────────────────── */
function initHamburger() {
  const btn   = document.getElementById('hamburger');
  const links = document.getElementById('navLinks');
  if (!btn || !links) return;

  const close = () => {
    links.classList.remove('open');
    btn.classList.remove('active');
    btn.setAttribute('aria-expanded', 'false');
    document.body.style.overflow = '';
  };

  btn.addEventListener('click', () => {
    const open = links.classList.toggle('open');
    btn.classList.toggle('active', open);
    btn.setAttribute('aria-expanded', open);
    document.body.style.overflow = open ? 'hidden' : '';
  });

  links.querySelectorAll('a').forEach(a => a.addEventListener('click', close));
  document.addEventListener('click', e => {
    if (!links.contains(e.target) && !btn.contains(e.target)) close();
  });
}

/* ── 3. Scroll Reveal ─────────────────────────────────────── */
function initScrollReveal() {
  const els = document.querySelectorAll('.reveal');
  if (!els.length) return;
  const obs = new IntersectionObserver(entries => {
    entries.forEach(e => {
      if (e.isIntersecting) {
        e.target.classList.add('visible');
        obs.unobserve(e.target);
      }
    });
  }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });
  els.forEach(el => obs.observe(el));
}

/* ── 4. Smooth Scroll ─────────────────────────────────────── */
function initSmoothScroll() {
  document.querySelectorAll('a[href*="#"]').forEach(anchor => {
    anchor.addEventListener('click', e => {
      const hash = anchor.getAttribute('href').split('#')[1];
      if (!hash) return;
      const target = document.getElementById(hash);
      if (!target) return;
      e.preventDefault();
      const navH = document.getElementById('navbar')?.offsetHeight || 70;
      window.scrollTo({ top: target.getBoundingClientRect().top + window.scrollY - navH, behavior: 'smooth' });
    });
  });
}

/* ── 5. Active Nav Highlighting ───────────────────────────── */
function initActiveNavLinks() {
  const sections = document.querySelectorAll('section[id]');
  const navLinks = document.querySelectorAll('.nav-link');
  if (!sections.length) return;

  const obs = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const id = entry.target.id;
        navLinks.forEach(link => {
          const href = link.getAttribute('href') || '';
          link.style.color = href.endsWith(`#${id}`) ? '#fff' : '';
        });
      }
    });
  }, { threshold: 0.4 });

  sections.forEach(s => obs.observe(s));
}

/* ── 6. AJAX Contact Form ─────────────────────────────────── */
function initContactForm() {
  const form       = document.getElementById('contactForm');
  const successDiv = document.getElementById('formSuccess');
  const successMsg = document.getElementById('successMsg');
  const submitBtn  = document.getElementById('submitBtn');
  if (!form) return;

  const showError = (field, msg) => {
    const el = document.getElementById(`err-${field}`);
    const input = form.querySelector(`[name="${field}"]`);
    if (el) el.textContent = msg;
    if (input) input.classList.add('error');
  };

  const clearErrors = () => {
    form.querySelectorAll('.field-error').forEach(el => el.textContent = '');
    form.querySelectorAll('.form-input').forEach(el => el.classList.remove('error'));
  };

  // Live clear on input
  form.querySelectorAll('.form-input').forEach(input => {
    input.addEventListener('input', () => {
      input.classList.remove('error');
      const errEl = document.getElementById(`err-${input.name}`);
      if (errEl) errEl.textContent = '';
    });
  });

  form.addEventListener('submit', async e => {
    e.preventDefault();
    clearErrors();

    const url  = form.dataset.url;
    const data = new FormData(form);
    const btnText = submitBtn.querySelector('.btn-text');

    submitBtn.disabled = true;
    if (btnText) btnText.textContent = 'Sending…';

    try {
      const res  = await fetch(url, {
        method: 'POST',
        body: data,
        headers: { 'X-Requested-With': 'XMLHttpRequest' }
      });

      const json = await res.json();

      if (json.success) {
        form.reset();
        if (successMsg) successMsg.textContent = json.message;
        if (successDiv) successDiv.classList.add('show');
        setTimeout(() => successDiv?.classList.remove('show'), 6000);
      } else {
        // Show field-level errors from Django form validation
        if (json.errors) {
          Object.entries(json.errors).forEach(([field, errs]) => {
            const msg = Array.isArray(errs) ? errs.map(e => e.message).join(' ') : errs;
            showError(field, msg);
          });
        }
        shakeForm(form);
      }
    } catch (err) {
      showError('message', 'Something went wrong. Please try again.');
    } finally {
      submitBtn.disabled = false;
      if (btnText) btnText.textContent = 'Send Message';
    }
  });
}

/* ── 7. Stat Counters ─────────────────────────────────────── */
function initCounters() {
  const stats = document.querySelector('.hero-stats');
  if (!stats) return;

  const obs = new IntersectionObserver(([entry]) => {
    if (!entry.isIntersecting) return;
    obs.disconnect();

    stats.querySelectorAll('strong').forEach(el => {
      const text  = el.textContent;
      const match = text.match(/\d+/);
      if (!match) return;
      const end    = parseInt(match[0], 10);
      const suffix = text.replace(/\d/g, '');
      const dur    = 1400;
      const step   = Math.max(1, Math.ceil(end / (dur / 16)));
      let cur      = 0;

      const tick = () => {
        cur = Math.min(cur + step, end);
        el.textContent = cur + suffix;
        if (cur < end) requestAnimationFrame(tick);
      };
      requestAnimationFrame(tick);
    });
  }, { threshold: 0.5 });

  obs.observe(stats);
}

/* ── 8. Mouse Parallax Orbs ───────────────────────────────── */
function initParallax() {
  const orbs = document.querySelectorAll('.orb');
  if (!orbs.length) return;
  if (!window.matchMedia('(pointer: fine)').matches) return;

  document.addEventListener('mousemove', e => {
    const x = (e.clientX / window.innerWidth  - 0.5) * 2;
    const y = (e.clientY / window.innerHeight - 0.5) * 2;
    orbs.forEach((orb, i) => {
      const s = (i + 1) * 10;
      orb.style.transform = `translate(${x * s}px, ${y * s}px)`;
    });
  }, { passive: true });
}

/* ── Shake helper ─────────────────────────────────────────── */
function shakeForm(el) {
  el.animate(
    [
      { transform: 'translateX(0)' },
      { transform: 'translateX(-7px)' },
      { transform: 'translateX(7px)' },
      { transform: 'translateX(-5px)' },
      { transform: 'translateX(5px)' },
      { transform: 'translateX(0)' },
    ],
    { duration: 420, easing: 'ease-in-out' }
  );
}
