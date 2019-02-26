from django import forms
from django.forms import ModelForm
from .models import *


class DemandeForm(ModelForm):
    class Meta:
        model = Demande
        fields = ['nom','prenom', 'indication','degre_urgence','type_examen','injection']
        widgets = {
       'degre_urgence':forms.Select(attrs={'cols': 80, 'rows': 20, "class": "browser-default grey lighten-2" }),
       'type_examen':forms.Select(attrs={'cols': 80, 'rows': 20, "class": "browser-default grey lighten-2" }),
       'injection':forms.Select(attrs={'cols': 80, 'rows': 20, "class": "browser-default grey lighten-2" }), 
       'indication': forms.Textarea(attrs={'cols': 80, 'rows': 20, "class": "browser-default grey lighten-2" }),  
       'nom': forms.Textarea(attrs={'cols': 80, 'rows': 20, "class": "browser-default grey lighten-2" }), 
       'prenom': forms.Textarea(attrs={'cols': 80, 'rows': 20, "class": "browser-default grey lighten-2" }), 
        }
        
class RadiologueForm(ModelForm):
    class Meta:
        model = Radiologue
        fields = '__all__'
        widgets = {

        'prenom':forms.TextInput(attrs={'cols': 20, 'rows': 20, "class": "grey lighten-2"}),
        'nom':forms.TextInput(attrs={'cols': 20, 'rows': 20, "class": "grey lighten-2"}),
       'statut':forms.Select(attrs={'cols': 20, 'rows': 20, "class": "browser-default grey lighten-2"}),
       "tempsDeTravail" : forms.Select(attrs={'cols': 80, 'rows': 20, "class": "browser-default grey lighten-2" }),
       #'indisponibilites': forms.HiddenInput(),
        'vacationFixe': forms.TextInput(attrs={'cols': 20, 'rows': 20, "class": "grey lighten-2"}),
        'jourSansTravail':  forms.TextInput(attrs={'cols': 20, 'rows': 20, "class": "grey lighten-2"}),  
        }


        labels = {
            'tempsDeTravail': ('temps de travail'),
        }
    

class UtilisateurForm(forms.Form):
  nom = forms.CharField(max_length=100)
  prenom = forms.CharField(max_length=100)
  mot_de_passe = forms.CharField(max_length=100)
  mail = forms.EmailField(max_length=254)


class AuthentificationForm(forms.Form):
        nom = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'cols': 10, 'rows': 20, "class": "grey lighten-2"})) 
        mot_de_passe = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'cols': 20, 'rows': 20, "class": "grey lighten-2"}))
  



