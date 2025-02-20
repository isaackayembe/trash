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




# Create your views here.
def base(request):
    return render(request, 'base.html')
def envoyer_notification_nouveau_client(client_email):
    subject = 'Nouveau Client Enregistré'
    message = 'Un nouveau client a été enregistré sur le site.'
    recipient_list = ['isaackayembe44@gmail.com']  # Vous pouvez aussi mettre votre adresse ici
    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,
        recipient_list,
        fail_silently=False,
    )

def index(request):
    if request.method == 'POST':
        forme = ClientForm(request.POST, request.FILES)
        if forme.is_valid():
            client = forme.save()  # Enregistre le client
            # Supposons que client a un champ 'email'
            envoyer_notification_nouveau_client(client.email)  # Envoie l'e-mail
            return redirect('index')  # Redirigez vers la liste des agents
    else:
        forme = ClientForm()
    return render(request, 'index.html', {'forme': forme})

def abonne(request):

    clients = Client.objects.all()  # Récupérer tous les clients
    return render(request, 'client.html', {'clients': clients})
def recherche(request):
    query = request.GET.get('q', '')
    clients = Client.objects.all()  # Renommé à 'clients' pour éviter la confusion

    if query:
        clients = clients.filter(nom__icontains=query) | clients.filter(prenom__icontains=query) | clients.filter(commune__icontains=query)

    return render(request, 'client.html', {'clients': clients, 'query': query})  # Passe 'clients' au template

def delete(request, client_id):
    client = get_object_or_404(Client, id=client_id)
    
    if request.method == 'POST':
        client.delete()  # Utilisez client.delete() pour supprimer l'objet
        return redirect('abonne')  # Redirection vers la liste des clients

    return render(request, 'client.html', {'client': client}) 

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

def get_clients(request):
    client = Client.objects.all().values()  # Récupérer tous les clients
    return JsonResponse(list(client), safe=False)
def valide(request, id):  # Ajoute 'id' comme argument
    client = get_object_or_404(Client, id=id)  # Utilise 'id' pour récupérer le client
    return render(request, 'valide.html', {'client': client})
def ajouter(request):
    return render(request, 'ajouter.html')


def envoyer_notification_nouveau_client(client_email):
    subject = 'Nouveau Client Enregistré'
    message = 'Un nouveau client a été enregistré sur le site.'
    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,
        [client_email],  # Vous pouvez changer cela pour envoyer à votre adresse
        fail_silently=False,
    )





def register_client(request):
    if request.method == 'POST':
        form = ClientTempForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirige vers une page de confirmation ou d'accueil
    else:
        form = ClientTempForm()
    return render(request, 'register_client.html', {'form': form})

def validate_client(request, client_id):
    client_temp = ClientTemp.objects.get(id=client_id)

    if request.method == 'POST':
        if 'validate' in request.POST:
            # Sauvegarder dans la table principale
            Client.objects.create(**client_temp.__dict__)
            client_temp.delete()  # Supprimer de la table temporaire
            return redirect('validation_success')
        elif 'refuse' in request.POST:
            client_temp.delete()  # Supprimer de la table temporaire
            return redirect('refusal_success')

    return render(request, 'validate_client.html', {'client_temp': client_temp})