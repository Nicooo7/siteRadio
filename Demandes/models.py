#coding: utf-8
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


#__________________________ Planning ______________________________


class Radiologue(models.Model):
    
    
    listeDesStatuts=(
        ("praticien clinicien","praticien clinicien"),
        ("praticien hospitalier", "praticien hospitalier"),
        ("interne","interne")
    )
    listeDesTempsDeTravail=(
        ("1/2 temps","1/2 temps"),
         ("3/4 temps", "3/4 temps"),
        ("temps complet","temps complet")
    )
    
    prenom=models.CharField(max_length=30, null=True)
    nom=models.CharField(max_length=30,null=True)
    indisponibilites = models.CharField(max_length=1000, null=True )
    statut=models.CharField(
        max_length=30,
        choices=listeDesStatuts,
        null=True
    )
    tempsDeTravail = models.CharField(
        max_length=30,
        choices=listeDesTempsDeTravail,
        null=True
    )
    vacationFixe =  models.CharField(max_length=1000, null=True)
    jourSansTravail =  models.CharField(max_length=30, null=True) 
    


#__________________________demandes ______________________________



class Createur(models.Model):
    utilisateur = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    def __str__(self):
        return self.utilisateur.username

class Validant(models.Model):
    utilisateur = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.utilisateur.username


class Demande(models.Model):
   
    degre_urgence_choix = (
        ('H24', 'H24'),
        ('immédiat', 'immédiat'),
        ('48H', '48H'),
        ('72H', '72H'),
        ('1_semaine', '1_semaine')
    )
    
    type_examen_choix = (
        ('scanner cerebral', 'scanner cerebral'),
        ('scanner AP', 'scanner AP'),
        ('scanner TAP', 'scanner TAP'),
        ('angioscanner pulmonaire', 'angioscanner pulmonaire'),
        ('uroscanner', 'uroscanner'),
        ('scanner Thoracique', 'scanner thoracique'),
    )
    injection_choix = (
        ('oui', 'oui'),
        ('non', 'non'),
        ('à discuter', 'à discuter')
    )
    realisation_choix =(
        ('oui', 'oui'),
        ('non', 'non'),
    )

    validation_choix=(
        ("accepter", "accepter"),
        ("refuser", "refuser"),
        ("accepter sous condition", "accepter sous condition"),
        ("demander un rappel", "demander un rappel")
        )
    
    
    prenom = models.CharField(max_length=30)
    nom = models.CharField(max_length=30)
    indication = models.CharField(max_length=300, null=True)
    degre_urgence = models.CharField(
        max_length=10,
        choices=degre_urgence_choix)
    type_examen= models.CharField(
        max_length=30,
        choices=type_examen_choix)
    injection = models.CharField(
        max_length=30,
        choices=injection_choix)
    realisation = models.CharField(
        max_length=30, 
        choices=realisation_choix, null=True, default="non")
    validation_choix= models.CharField(
        max_length=30, 
        choices=validation_choix, null=True)
    suppression = models.CharField(
        max_length=10,
        choices=realisation_choix,null=True, default="non")
    heure= models.DateTimeField(null = True)
    createur = models.ForeignKey(Createur, null=True, on_delete=models.CASCADE)
    validant = models.ForeignKey(Validant, null=True, on_delete=models.CASCADE)
    commentaires =  models.CharField(max_length=10000, null=True)


class Examen(models.Model):

    machine= models.CharField(
        max_length=10000,
        null=True,
        default = ""
        )
    region= models.CharField(
        max_length=10000,
        null=True,
        default = ""
        )

    intitule=models.CharField(
        max_length=50,
        )

    validationRequise = models.CharField(max_length=3, null =True
        )

    realisant = models.ManyToManyField(User)

    commentaire =  models.CharField(max_length=10000, null=True)

    def __str__(self):
        return(self.machine + " " + self.region + " " + self.intitule)



class Profile (models.Model):

    listeDesStatuts=(
            ("radiologue", "radiologue"),
            ("prescripteur", "prescripteur"),
            ("secretaire", "secretaire"),
        )

    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)
    mail = models.EmailField(max_length = 254, null = True)
    statut = models.CharField(
        max_length=30,
        choices=listeDesStatuts,
        null=True
            )

    examens = models.ManyToManyField(Examen)
        


    def __str__(self):
        return "profile de {0}".format(self.utilisateur)



    
    
