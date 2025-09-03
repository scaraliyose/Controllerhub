# storefront/forms.py
from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'title', 'body', 'author_name', 'author_email']
        widgets = {
            'rating': forms.NumberInput(attrs={'min': 1, 'max': 5}),
            'title': forms.TextInput(attrs={'placeholder': 'Short summary'}),
            'body': forms.Textarea(attrs={'rows': 4}),
        }

    def clean(self):
        data = super().clean()
   
        if not self.instance.customer:
            if not data.get('author_name') or not data.get('author_email'):
                raise forms.ValidationError("Please provide your name and email for the review.")
        return data
