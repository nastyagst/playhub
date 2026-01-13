from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path(
        'accounts/logout/',
        auth_views.LogoutView.as_view(template_name='registration/logged_out.html'),
        name='logout'
    ),
    path("accounts/", include("django.contrib.auth.urls")),
    path("", include("catalog.urls")),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
