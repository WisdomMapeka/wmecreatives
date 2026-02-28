/**
 * NexCore Technologies — Main JavaScript
 * Works with the Django backend:
 *   - AJAX contact form with CSRF token
 *   - Server-side field error display
 *   - Navbar, scroll reveal, hamburger, parallax, counters
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

/* ── 1. Navbar scroll effect ──────────────────────────────── */
function initNavbar() {
  const navbar = document.getElementById('navbar');
  if (!navbar) return;

  const update = () => navbar.classList.toggle('scrolled', window.scrollY > 40);
  window.addEventListener('scroll', update, { passive: true });
  update();
}

/* ── 2. Mobile hamburger ──────────────────────────────────── */
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

  const observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.1, rootMargin: '0px 0px -40px 0px' });

  els.forEach(el => observer.observe(el));
}

/* ── 4. Smooth scroll ─────────────────────────────────────── */
function initSmoothScroll() {
  document.querySelectorAll('a[href^="#"]').forEach(a => {
    a.addEventListener('click', e => {
      const target = document.querySelector(a.getAttribute('href'));
      if (!target) return;
      e.preventDefault();
      const navH = document.getElementById('navbar')?.offsetHeight || 70;
      window.scrollTo({ top: target.getBoundingClientRect().top + window.scrollY - navH, behavior: 'smooth' });
    });
  });
}

/* ── 5. Active nav links ──────────────────────────────────── */
function initActiveNavLinks() {
  const sections = document.querySelectorAll('section[id]');
  const navLinks = document.querySelectorAll('.nav-link');

  const observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const id = entry.target.id;
        navLinks.forEach(link => {
          link.style.color = link.getAttribute('href')?.includes(`#${id}`) ? '#fff' : '';
        });
      }
    });
  }, { threshold: 0.4 });

  sections.forEach(s => observer.observe(s));
}

/* ── 6. Django AJAX Contact Form ──────────────────────────── */
function initContactForm() {
  const form = document.getElementById('contactForm');
  if (!form) return;

  const submitUrl = form.dataset.submitUrl;
  const csrfToken = form.querySelector('[name=csrfmiddlewaretoken]')?.value;
  const successEl = document.getElementById('formSuccess');
  const successMsg = document.getElementById('successMsg');
  const btn      = form.querySelector('button[type="submit"]');
  const btnText  = form.querySelector('.btn-text');

  // Helper: set or clear a field error
  const setError = (fieldName, msg) => {
    const el = document.getElementById(`err-${fieldName}`);
    const input = form.querySelector(`[name="${fieldName}"]`);
    if (el) el.textContent = msg;
    if (input) input.classList.toggle('error', !!msg);
  };

  const clearErrors = () => {
    form.querySelectorAll('.field-error').forEach(el => el.textContent = '');
    form.querySelectorAll('.error').forEach(el => el.classList.remove('error'));
  };

  // Inline validation on blur
  form.querySelectorAll('input, select, textarea').forEach(field => {
    field.addEventListener('blur', () => {
      if (field.hasAttribute('required') && !field.value.trim()) {
        setError(field.name, 'This field is required.');
      } else if (field.type === 'email' && field.value && !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(field.value)) {
        setError(field.name, 'Please enter a valid email address.');
      } else {
        setError(field.name, '');
      }
    });
    field.addEventListener('input', () => {
      if (field.classList.contains('error')) setError(field.name, '');
    });
  });

  form.addEventListener('submit', async (e) => {
    e.preventDefault();
    clearErrors();

    // Loading state
    btn.disabled = true;
    btnText.textContent = 'Sending…';

    try {
      const response = await fetch(submitUrl, {
        method: 'POST',
        headers: {
          'X-CSRFToken': csrfToken,
          'X-Requested-With': 'XMLHttpRequest',
        },
        body: new FormData(form),
      });

      const data = await response.json();

      if (data.success) {
        // Success
        form.reset();
        if (successMsg) successMsg.textContent = data.message;
        if (successEl)  successEl.classList.add('show');
        setTimeout(() => successEl?.classList.remove('show'), 6000);
      } else {
        // Show server-side field errors
        if (data.errors) {
          Object.entries(data.errors).forEach(([field, msgs]) => {
            setError(field, msgs[0]);
          });
          shakeForm(form);
        }
      }
    } catch (err) {
      setError('message', 'Something went wrong. Please try again.');
    } finally {
      btn.disabled = false;
      btnText.textContent = 'Send Message';
    }
  });
}

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
    { duration: 400, easing: 'ease-in-out' }
  );
}

/* ── 7. Counter animation ─────────────────────────────────── */
function initCounters() {
  const stats = document.querySelectorAll('.stat strong');
  if (!stats.length) return;

  const animateStat = (el) => {
    const text = el.textContent;
    const num  = parseInt(text.match(/\d+/)?.[0] || '0', 10);
    const suffix = text.replace(/[\d]/g, '');
    const dur  = 1400;
    const step = Math.ceil(num / (dur / 16));
    let cur = 0;
    const tick = () => {
      cur = Math.min(cur + step, num);
      el.textContent = cur + suffix;
      if (cur < num) requestAnimationFrame(tick);
    };
    requestAnimationFrame(tick);
  };

  const statsWrap = document.querySelector('.hero-stats');
  if (!statsWrap) return;

  new IntersectionObserver(([entry], obs) => {
    if (entry.isIntersecting) {
      stats.forEach(animateStat);
      obs.disconnect();
    }
  }, { threshold: 0.5 }).observe(statsWrap);
}

/* ── 8. Mouse parallax on hero orbs ──────────────────────── */
function initParallax() {
  const orbs = document.querySelectorAll('.orb');
  if (!orbs.length) return;
  if (!window.matchMedia('(pointer: fine)').matches) return;

  document.addEventListener('mousemove', e => {
    const x = (e.clientX / window.innerWidth - 0.5) * 2;
    const y = (e.clientY / window.innerHeight - 0.5) * 2;
    orbs.forEach((orb, i) => {
      const s = (i + 1) * 9;
      orb.style.transform = `translate(${x * s}px, ${y * s}px)`;
    });
  }, { passive: true });
}
