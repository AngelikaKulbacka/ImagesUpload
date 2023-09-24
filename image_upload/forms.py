from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class CustomUserCreationForm(UserCreationForm):
    account_tier = forms.ChoiceField(choices=User.ACCOUNT_TIERS)
