from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Gamer, Game, Comment


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


class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = "__all__"
        widgets = {
            "release_date": forms.DateInput(attrs={"type": "date", "class": "form-control"})
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["text"]
        widgets = {
            "text": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 3,
                "placeholder": "Write your comment here"
            })
        }
