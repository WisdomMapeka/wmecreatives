"""Seed initial content for NexCore website."""
from django.db import migrations
from django.utils import timezone


def seed_data(apps, schema_editor):
    Service = apps.get_model('website', 'Service')
    Stat = apps.get_model('website', 'Stat')
    CompanyValue = apps.get_model('website', 'CompanyValue')
    SiteSettings = apps.get_model('website', 'SiteSettings')

    # Services
    services = [
        dict(number=1, title='Web Development', slug='web-development', icon_key='web',
             short_description='Custom, high-performance websites and web applications built with modern frameworks. Pixel-perfect design meets robust engineering.',
             full_description='We build fast, scalable, and beautiful web applications using modern technologies like React, Next.js, Vue, and Node.js. Every project is engineered for performance, accessibility, and long-term maintainability.',
             tags='React, Next.js, Node.js', is_featured=False),
        dict(number=2, title='CRM Software Solutions', slug='crm-software-solutions', icon_key='crm',
             short_description='Centralize your customer relationships with tailored CRM platforms that automate sales pipelines, track leads, and boost conversion rates.',
             full_description='Our CRM solutions give your sales and support teams a single source of truth. We build or customize CRM platforms that fit your sales process — from lead capture to deal close and post-sale support.',
             tags='Sales Automation, Lead Tracking, Pipelines', is_featured=False),
        dict(number=3, title='ERP Systems', slug='erp-systems', icon_key='erp',
             short_description='Unify your business operations — finance, HR, inventory, and supply chain — in one integrated platform that scales with your organization.',
             full_description='Enterprise Resource Planning done right. We design and implement ERP systems that connect every department, eliminate data silos, and give leadership real-time visibility across the business.',
             tags='Finance, HR, Inventory, Supply Chain', is_featured=False),
        dict(number=4, title='Odoo Implementation', slug='odoo-implementation', icon_key='odoo',
             short_description='Expert Odoo configuration, customization, and deployment. We map your business processes to Odoo modules for a seamless digital transformation.',
             full_description='As certified Odoo partners, we handle everything from initial discovery and module selection to data migration, custom module development, user training, and ongoing support.',
             tags='Odoo 17, Custom Modules, Migration', is_featured=False),
        dict(number=5, title='ERPNext Implementation', slug='erpnext-implementation', icon_key='erpnext',
             short_description='Open-source ERP power with enterprise reliability. We implement and customize ERPNext to fit your industry-specific workflows precisely.',
             full_description='ERPNext on the Frappe framework gives you a powerful, open-source ERP at a fraction of the cost of proprietary solutions. We handle setup, customization, and hosting so you get all the benefits with none of the headaches.',
             tags='Frappe, Open Source, Custom Workflows', is_featured=False),
        dict(number=6, title='WhatsApp Chatbot Development', slug='whatsapp-chatbot-development', icon_key='whatsapp',
             short_description='Intelligent, conversational chatbots on WhatsApp Business API. Automate customer support, lead qualification, and order management 24/7.',
             full_description='WhatsApp has over 2 billion users — meet your customers where they already are. We build smart chatbots using the WhatsApp Business API that can handle support queries, qualify leads, process orders, and escalate to human agents when needed.',
             tags='WhatsApp API, AI-Powered, 24/7 Automation', is_featured=True),
    ]

    for s in services:
        Service.objects.create(**s)

    # Stats
    stats = [
        dict(value='200+', label='Projects Delivered', order=1),
        dict(value='98%',  label='Client Retention',   order=2),
        dict(value='12+',  label='Years Experience',   order=3),
    ]
    for s in stats:
        Stat.objects.create(**s)

    # Company values
    values = [
        dict(icon='◈', title='Strategic Thinking',
             description="We don't just implement software — we understand your business model and design solutions that create real competitive advantage.",
             order=1),
        dict(icon='◈', title='End-to-End Delivery',
             description='From discovery and architecture to deployment and ongoing support — we\'re with you at every stage of your digital journey.',
             order=2),
        dict(icon='◈', title='Open-Source Expertise',
             description='Deep specialization in Odoo and ERPNext means you get enterprise-grade solutions without the enterprise-grade licensing costs.',
             order=3),
    ]
    for v in values:
        CompanyValue.objects.create(**v)

    # Site settings
    SiteSettings.objects.create(
        pk=1,
        hero_badge_text='Technology & Business Solutions',
        hero_headline_line1='We Engineer',
        hero_headline_accent='Digital Futures',
        hero_subheadline='From custom web platforms to enterprise ERP systems — NexCore delivers end-to-end technology solutions that transform how businesses operate, grow, and compete.',
        about_lead="NexCore Technologies is a full-service digital transformation partner for businesses ready to scale. Since 2012, we've helped companies across industries modernize their operations through smart technology choices.",
        office_address='Innovation Hub, 4th Floor\n123 Tech Boulevard, Suite 400\nSan Francisco, CA 94105',
        email_primary='hello@nexcore.tech',
        email_support='support@nexcore.tech',
        phone='+1 (415) 555-0192',
        phone_hours='Mon – Fri, 9am – 6pm PST',
        footer_tagline='Engineering digital futures for ambitious businesses worldwide.',
        linkedin_url='#',
        twitter_url='#',
        github_url='#',
    )


def unseed_data(apps, schema_editor):
    for model_name in ['Service', 'Stat', 'CompanyValue', 'SiteSettings']:
        apps.get_model('website', model_name).objects.all().delete()


class Migration(migrations.Migration):
    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(seed_data, unseed_data),
    ]
