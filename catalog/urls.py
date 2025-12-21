from django.urls import path
from .views import index, GameListView

app_name = "catalog"

urlpatterns = [
    path("", index, name="index"),
    path("games/", GameListView.as_view(), name="game-list"),
]
