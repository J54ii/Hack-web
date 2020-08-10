from django import forms
from .models import post


class PostCreateForm(forms.ModelForm):
    title = forms.CharField(label='عنوان التدوينة')
    content = forms.CharField(label='نص التدوينة', widget=forms.Textarea)

    class Meta:
        model = post
        fields = ['title', 'content']