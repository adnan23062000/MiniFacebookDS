from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    body = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={
            'rows': '3',
            'placeholder': 'Say Something...',
            'class': 'md-textarea form-control'
            }))

    class Meta:
        model = Post
        fields = ['body']
