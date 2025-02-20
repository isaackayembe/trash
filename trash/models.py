from django.db import models
from django.utils import timezone

# Create your models here.
class Client(models.Model):
    SEX_CHOICES = [
        ('M', 'Masculin'),
        ('F', 'Féminin'),
        ('O', 'Autre'),
    ]

    TYPE_CONTRAT_CHOICES = [
        ('1', '10$'),
        ('2', '20$'),
        ('3', 'Extra +'),
    ]

    nom = models.CharField(max_length=100)
    postnom = models.CharField(max_length=100, null=False, blank=True)
    prenom = models.CharField(max_length=100, null=False, blank=True)
    sex = models.CharField(max_length=1, choices=SEX_CHOICES)
    num_tel = models.CharField(max_length=100, null=False, blank=True)
    email = models.CharField(max_length=100, null=False, blank=True)
    commune = models.CharField(max_length=100, null=False, blank=True)
    quartier = models.CharField(max_length=100, null=False, blank=True)
    avenue = models.CharField(max_length=100, null=False, blank=True)
    num_reference= models.CharField(max_length=100, null=False, blank=True)
    type_contrat = models.CharField(max_length=1, choices=TYPE_CONTRAT_CHOICES)
    date_enregistrement = models.DateTimeField(auto_now_add=True)
    statut_paiement = models.BooleanField(default=False)  # True = Payé, False = Non payé
    date_paiement = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return f"{self.nom} {self.statut_paiement} {self.commune} {self.type_contrat}"
   
   
class ClientTemp(models.Model):
    SEX_CHOICES = [
        ('M', 'Masculin'),
        ('F', 'Féminin'),
        ('O', 'Autre'),
    ]

    TYPE_CONTRAT_CHOICES = [
        ('1', '10$'),
        ('2', '20$'),
        ('3', 'Extra +'),
    ]

    nom = models.CharField(max_length=100)
    postnom = models.CharField(max_length=100, null=False, blank=True)
    prenom = models.CharField(max_length=100, null=False, blank=True)
    sex = models.CharField(max_length=1, choices=SEX_CHOICES)
    num_tel = models.CharField(max_length=100, null=False, blank=True)
    email = models.CharField(max_length=100, null=False, blank=True)
    commune = models.CharField(max_length=100, null=False, blank=True)
    quartier = models.CharField(max_length=100, null=False, blank=True)
    avenue = models.CharField(max_length=100, null=False, blank=True)
    num_reference= models.CharField(max_length=100, null=False, blank=True)
    type_contrat = models.CharField(max_length=1, choices=TYPE_CONTRAT_CHOICES)
    date_enregistrement = models.DateTimeField(auto_now_add=True)
    statut_paiement = models.BooleanField(default=False)  # True = Payé, False = Non payé
    date_paiement = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return f"{self.nom} {self.statut_paiement} {self.commune} {self.type_contrat}"