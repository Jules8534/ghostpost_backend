"""django_ghostpost URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from .models import Post
from . import views
# import urlpatterns as ghostpost_urls
from ghostpost.helpers import private_url_maker



urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.index, name="home"),
    path("ghost/<int:pk>/", views.ghost_public_detail, name="ghost_public_detail"),
    path("ghost/<str:private_url>/", views.ghost_private_detail, name="views.ghost_private_detail"),
    path('up/<int:pk>', views.vote_up, name="vote_up"),
    path('down/<int:pk>', views.vote_down, name="vote_down"),
    # path('up/<int:pk>', views.up_view, name="vote_up"),
    # path('down/<int:pk', views.down_view, name="vote_down"),
    path("delete/<str:private_url>/", views.delete_post, name="delete")

]