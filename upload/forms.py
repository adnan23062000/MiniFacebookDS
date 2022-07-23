from django import forms
from .models import Material

class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = ('title', 'pdf')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
        }
