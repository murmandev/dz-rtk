from django import forms

from .models import Article
from django.forms import TextInput, FileInput, Textarea



class ArticleUpdateForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content', 'image']
        widgets = {'title': TextInput({'class': 'textinput form-control',
                                       'placeholder': 'НикНейм'}),
                    'content': Textarea({'class': 'textinput form-control',
                                       'placeholder': 'НикНейм'}),                                       
                    'image': FileInput({'class': 'form-control',
                                               'placeholder': 'image'}),
                   }


