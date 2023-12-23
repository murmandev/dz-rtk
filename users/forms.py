from django import forms

from django.contrib.auth.models import User
from .models import Account
from django.forms import TextInput, EmailInput, FileInput
from django.contrib.auth.forms import UserChangeForm


class UserUpdateForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
        widgets = {'username': TextInput({'class': 'textinput form-control',
                                          'placeholder': 'username'}),
                   'email': EmailInput({'class': 'textinput form-control',
                                        'placeholder': 'email'}),
                   'first_name': TextInput({'class': 'textinput form-control',
                                            'placeholder': 'First name'}),
                   'last_name': TextInput({'class': 'textinput form-control',
                                           'placeholder': 'Last name'}),
                   }


class AccountUpdateForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['nickname', 'account_image']
        widgets = {'nickname': TextInput({'class': 'textinput form-control',
                                       'placeholder': 'НикНейм', 'required': False}),
                   'account_image': FileInput({'class': 'form-control',
                                               'placeholder': 'image'}),
                   }


