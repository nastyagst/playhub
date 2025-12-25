from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path(
        'accounts/logout/',
        auth_views.LogoutView.as_view(template_name='registration/logged_out.html'),
        name='logout'
    ),
    path("accounts/", include("django.contrib.auth.urls")),
    path("", include("catalog.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
