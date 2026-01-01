from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import get_user_model
from .models import Game, Developer, Genre, Comment
from .forms import GameSearchForm, GamerCreationForm, GameForm, CommentForm
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin



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


class GameListView(LoginRequiredMixin, generic.ListView):
    model = Game
    paginate_by = 11
    context_object_name = "game_list"
    template_name = "catalog/game_list.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(GameListView, self).get_context_data(**kwargs)
        context["search_form"] = GameSearchForm(self.request.GET)
        return context

    def get_queryset(self):
        queryset = Game.objects.select_related("developer")
        form = GameSearchForm(self.request.GET)

        if form.is_valid():
            if form.cleaned_data["title"]:
                queryset = queryset.filter(title__icontains=form.cleaned_data["title"])

            if form.cleaned_data["genres"]:
                queryset = queryset.filter(genres__in=form.cleaned_data["genres"]).distinct()

            if form.cleaned_data["developers"]:
                queryset = queryset.filter(developer__in=form.cleaned_data["developers"])

        return queryset


class GameDetailView(LoginRequiredMixin, generic.DetailView):
    model = Game

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comment_form"] = CommentForm
        return context


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


class DeveloperListView(LoginRequiredMixin, generic.ListView):
    model = Developer
    paginate_by = 8
    context_object_name = "developer_list"
    template_name = "catalog/developer_list.html"


class DeveloperDetailView(LoginRequiredMixin, generic.DetailView):
    model = Developer


class GameCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Game
    form_class = GameForm
    template_name = "catalog/game_edit.html"

    def test_func(self):
        return self.request.user.is_staff


class GameUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Game
    form_class = GameForm
    template_name = "catalog/game_edit.html"

    def test_func(self):
        return self.request.user.is_staff

class GameDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Game
    success_url = reverse_lazy("catalog:game-list")
    template_name = "catalog/game_confirm_delete.html"

    def test_func(self):
        return self.request.user.is_staff


class CommentCreateView(LoginRequiredMixin, generic.CreateView):
    model = Comment
    form_class = CommentForm
    template_name = "catalog/game_detail.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        game_id = self.kwargs["pk"]
        form.instance.game = get_object_or_404(Game, pk=game_id)

        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("catalog:game-detail", kwargs={"pk": self.kwargs["pk"]})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["game"] = get_object_or_404(Game, pk=self.kwargs["pk"])
        context["comment_form"] = context["form"]
        return context
