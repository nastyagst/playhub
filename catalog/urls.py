from django.urls import path
from .views import index, GameListView, GameDetailView
from . import views

app_name = "catalog"

urlpatterns = [
    path("", index, name="index"),
    path("games/", GameListView.as_view(), name="game-list"),
    path("games/<int:pk>/", GameDetailView.as_view(), name="game-detail"),
    path("developers/", views.DeveloperListView.as_view(), name="developer-list"),
    path("developers/<int:pk>/", views.DeveloperDetailView.as_view(), name="developer-detail"),
    path('accounts/register/', views.register, name='register'),
]
