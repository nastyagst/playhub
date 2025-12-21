from django.shortcuts import render
from django.views import generic
from django.contrib.auth import get_user_model
from .models import Game, Developer, Genre

def index(request):
    num_games = Game.objects.count()
    num_developers = Developer.objects.count()
    num_gamers = get_user_model().objects.count()

    context = {
        "num_games": num_games,
        "num_developers": num_developers,
        "num_gamers": num_gamers,
    }

    return render(request, "catalog/index.html", context=context)


class GameListView(generic.ListView):
    model = Game
    paginate_by = 5
    queryset = Game.objects.select_related("developer")