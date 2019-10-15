from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import users


class userForm(forms.ModelForm):
    class Meta:
        model = users
        fields = ('name', 'email', 'mobile_no')
