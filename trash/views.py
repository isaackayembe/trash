from django.shortcuts import render, redirect, get_object_or_404
from .forme import ClientForm  # Assurez-vous que le nom est correct
from .models import Client  # Utilisez 'Client' s'il s'agit d'une classe
from django.utils import timezone
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect
from .models import Client
from django.http import JsonResponse
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .forme import ClientForm  # Assurez-vous d'importer votre formulaire
from django.shortcuts import render, redirect
from .forme import ClientTempForm
from .models import ClientTemp, Client
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .forme import statistiques
from django.utils import timezone
from datetime import timedelta
from django.contrib.auth.models import User
from django.shortcuts import render






# Create your views here.
@login_required
def admin_dashboard(request):
    # Récupérer les clients approuvés
    clients_approuves = Client.objects.filter(is_approved=True)

    # Statistiques des clients
    total_clients = clients_approuves.count()
    reabonne_count = clients_approuves.filter(statut_paiement=True).count()
    non_reabonne_count = total_clients - reabonne_count

    # Montant total des contrats pour les clients approuvés
    total_montant = sum(client.get_montant() for client in clients_approuves)

    # Montant total des clients réabonnés
    total_montant_reabonne = sum(client.get_montant() for client in clients_approuves.filter(statut_paiement=True))

    # Vérifier s'il y a des clients en attente d'approbation
    clients_en_attente = Client.objects.filter(is_approved=False).exists()

    # Récupérer les utilisateurs
    users = User.objects.all()  # Récupère tous les utilisateurs

    context = {
        'total_clients': total_clients,
        'reabonne_count': reabonne_count,
        'non_reabonne_count': non_reabonne_count,
        'total_montant': total_montant,
        'total_montant_reabonne': total_montant_reabonne,
        'clients_en_attente': clients_en_attente,
        'users': users,  # Ajoutez les utilisateurs au contexte
    }
    return render(request, 'profil.html', context)

def base(request):
    return render(request, 'base.html')


def index(request):
    if request.method == 'POST':
        forme = ClientForm(request.POST, request.FILES)
        if forme.is_valid():
            client = forme.save()  # Enregistre le clien
            return redirect('message')  # Redirigez vers la liste des agents
    else:
        forme = ClientForm()
    return render(request, 'index.html', {'forme': forme})

def abonne(request):
    # Récupérer uniquement les clients approuvés
    clients = Client.objects.filter(is_approved=True)
    return render(request, 'client.html', {'clients': clients})

from django.shortcuts import render
from .models import Client

def recherche(request):
    query = request.GET.get('q', '')  # Obtenir la requête de recherche
    clients = []  # Initialiser la liste des clients

    if query:  # Vérifiez si une recherche a été effectuée
        # Filtrer les résultats en fonction de la recherche
        clients = Client.objects.filter(
            is_approved=True  # Garder uniquement les clients approuvés
        ).filter(
            num_tel__icontains=query
        ) | Client.objects.filter(
            is_approved=True
        ).filter(
            nom__icontains=query
        ) | Client.objects.filter(
            is_approved=True
        ).filter(
            commune__icontains=query
        )
    # Aucune recherche effectuée, clients sera vide

    return render(request, 'client.html', {'clients': clients, 'query': query})# Passe 'clients' au template

def delete(request, client_id):
    client = get_object_or_404(Client, id=client_id)
    
    if request.method == 'POST':
        client.delete()  # Utilisez client.delete() pour supprimer l'objet
        return redirect('abonne')  # Redirection vers la liste des clients

    return render(request, 'client.html', {'client': client}) 
def renouveler_abonnement(request, client_id):
    # Récupérer le client par son ID
    client = get_object_or_404(Client, id=client_id)
    
    # Mettre à jour le statut et la date de réabonnement
    client.statut_paiement = True
    client.date_paiement = timezone.now()  # Mettez à jour avec la date actuelle
    client.save()

    # Rediriger vers la page appropriée après le renouvellement
    return redirect('abonne')  # Ou une autre page si nécessaire
def verifier_abonnements(request):
    clients = Client.objects.all()
    for client in clients:
        expiration_date = client.date_paiement + timedelta(days=30)  # Supposons un abonnement de 30 jours
        if timezone.now() > expiration_date:
            client.statut_paiement = False  # Mettre à jour le statut à non payé
            client.save()

    return redirect('admin_dashboard')  # Redirigez vers le tableau de bord ou une autre page


def main(request):
    # Récupérer la date actuelle
    date_actuelle = timezone.now()
    # Récupérer les clients qui ont payé cet abonnement
    clients = Client.objects.filter(date_paiement__month=date_actuelle.month, 
                                    date_paiement__year=date_actuelle.year)

    # Filtrer pour que les clients n'apparaissent pas après le 15
    if date_actuelle.day > 15:
        clients = clients.none()  # Ou d'autres logiques selon votre besoin

    return render(request, 'main.html', {'clients': clients})

def authetification(request):  # Correction de la faute de frappe dans le nom de la fonction
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('abonne')  # Redirigez vers la page d'accueil ou une autre page
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})  # Correction de l'indentation

    return render(request, 'login.html')  # Correction du nom du template
def logout_view(request):
    logout(request)
    messages.success(request, "Vous avez été déconnecté avec succès.")
    return redirect('authetification')

    return JsonResponse(list(client), safe=False)
def valide(request, id):  # Ajoute 'id' comme argument
    client = get_object_or_404(Client, id=id)  # Utilise 'id' pour récupérer le client
    return render(request, 'valide.html', {'client': client})
   

def approve_client(request, client_id):
    # Récupérer le client avec l'ID donné
    client = get_object_or_404(Client, id=client_id)
    
    # Approuver le client
    client.is_approved = True
    client.save()
    
    # Rediriger vers le tableau de bord ou une autre vue appropriée
    return redirect('pending_clients') 
    
def pending_clients(request):
    # Récupérer les clients non approuvés
    clients = Client.objects.filter(is_approved=False)
    return render(request, 'pending_clients.html', {'clients': clients})

def message(request):
    return render(request, 'message.html')

def reabonnement(request):
    query = request.GET.get('q', '')  # Obtenir la requête de recherche
    clients = []  # Initialiser la liste des clients

    if query:  # Vérifiez si une recherche a été effectuée
        # Filtrer les résultats en fonction de la recherche
        clients = Client.objects.filter(
            is_approved=True  # Garder uniquement les clients approuvés
        ).filter(
            num_tel__icontains=query
        ) | Client.objects.filter(
            is_approved=True
        ).filter(
            nom__icontains=query
        ) | Client.objects.filter(
            is_approved=True
        ).filter(
            commune__icontains=query
        )
    # Aucune recherche effectuée, clients sera vide

    return render(request, 'reabon.html', {'clients': clients, 'query': query})

def contact(request):
 return render(request,'contact.html')
 
def detail (request):
    return render(request,'detail.html')

def trans (request, id):  # Ajoute 'id' comme argument
    client = get_object_or_404(Client, id=id) 
    return render(request,'trans.html', {'client': client})

