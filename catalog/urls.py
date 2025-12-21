from django.urls import path
from .views import index, GameListView, GameDetailView

app_name = "catalog"

urlpatterns = [
    path("", index, name="index"),
    path("games/", GameListView.as_view(), name="game-list"),
    path("games/<int:pk>/", GameDetailView.as_view(), name="game-detail"),
]
