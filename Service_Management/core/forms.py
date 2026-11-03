from django import forms
from .models import Services

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Services
        fields = [
            "service_name",
            "description",
            "price",
            "duration",
            "status"
        ]

        widgets = {
            "description": forms.Textarea(attrs={
                "rows": 3,
                "cols": 40
            })
        }