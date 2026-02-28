"""
NexCore admin configuration.
All content is fully editable through the Django admin panel.
"""
from django.contrib import admin
from django.utils.html import format_html
from .models import Service, Stat, TeamMember, CompanyValue, ContactMessage, SiteSettings


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['number_display', 'title', 'icon_key', 'is_featured', 'is_active']
    list_editable = ['is_featured', 'is_active']
    list_filter = ['is_active', 'is_featured', 'icon_key']
    prepopulated_fields = {'slug': ('title',)}
    ordering = ['number']
    fieldsets = (
        ('Basic Info', {'fields': ('number', 'title', 'slug', 'icon_key')}),
        ('Content', {'fields': ('short_description', 'full_description', 'tags')}),
        ('Display', {'fields': ('is_featured', 'is_active')}),
    )


@admin.register(Stat)
class StatAdmin(admin.ModelAdmin):
    list_display = ['value', 'label', 'order']
    list_editable = ['order']
    ordering = ['order']


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ['name', 'role', 'order', 'is_active']
    list_editable = ['order', 'is_active']


@admin.register(CompanyValue)
class CompanyValueAdmin(admin.ModelAdmin):
    list_display = ['icon', 'title', 'order']
    list_editable = ['order']
    ordering = ['order']


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'service', 'status', 'submitted_at']
    list_filter = ['status', 'service', 'submitted_at']
    list_editable = ['status']
    readonly_fields = ['first_name', 'last_name', 'email', 'service', 'message',
                       'submitted_at', 'ip_address']
    search_fields = ['first_name', 'last_name', 'email', 'message']
    ordering = ['-submitted_at']

    def has_add_permission(self, request):
        return False  # Only created via contact form


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Hero Section', {
            'fields': ('hero_badge_text', 'hero_headline_line1', 'hero_headline_accent', 'hero_subheadline')
        }),
        ('About Section', {
            'fields': ('about_lead',)
        }),
        ('Contact Info', {
            'fields': ('office_address', 'email_primary', 'email_support', 'phone', 'phone_hours')
        }),
        ('Footer & Social', {
            'fields': ('footer_tagline', 'linkedin_url', 'twitter_url', 'github_url')
        }),
    )

    def has_add_permission(self, request):
        # Only one settings instance allowed
        return not SiteSettings.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False
