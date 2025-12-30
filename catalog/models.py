from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.urls import reverse

class Gamer(AbstractUser):
    bio = models.TextField(blank=True, verbose_name="About me")
    avatar = models.ImageField(upload_to="avatars/", blank=True, null=True)

    class Meta:
        verbose_name = "gamer"
        verbose_name_plural = "gamers"

    def __str__(self):
        return self.username


class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Developer(models.Model):
    name = models.CharField(max_length=255, unique=True)
    country = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="developers/", blank=True, null=True)

    def __str__(self):
        return self.name


class Game(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    release_date = models.DateField()
    image = models.ImageField(upload_to="games/", blank=True, null=True)

    developer = models.ForeignKey(Developer, on_delete=models.CASCADE, related_name="games")
    genres = models.ManyToManyField(Genre, related_name="games")
    gamers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="library", blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("catalog:game-detail", args=[str(self.id)])


class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name="comments")
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
