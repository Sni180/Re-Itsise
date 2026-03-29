from django import forms
from map.models import Fault # We reuse the model from the map app

class FaultReportForm(forms.ModelForm):
    class Meta:
        model = Fault
        fields = ['category', 'description', 'location_address', 'image']
        widgets = {
            'description': forms.Textarea(attrs={'placeholder': 'Describe the issue...'}),
            'location_address': forms.TextInput(attrs={'placeholder': 'Street name or GPS...'}),
        }