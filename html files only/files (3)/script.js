/**
 * NexCore Technologies — Main JavaScript
 * Handles: Navigation, Scroll Effects, Animations, Form Validation
 */

/* ── DOM Ready ────────────────────────────────────────────── */
document.addEventListener('DOMContentLoaded', () => {
  initNavbar();
  initHamburger();
  initScrollReveal();
  initSmoothScroll();
  initContactForm();
  initActiveNavLinks();
});

/* ── 1. Navbar Scroll Effect ──────────────────────────────── */
function initNavbar() {
  const navbar = document.getElementById('navbar');

  const handleScroll = () => {
    if (window.scrollY > 40) {
      navbar.classList.add('scrolled');
    } else {
      navbar.classList.remove('scrolled');
    }
  };

  window.addEventListener('scroll', handleScroll, { passive: true });
  handleScroll(); // Run on load
}

/* ── 2. Mobile Hamburger Menu ─────────────────────────────── */
function initHamburger() {
  const hamburger = document.getElementById('hamburger');
  const navLinks  = document.getElementById('navLinks');

  if (!hamburger || !navLinks) return;

  // Toggle menu on button click
  hamburger.addEventListener('click', () => {
    const isOpen = navLinks.classList.toggle('open');
    hamburger.classList.toggle('active', isOpen);
    hamburger.setAttribute('aria-expanded', isOpen);
    document.body.style.overflow = isOpen ? 'hidden' : '';
  });

  // Close menu when a link is clicked
  navLinks.querySelectorAll('a').forEach(link => {
    link.addEventListener('click', () => {
      navLinks.classList.remove('open');
      hamburger.classList.remove('active');
      hamburger.setAttribute('aria-expanded', 'false');
      document.body.style.overflow = '';
    });
  });

  // Close on outside click
  document.addEventListener('click', (e) => {
    if (!navLinks.contains(e.target) && !hamburger.contains(e.target)) {
      navLinks.classList.remove('open');
      hamburger.classList.remove('active');
      document.body.style.overflow = '';
    }
  });
}

/* ── 3. Scroll Reveal Animation ───────────────────────────── */
function initScrollReveal() {
  const elements = document.querySelectorAll('.reveal');

  if (!elements.length) return;

  // Use IntersectionObserver for performance
  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible');
          // Unobserve after reveal to save resources
          observer.unobserve(entry.target);
        }
      });
    },
    {
      threshold: 0.12,
      rootMargin: '0px 0px -40px 0px'
    }
  );

  elements.forEach(el => observer.observe(el));
}

/* ── 4. Smooth Scroll for Anchor Links ────────────────────── */
function initSmoothScroll() {
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', (e) => {
      const target = document.querySelector(anchor.getAttribute('href'));
      if (!target) return;

      e.preventDefault();

      const navH   = document.getElementById('navbar')?.offsetHeight || 72;
      const top    = target.getBoundingClientRect().top + window.scrollY - navH;

      window.scrollTo({ top, behavior: 'smooth' });
    });
  });
}

/* ── 5. Active Nav Link Highlighting ──────────────────────── */
function initActiveNavLinks() {
  const sections  = document.querySelectorAll('section[id]');
  const navLinks  = document.querySelectorAll('.nav-link');

  if (!sections.length || !navLinks.length) return;

  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          const id = entry.target.getAttribute('id');
          navLinks.forEach(link => {
            const isActive = link.getAttribute('href') === `#${id}`;
            link.style.color = isActive
              ? 'var(--text-primary)'
              : '';
          });
        }
      });
    },
    {
      threshold: 0.4
    }
  );

  sections.forEach(section => observer.observe(section));
}

/* ── 6. Contact Form Validation & Submit ──────────────────── */
function initContactForm() {
  const form        = document.getElementById('contactForm');
  const successMsg  = document.getElementById('formSuccess');

  if (!form) return;

  // Validate a single field
  const validateField = (field) => {
    let valid = true;
    field.classList.remove('error');

    if (field.hasAttribute('required') && !field.value.trim()) {
      valid = false;
    }

    if (field.type === 'email' && field.value.trim()) {
      const emailRe = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      if (!emailRe.test(field.value)) valid = false;
    }

    if (!valid) field.classList.add('error');
    return valid;
  };

  // Live validation on blur
  form.querySelectorAll('input, select, textarea').forEach(field => {
    field.addEventListener('blur', () => validateField(field));
    field.addEventListener('input', () => {
      if (field.classList.contains('error')) validateField(field);
    });
  });

  // Form submission
  form.addEventListener('submit', (e) => {
    e.preventDefault();

    // Validate all required fields
    let allValid = true;
    form.querySelectorAll('input[required], select, textarea[required]').forEach(field => {
      if (!validateField(field)) allValid = false;
    });

    if (!allValid) {
      // Shake effect on invalid submit
      form.style.animation = 'none';
      form.offsetHeight; // reflow
      shakeElement(form);
      return;
    }

    // Simulate async send (front-end only)
    const btn      = form.querySelector('.btn');
    const btnText  = form.querySelector('.btn-text');

    btn.disabled   = true;
    btnText.textContent = 'Sending…';

    setTimeout(() => {
      // Success state
      form.reset();
      btn.disabled    = false;
      btnText.textContent = 'Send Message';

      if (successMsg) {
        successMsg.classList.add('show');
        setTimeout(() => successMsg.classList.remove('show'), 5000);
      }
    }, 1400);
  });
}

/* ── Helper: Shake animation ──────────────────────────────── */
function shakeElement(el) {
  el.animate(
    [
      { transform: 'translateX(0)' },
      { transform: 'translateX(-8px)' },
      { transform: 'translateX(8px)' },
      { transform: 'translateX(-6px)' },
      { transform: 'translateX(6px)' },
      { transform: 'translateX(-4px)' },
      { transform: 'translateX(0)' }
    ],
    { duration: 450, easing: 'ease-in-out' }
  );
}

/* ── 7. Hero Stats Counter Animation ──────────────────────── */
function animateCounters() {
  const stats = document.querySelectorAll('.stat strong');

  stats.forEach(stat => {
    const text    = stat.textContent;
    const numMatch = text.match(/\d+/);
    if (!numMatch) return;

    const end     = parseInt(numMatch[0], 10);
    const suffix  = text.replace(/[\d]/g, '');
    const duration = 1400;
    const step    = Math.ceil(end / (duration / 16));
    let current   = 0;

    const tick = () => {
      current = Math.min(current + step, end);
      stat.textContent = current + suffix;
      if (current < end) requestAnimationFrame(tick);
    };

    requestAnimationFrame(tick);
  });
}

// Trigger counter animation when stats come into view
const statsSection = document.querySelector('.hero-stats');
if (statsSection) {
  const counterObserver = new IntersectionObserver(
    ([entry]) => {
      if (entry.isIntersecting) {
        animateCounters();
        counterObserver.disconnect();
      }
    },
    { threshold: 0.5 }
  );
  counterObserver.observe(statsSection);
}

/* ── 8. Parallax Orbs ─────────────────────────────────────── */
(function initParallax() {
  const orbs = document.querySelectorAll('.orb');
  if (!orbs.length) return;

  // Only on non-touch devices to avoid jank
  if (window.matchMedia('(pointer: fine)').matches) {
    document.addEventListener('mousemove', (e) => {
      const x = (e.clientX / window.innerWidth - 0.5) * 2;
      const y = (e.clientY / window.innerHeight - 0.5) * 2;

      orbs.forEach((orb, i) => {
        const strength = (i + 1) * 10;
        orb.style.transform = `translate(${x * strength}px, ${y * strength}px)`;
      });
    }, { passive: true });
  }
})();
