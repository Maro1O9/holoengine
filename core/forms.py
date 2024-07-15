from django import forms
from .models import Post, Media

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['text']

class MediaForm(forms.ModelForm):
    class Meta:
        model = Media
        fields = ['media_type', 'file']
