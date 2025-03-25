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
# urls.py
# urls.py
from django.urls import path
from django.urls import path

urlpatterns = [
    path('force/', admin.site.urls),
    path('a',admin_dashboard, name='admin_dashboard'),
    path('client',abonne, name='abonne'),
    path('y',index, name='index'),
    path('',main, name='main'),
    path('login',authetification, name='authetification'),
    path('deco',logout_view, name='logout_view'),
    path('delete/<int:client_id>/',delete, name='delete'),
    path('valide/<int:id>/',valide, name='valide'),
    path('approve/<int:client_id>/', approve_client, name='approve_client'),
    path('recherche',recherche, name='recherche'),
    path('pending_clients/', pending_clients, name='pending_clients'),
    path('mes',message, name='message'),
    path('renouveler_abonnement/<int:client_id>/', renouveler_abonnement, name='renouveler_abonnement'),
    path('verifier_abonnements/', verifier_abonnements, name='verifier_abonnements'),
    path('reabon',reabonnement, name='reabonnement'),
    path('contact',contact, name='contact'),
    path('detail',detail, name='detail'),
    path('trans/<int:id>/',trans, name='trans'),
    
]

contact
