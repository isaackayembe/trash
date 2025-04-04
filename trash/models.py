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
        ('2', '15$'),
        ('3', '20$'),
        ('4', '30$'),
        ('5', '40$'),
        ('6', '45$'),
        ('7', '100$'),
        ('8', '150$'),
        ('9', '200$'),
        ('10', '250$'),
        ('11', '300$'),
        ('12', '350$'),
        ('13', '400$'),
        ('14', '450$'),
        ('15', '500$'),
        ('16', '550$'),
        ('17', '600$'),
        ('18', '650$'),
        ('19', '700$'),
        ('20', '800$'),
        ('21', '1000$'),
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
    type_contrat = models.CharField(max_length=2, choices=TYPE_CONTRAT_CHOICES)
    date_enregistrement = models.DateTimeField(auto_now_add=True)
    statut_paiement = models.BooleanField(default=False)  # True = Payé, False = Non payé
    date_paiement = models.DateTimeField(default=timezone.now)
    is_approved = models.BooleanField(default=False)  # Nouveau champ pour l'approbation
    
    def get_montant(self):
        if self.type_contrat == '1':
            return 10.00
        elif self.type_contrat == '2':
            return 15.00
        elif self.type_contrat == '3':
            return 20.00
        elif self.type_contrat == '4':
            return 30.00
        elif self.type_contrat == '5':
            return 40.00
        elif self.type_contrat == '6':
            return 45.00
        elif self.type_contrat == '7':
            return 100.00
        elif self.type_contrat == '8':
            return 150.00  
        elif self.type_contrat == '9':
            return 200.00 
        elif self.type_contrat == '10':
            return 250.00 
        elif self.type_contrat == '11':
            return 300.00 
        elif self.type_contrat == '12':
            return 350.00 
        elif self.type_contrat == '13':
            return 400.00 
        elif self.type_contrat == '14':
            return 450.00 
        elif self.type_contrat == '15':
            return 500.00 
        elif self.type_contrat == '16':
            return 550.00 
        elif self.type_contrat == '17':
            return 600.00 
        elif self.type_contrat == '18':
            return 650.00 
        elif self.type_contrat == '19':
            return 700.00
        elif self.type_contrat == '20':
            return 800.00 
        elif self.type_contrat == '21':
            return 1000.00   # Modifiez ce montant selon votre besoin
       


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