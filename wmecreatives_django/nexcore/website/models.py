"""
NexCore website models.
All site content is managed through the Django admin.
"""
from django.db import models
from django.utils import timezone


class Service(models.Model):
    """A service offered by NexCore."""
    ICON_CHOICES = [
        ('web', 'Web Development'),
        ('crm', 'CRM'),
        ('erp', 'ERP'),
        ('odoo', 'Odoo'),
        ('erpnext', 'ERPNext'),
        ('whatsapp', 'WhatsApp'),
        ('custom', 'Custom'),
    ]

    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    number = models.PositiveSmallIntegerField(help_text='Display order (01, 02…)')
    icon_key = models.CharField(max_length=20, choices=ICON_CHOICES, default='custom')
    short_description = models.TextField(help_text='Shown on the service card')
    full_description = models.TextField(blank=True, help_text='Shown on detail page')
    tags = models.CharField(max_length=200, help_text='Comma-separated tag labels')
    is_featured = models.BooleanField(default=False, help_text='Highlights the card (green accent)')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['number']

    def __str__(self):
        return self.title

    def tags_list(self):
        return [t.strip() for t in self.tags.split(',') if t.strip()]

    def number_display(self):
        return str(self.number).zfill(2)


class Stat(models.Model):
    """Hero section statistics."""
    value = models.CharField(max_length=20, help_text='e.g. 200+')
    label = models.CharField(max_length=60, help_text='e.g. Projects Delivered')
    order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f'{self.value} — {self.label}'


class TeamMember(models.Model):
    """About section team members."""
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    bio = models.TextField(blank=True)
    order = models.PositiveSmallIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f'{self.name} — {self.role}'


class CompanyValue(models.Model):
    """About section — company values / pillars."""
    icon = models.CharField(max_length=10, default='◈')
    title = models.CharField(max_length=100)
    description = models.TextField()
    order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title


class ContactMessage(models.Model):
    """Stores contact form submissions."""
    STATUS_CHOICES = [
        ('new', 'New'),
        ('read', 'Read'),
        ('replied', 'Replied'),
        ('archived', 'Archived'),
    ]

    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    email = models.EmailField()
    service = models.CharField(max_length=100, blank=True)
    message = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')
    submitted_at = models.DateTimeField(default=timezone.now)
    ip_address = models.GenericIPAddressField(null=True, blank=True)

    class Meta:
        ordering = ['-submitted_at']

    def __str__(self):
        return f'{self.first_name} {self.last_name} <{self.email}> — {self.submitted_at:%Y-%m-%d}'

    def full_name(self):
        return f'{self.first_name} {self.last_name}'


class SiteSettings(models.Model):
    """Singleton model for editable site-wide content."""
    # Hero
    hero_badge_text = models.CharField(max_length=100, default='Technology & Business Solutions')
    hero_headline_line1 = models.CharField(max_length=80, default='We Engineer')
    hero_headline_accent = models.CharField(max_length=80, default='Digital Futures')
    hero_subheadline = models.TextField(
        default='From custom web platforms to enterprise ERP systems — NexCore delivers '
                'end-to-end technology solutions that transform how businesses operate, grow, and compete.'
    )

    # About
    about_lead = models.TextField(
        default='NexCore Technologies is a full-service digital transformation partner for '
                'businesses ready to scale. Since 2012, we\'ve helped companies across industries '
                'modernize their operations through smart technology choices.'
    )

    # Contact info
    office_address = models.TextField(default='Innovation Hub, 4th Floor\n123 Tech Boulevard, Suite 400\nSan Francisco, CA 94105')
    email_primary = models.EmailField(default='hello@nexcore.tech')
    email_support = models.EmailField(default='support@nexcore.tech')
    phone = models.CharField(max_length=30, default='+1 (415) 555-0192')
    phone_hours = models.CharField(max_length=60, default='Mon – Fri, 9am – 6pm PST')

    # Footer
    footer_tagline = models.CharField(max_length=160, default='Engineering digital futures for ambitious businesses worldwide.')
    linkedin_url = models.URLField(blank=True, default='#')
    twitter_url = models.URLField(blank=True, default='#')
    github_url = models.URLField(blank=True, default='#')

    class Meta:
        verbose_name = 'Site Settings'
        verbose_name_plural = 'Site Settings'

    def __str__(self):
        return 'Site Settings'

    def save(self, *args, **kwargs):
        # Enforce singleton
        self.pk = 1
        super().save(*args, **kwargs)

    @classmethod
    def get(cls):
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj
