from django import forms
from .models import Letter


class LetterPost(forms.ModelForm):
    class Meta:
        model = Letter
        fields = [
            'text',
        ]
