#!/bin/bash
# NexCore Technologies — Quick Setup Script
set -e

echo "========================================"
echo "  NexCore Technologies — Django Setup"
echo "========================================"

# 1. Create and activate virtual environment
echo ""
echo "→ Creating virtual environment..."
python -m venv venv
source venv/bin/activate

# 2. Install dependencies
echo "→ Installing Django..."
pip install -r requirements.txt --quiet

# 3. Run migrations (creates SQLite db + seeds initial content)
echo "→ Running migrations & seeding data..."
python manage.py migrate --run-syncdb

# 4. Create superuser for admin
echo ""
echo "→ Creating admin superuser..."
echo "  (Enter credentials for the /admin panel)"
python manage.py createsuperuser

# 5. Done
echo ""
echo "========================================"
echo "  Setup complete! Run the server with:"
echo ""
echo "  source venv/bin/activate"
echo "  python manage.py runserver"
echo ""
echo "  Then open: http://127.0.0.1:8000"
echo "  Admin:     http://127.0.0.1:8000/admin"
echo "========================================"
