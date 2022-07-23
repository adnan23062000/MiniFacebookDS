from django import forms
from django.contrib.auth.models import User

class studentForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    class Meta():
        model=User
        fields=['first_name','last_name','username','email','password']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'})
        }
        help_texts = {
            'username': None,
        }
