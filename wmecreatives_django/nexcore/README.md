# NexCore Technologies — Django Application

A fully dynamic Django website for a technology services company.

## Project Structure

```
nexcore/
├── manage.py
├── requirements.txt
├── setup.sh                  # One-command setup
├── db.sqlite3                # Created after migrations
│
├── nexcore/                  # Django project package
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
└── website/                  # Main app
    ├── models.py             # Service, Stat, CompanyValue, ContactMessage, SiteSettings
    ├── views.py              # home, service_detail, contact_submit (AJAX)
    ├── forms.py              # ContactForm
    ├── admin.py              # Full admin panel configuration
    ├── urls.py
    ├── migrations/
    │   ├── 0001_initial.py
    │   └── 0002_seed_data.py  # Pre-loads all content
    ├── templates/website/
    │   ├── base.html
    │   ├── home.html
    │   ├── service_detail.html
    │   └── partials/
    │       └── service_icon.html
    └── static/website/
        ├── css/styles.css
        └── js/script.js
```

## Quick Start

```bash
# Clone / unzip the project, then:
cd nexcore
bash setup.sh
```

Or manually:

```bash
python -m venv venv
source venv/bin/activate          # Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Open **http://127.0.0.1:8000** in your browser.

## Dynamic Content (Admin Panel)

All website content is fully editable via **http://127.0.0.1:8000/admin**:

| Model | What it controls |
|---|---|
| **SiteSettings** | Hero text, contact info, footer tagline, social links |
| **Service** | All 6 service cards — title, description, tags, featured flag |
| **Stat** | Hero stats (200+, 98%, 12+) |
| **CompanyValue** | About section pillars |
| **ContactMessage** | All form submissions with status tracking |

## Features

- **Homepage** — Hero, Marquee, Services, About, Contact (single page)
- **Service detail pages** — `/services/<slug>/` with full description
- **AJAX contact form** — Submits without page reload; stored in database
- **Admin panel** — Full CRUD for all content, contact message inbox
- **Seed data** — All 6 services, stats, and values pre-loaded on first migrate

## Deployment Notes

For production, update `settings.py`:
- Set `DEBUG = False`
- Set a real `SECRET_KEY`
- Configure `ALLOWED_HOSTS`
- Set up a proper database (PostgreSQL recommended)
- Configure `STATIC_ROOT` and run `python manage.py collectstatic`
