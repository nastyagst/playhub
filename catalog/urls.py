from django.urls import path
from .views import index, GameListView, GameDetailView
from . import views

app_name = "catalog"

urlpatterns = [
    path("", index, name="index"),
    path("games/", GameListView.as_view(), name="game-list"),
    path("games/<int:pk>/", GameDetailView.as_view(), name="game-detail"),
    path("games/create/", views.GameCreateView.as_view(), name="game-create"),
    path("games/<int:pk>/update/", views.GameUpdateView.as_view(), name="game-update"),
    path("games/<int:pk>/delete/", views.GameDeleteView.as_view(), name="game-delete"),
    path("developers/", views.DeveloperListView.as_view(), name="developer-list"),
    path("developers/<int:pk>/", views.DeveloperDetailView.as_view(), name="developer-detail"),
    path("games/<int:pk>/comment/", views.CommentCreateView.as_view(), name="comment-create"),
    path('accounts/register/', views.register, name='register'),
]
