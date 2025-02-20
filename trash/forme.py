from django import forms
from django.contrib.auth.models import User
from .models import Client
from .models import ClientTemp



class ClientForm(forms.ModelForm):
    class Meta:
        model = Client 
        fields = ['nom', 'postnom','prenom','sex','num_tel','commune','quartier','avenue','num_reference','type_contrat','statut_paiement',]
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            'postnom': forms.TextInput(attrs={'class': 'form-control'}),
            'prenom': forms.TextInput(attrs={'class': 'form-control'}),
            'sex': forms.Select(attrs={'class': 'form-select'}),
            'num_tel': forms.TextInput(attrs={'class': 'form-control'}),
            'commune': forms.TextInput(attrs={'class': 'form-control'}),
            'quartier': forms.TextInput(attrs={'class': 'form-control'}),
            'avenue': forms.TextInput(attrs={'class': 'form-control'}),
            'num_reference': forms.TextInput(attrs={'class': 'form-control'}),
            'type_contrat': forms.Select(attrs={'class': 'form-select'}),
            'statut_paiement': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


class ClientTempForm(forms.ModelForm):
    class Meta:
        model = ClientTemp
        fields = ['nom', 'postnom','prenom','sex','num_tel','commune','quartier','avenue','num_reference','type_contrat','statut_paiement',]
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            'postnom': forms.TextInput(attrs={'class': 'form-control'}),
            'prenom': forms.TextInput(attrs={'class': 'form-control'}),
            'sex': forms.Select(attrs={'class': 'form-select'}),
            'num_tel': forms.TextInput(attrs={'class': 'form-control'}),
            'commune': forms.TextInput(attrs={'class': 'form-control'}),
            'quartier': forms.TextInput(attrs={'class': 'form-control'}),
            'avenue': forms.TextInput(attrs={'class': 'form-control'}),
            'num_reference': forms.TextInput(attrs={'class': 'form-control'}),
            'type_contrat': forms.Select(attrs={'class': 'form-select'}),
            'statut_paiement': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
