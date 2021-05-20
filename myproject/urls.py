from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/', include('app.urls')),
    path('base-auth/', include('rest_framework.urls')),
    path('auth/', include('djoser.urls')),
    path('auth-token/', include('djoser.urls.authtoken')),
]
