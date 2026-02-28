"""
NexCore website views.
"""
import json
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_protect
from django.utils.decorators import method_decorator

from .models import Service, Stat, CompanyValue, SiteSettings
from .forms import ContactForm


def home(request):
    """Main single-page website view."""
    settings = SiteSettings.get()
    services = Service.objects.filter(is_active=True)
    stats = Stat.objects.all()
    values = CompanyValue.objects.all()
    form = ContactForm()

    context = {
        'settings': settings,
        'services': services,
        'stats': stats,
        'values': values,
        'form': form,
    }
    return render(request, 'website/home.html', context)


def service_detail(request, slug):
    """Detail page for a single service."""
    service = get_object_or_404(Service, slug=slug, is_active=True)
    other_services = Service.objects.filter(is_active=True).exclude(slug=slug)[:3]
    context = {
        'service': service,
        'other_services': other_services,
        'settings': SiteSettings.get(),
    }
    return render(request, 'website/service_detail.html', context)


@require_POST
@csrf_protect
def contact_submit(request):
    """
    AJAX endpoint for the contact form.
    Returns JSON so the frontend can handle success/error without a page reload.
    """
    form = ContactForm(request.POST)
    if form.is_valid():
        msg = form.save(commit=False)
        # Capture IP
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            msg.ip_address = x_forwarded_for.split(',')[0].strip()
        else:
            msg.ip_address = request.META.get('REMOTE_ADDR')
        msg.save()
        return JsonResponse({'success': True, 'message': "Thanks! We'll be in touch within 24 hours."})
    else:
        errors = {field: error.get_json_data() for field, error in form.errors.items()}
        return JsonResponse({'success': False, 'errors': errors}, status=400)
