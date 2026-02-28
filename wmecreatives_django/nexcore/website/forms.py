"""
NexCore website forms.
"""
from django import forms
from .models import ContactMessage

SERVICE_CHOICES = [
    ('', 'Select a service…'),
    ('Web Development', 'Web Development'),
    ('CRM Software Solutions', 'CRM Software Solutions'),
    ('ERP Systems', 'ERP Systems'),
    ('Odoo Implementation', 'Odoo Implementation'),
    ('ERPNext Implementation', 'ERPNext Implementation'),
    ('WhatsApp Chatbot Development', 'WhatsApp Chatbot Development'),
    ('Other / Multiple Services', 'Other / Multiple Services'),
]


class ContactForm(forms.ModelForm):
    service = forms.ChoiceField(
        choices=SERVICE_CHOICES,
        required=False,
        widget=forms.Select()
    )

    class Meta:
        model = ContactMessage
        fields = ['first_name', 'last_name', 'email', 'service', 'message']
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'John'}),
            'last_name':  forms.TextInput(attrs={'placeholder': 'Doe'}),
            'email':      forms.EmailInput(attrs={'placeholder': 'john@company.com'}),
            'message':    forms.Textarea(attrs={
                'rows': 5,
                'placeholder': 'Describe your project, goals, and timeline…'
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            existing = field.widget.attrs.get('class', '')
            field.widget.attrs['class'] = (existing + ' form-input').strip()
