from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Gamer


class GameSearchForm(forms.Form):
    title = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by game title..."})
    )


class GamerCreationForm(UserCreationForm):
    class Meta:
        model = Gamer
        fields = ("username", "email")
