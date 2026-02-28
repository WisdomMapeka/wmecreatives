"""Initial migration for NexCore website app."""
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField(unique=True)),
                ('number', models.PositiveSmallIntegerField(help_text='Display order (01, 02…)')),
                ('icon_key', models.CharField(
                    choices=[('web','Web Development'),('crm','CRM'),('erp','ERP'),
                             ('odoo','Odoo'),('erpnext','ERPNext'),('whatsapp','WhatsApp'),('custom','Custom')],
                    default='custom', max_length=20)),
                ('short_description', models.TextField()),
                ('full_description', models.TextField(blank=True)),
                ('tags', models.CharField(max_length=200)),
                ('is_featured', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={'ordering': ['number']},
        ),
        migrations.CreateModel(
            name='Stat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=20)),
                ('label', models.CharField(max_length=60)),
                ('order', models.PositiveSmallIntegerField(default=0)),
            ],
            options={'ordering': ['order']},
        ),
        migrations.CreateModel(
            name='TeamMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('role', models.CharField(max_length=100)),
                ('bio', models.TextField(blank=True)),
                ('order', models.PositiveSmallIntegerField(default=0)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={'ordering': ['order']},
        ),
        migrations.CreateModel(
            name='CompanyValue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.CharField(default='◈', max_length=10)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('order', models.PositiveSmallIntegerField(default=0)),
            ],
            options={'ordering': ['order']},
        ),
        migrations.CreateModel(
            name='ContactMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=80)),
                ('last_name', models.CharField(max_length=80)),
                ('email', models.EmailField()),
                ('service', models.CharField(blank=True, max_length=100)),
                ('message', models.TextField()),
                ('status', models.CharField(
                    choices=[('new','New'),('read','Read'),('replied','Replied'),('archived','Archived')],
                    default='new', max_length=20)),
                ('submitted_at', models.DateTimeField()),
                ('ip_address', models.GenericIPAddressField(blank=True, null=True)),
            ],
            options={'ordering': ['-submitted_at']},
        ),
        migrations.CreateModel(
            name='SiteSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hero_badge_text', models.CharField(default='Technology & Business Solutions', max_length=100)),
                ('hero_headline_line1', models.CharField(default='We Engineer', max_length=80)),
                ('hero_headline_accent', models.CharField(default='Digital Futures', max_length=80)),
                ('hero_subheadline', models.TextField(default='From custom web platforms to enterprise ERP systems.')),
                ('about_lead', models.TextField(default='NexCore Technologies is a full-service digital transformation partner.')),
                ('office_address', models.TextField(default='123 Tech Boulevard\nSan Francisco, CA 94105')),
                ('email_primary', models.EmailField(default='hello@nexcore.tech')),
                ('email_support', models.EmailField(default='support@nexcore.tech')),
                ('phone', models.CharField(default='+1 (415) 555-0192', max_length=30)),
                ('phone_hours', models.CharField(default='Mon – Fri, 9am – 6pm PST', max_length=60)),
                ('footer_tagline', models.CharField(default='Engineering digital futures for ambitious businesses worldwide.', max_length=160)),
                ('linkedin_url', models.URLField(blank=True, default='#')),
                ('twitter_url', models.URLField(blank=True, default='#')),
                ('github_url', models.URLField(blank=True, default='#')),
            ],
            options={'verbose_name': 'Site Settings', 'verbose_name_plural': 'Site Settings'},
        ),
    ]
