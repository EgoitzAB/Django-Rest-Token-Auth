"""
URL configuration for recetas project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.urls import re_path as url
from api import views
from rest_framework import routers

router = routers.DefaultRouter()

router.register('recetas', views.RecetaViewSet, basename='receta')

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('api/v1/auth/', include('dj_rest_auth.urls')),
    path('api/v1/auth/registration/', include('dj_rest_auth.registration.urls')),
    path('api/v1/favorita/', views.MarcarRecetaFavorita.as_view()),
    path('api/v1/favoritas/', views.ListarPeliculasFavoritas.as_view()),
    path('admin/', admin.site.urls),
]
