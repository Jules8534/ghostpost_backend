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
from .views import home_page, post_view, boast_view, roast_view, vote_up, vote_down, up_view, down_view



urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', home_page, name='home'),
    path('addpost/', post_view, name='addpost'),
    path('boasts/', boast_view, name='boasts'),
    path('roasts/', roast_view, name='roasts'),
    path('up/<int:element_id>', vote_up, name="vote_up"),
    path('down/<int:element_id>', vote_down, name="vote_down"),
    path('up/', up_view, name="vote_up"),
    path('down/', down_view, name="vote_down"),



]