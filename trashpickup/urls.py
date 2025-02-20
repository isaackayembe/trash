"""
URL configuration for trashpickup project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from trash.views import*
from django.conf.urls.static import static
from trashpickup import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('client',abonne, name='abonne'),
    path('y',index, name='index'),
    path('',main, name='main'),
    path('login',authetification, name='authetification'),
    path('deco',logout_view, name='logout_view'),
    path('delete/<int:client_id>/',delete, name='delete'),
    path('get_clients/', get_clients, name='get_clients'),
    path('valide/<int:id>/',valide, name='valide'),
    path('ajouter/',ajouter, name='ajouter'),
    path('register/', register_client, name='register_client'),
    path('validate/<int:client_id>/', validate_client, name='validate_client'),
    path('recherche',recherche, name='recherche'),
]
