from django import forms
from .models import Keyword
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class KeywordForm(forms.ModelForm):
    class Meta:
        model = Keyword
        fields = ['text']

class UserRegistrationForm(UserCreationForm):
  email = forms.EmailField()
  class Meta:
    model = User
    fields = ('username', 'email', 'password1', 'password2')