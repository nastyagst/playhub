from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Gamer, Genre, Developer, Game, Comment


@admin.register(Gamer)
class GamerAdmin(UserAdmin):
    list_display = ("username", "email", "first_name", "last_name", "is_staff")
    fieldsets = UserAdmin.fieldsets + (
        ("Additional information", {"fields": ("bio", "avatar")}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Additional information", {"fields": ("bio", "avatar")}),
    )


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ("title", "developer", "release_date")
    search_fields = ("title",)
    list_filter = ("genres", "developer")


admin.site.register(Genre)
admin.site.register(Developer)
admin.site.register(Comment)
