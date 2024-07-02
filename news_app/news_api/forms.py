from django import forms
from .models import Keyword
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class KeywordForm(forms.ModelForm):
    """
    Form for creating and updating Keyword instances.

    Fields:
        text (CharField): The text of the keyword.
    """
    class Meta:
        model = Keyword
        fields = ['text']

class UserRegistrationForm(UserCreationForm):
    """
      Form for registering a new user with username, email, and password.

      Fields:
        username (CharField): The username of the user.
        email (EmailField): The email address of the user.
        password1 (CharField): The user's password.
        password2 (CharField): Confirmation of the user's password.
    """
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
