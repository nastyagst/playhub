from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth import get_user_model
from .models import Game, Developer, Genre
from .forms import GameSearchForm, GamerCreationForm
from django.contrib.auth import login



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
    context_object_name = "game_list"
    template_name = "catalog/game_list.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(GameListView, self).get_context_data(**kwargs)
        title = self.request.GET.get("title", "")
        context["search_form"] = GameSearchForm(initial={"title": title})
        return context

    def get_queryset(self):
        queryset = Game.objects.select_related("developer")
        form = GameSearchForm(self.request.GET)

        if form.is_valid():
            return queryset.filter(title__icontains=form.cleaned_data["title"])

        return queryset


class GameDetailView(generic.DetailView):
    model = Game


def register(request):
    if request.method != "POST":
        form = GamerCreationForm()
    else:
        form = GamerCreationForm(data=request.POST)

    if form.is_valid():
        new_user = form.save()
        login(request, new_user)
        return redirect("catalog:index")

    context = {"form": form}
    return render(request, "registration/register.html", context)


class DeveloperListView(generic.ListView):
    model = Developer
    paginate_by = 5
    context_object_name = "developer_list"
    template_name = "catalog/developer_list.html"


class DeveloperDetailView(generic.DetailView):
    model = Developer
