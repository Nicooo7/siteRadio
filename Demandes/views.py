# coding: utf-8

from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse, Http404
from django.template import loader
#from django.core.exceptions import ObjectDoesNotExist

from .models import *
from django.contrib.auth.models import*
from django.contrib.auth import *

from django.template.response import *

#from unidecode import unidecode
from django.utils.safestring import mark_safe
from.forms import *
from django.utils import timezone


# Create your views here.







def accueil(request):




    def reinitialiserExamens():
        examens = Examen.objects.filter()
        for examen in examens:
            examen.delete()
#reinitialiserExamens()

    #creation des utilisateurs
    def creerUtilisateurs():

        user = User.objects.create_user('Chamard', 'leila@radiologue.com', 'radiologue')
        user.save()
        user = User.objects.create_user('Vignoli','radiologue@hotmail.com', 'radiologue')
        user.save()
        user = User.objects.create_user('Rigal', 'radiologue@hotmail.com', 'radiologue')
        user.save()
        user = User.objects.create_user('Plateau', 'radiologue@hotmail.com', 'radiologue')
        user.save()
        user = User.objects.create_user('Olivier', 'radiologue@hotmail.com', 'radiologue')
        user.save()


    #creerUtilisateurs()

   # user = User.objects.create_user('Bossard', 'radiologue@hotmail.com', 'radiologue')
   # user.save()

    return render(request, 'accueil.html', {"titrePage":"Acceuil"})

def connexion(request):

    error = False

    if request.method == 'POST':
        form = AuthentificationForm(request.POST)
        if form.is_valid():
            username = request.POST["nom"]
            password = request.POST["mot_de_passe"]
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return render (request, 'accueil.html')
            else:
                error = True
        else:
            form = AuthentificationForm()


    form = AuthentificationForm()

    titre = "demandes d'examen : page d'authentification"

    return render(request, 'authentification.html', {'form': form})

def gererMesExamens(request):

    class Exam:

        liste= []

        def __init__(self, machine, region, intitule, validationRequise = "non", realise="non", commentaire ="aucun"):
            self.machine = machine
            self.region = region
            self.intitule = intitule
            self.validationRequise = validationRequise
            self.realise = realise
            self.commentaire = commentaire
            if machine == "geste":
                """self.commentaire = self.commentaire + " ; prévoir 48 H de repos et venir accompagné"
                print("commentaire ajouté")"""
            Exam.liste.append(self)

#IRM:

    #tete et cou
    Exam("IRM", "tete et cou","encephale")
    Exam("IRM", "tete et cou","spectro multimodal")
    Exam("IRM", "tete et cou","angio TSA")
    Exam("IRM", "tete et cou","hypophyse")
    Exam("IRM", "tete et cou","CAI")
    Exam("IRM", "tete et cou","sinus")
    Exam("IRM", "tete et cou","rocher(cholesteatome)")
    Exam("IRM", "tete et cou","parotide")
    Exam("IRM", "tete et cou","cavum")
    Exam("IRM", "tete et cou","oro-pharynx et ou cavite orale")
    Exam("IRM", "tete et cou","larynx")
    Exam("IRM", "tete et cou","ATM")

    #moelle
    Exam("IRM", "moelle","moelle")
    Exam("IRM", "moelle","plexus brachial")
    Exam("IRM", "moelle","plexus lombo-sacré")

    #abdomen et pelvis
    Exam("IRM", "abdomen et pelvis","foie")
    Exam("IRM", "abdomen et pelvis","pancreas")
    Exam("IRM", "abdomen et pelvis","bili-IRM")
    Exam("IRM", "abdomen et pelvis","entéro-IRM")
    Exam("IRM", "abdomen et pelvis","rénal")
    Exam("IRM", "abdomen et pelvis","angio rénal ou MI")
    Exam("IRM", "abdomen et pelvis","pelvienne (gynéco)")
    Exam("IRM", "abdomen et pelvis","déféco-IRM")
    Exam("IRM", "abdomen et pelvis","Prostate")
    Exam("IRM", "abdomen et pelvis","rectum")
    Exam("IRM", "abdomen et pelvis","périnéale")


    #ostéo-articulaire
    Exam("IRM", "osteo","rachis cervical/dorsal/lombaire")
    Exam("IRM", "osteo","Partie molle (lipome, jambe, avant bras…)")
    Exam("IRM", "osteo","sacro-iliaque")
    Exam("IRM", "osteo","bassin/hanche")
    Exam("IRM", "osteo","genou")
    Exam("IRM", "osteo","cheville")
    Exam("IRM", "osteo","pied")
    Exam("IRM", "osteo","épaule")
    Exam("IRM", "osteo","coude")
    Exam("IRM", "osteo","poignet")
    Exam("IRM", "osteo","main")
    Exam("IRM", "osteo","arthro scanner épaule")

#Scanner:
    #tete et cou
    Exam("scanner", "tete et cou","encephale")
    Exam("scanner", "tete et cou","angio TSA")
    Exam("scanner", "tete et cou","sinus")
    Exam("scanner", "tete et cou","rocher")
    Exam("scanner", "tete et cou","cervical ORL parties molles")
    Exam("scanner", "tete et cou","ATM")
    Exam("scanner", "tete et cou","dacryoscanner")


    #osteo:
    Exam("scanner", "osteo","epaule")
    Exam("scanner", "osteo","genou")
    Exam("scanner", "osteo","poignet")
    Exam("scanner", "osteo","coude")
    Exam("scanner", "osteo","cheville")
    Exam("scanner", "osteo","hanche")


    #autres
    Exam("scanner", "autre","rachis")
    Exam("scanner", "autre","thorax")
    Exam("scanner", "autre","coroscanner")
    Exam("scanner", "autre","score calcique")
    Exam("scanner", "autre","angio scanner aorte et MI")

#Echographie

    #général
    Exam("echographie", "general","abdominal")
    Exam("echographie", "general","abdomino-pelvienne")
    Exam("echographie", "general","thyroide")
    Exam("echographie", "general","parties molles")
    Exam("echographie", "general","pelvienne endo")
    Exam("echographie", "general","cervicale")
    Exam("echographie", "general","parties molles indéterminée")

    #doppler
    Exam("echographie", "doppler","artères MI/MS")
    Exam("echographie", "doppler","veines MI/MS")
    Exam("echographie", "doppler","rénale")
    Exam("echographie", "doppler","greffon")
    Exam("echographie", "doppler","TSA")

    #pédiatrie
    Exam("echographie", "pédiatrie","hanches nourrisson")
    Exam("echographie", "pédiatrie","moelle")
    Exam("echographie", "pédiatrie","ETF")
    Exam("echographie", "pédiatrie","pleurale")

    #Osteo
    Exam("echographie", "osteo","épaule")
    Exam("echographie", "osteo","coude")
    Exam("echographie", "osteo","poignet")
    Exam("echographie", "osteo","main")
    Exam("echographie", "osteo","hanche")
    Exam("echographie", "osteo","genou")
    Exam("echographie", "osteo","cheville")
    Exam("echographie", "osteo","pied")

#Gestes:
    #sous scanner
    Exam("geste", "sous scanner"," biopsie pulmonaire")
    Exam("geste", "sous scanner"," biopsie osseuse")
    Exam("geste", "sous scanner"," drainage")
    Exam("geste", "sous scanner"," infiltration C1-C2", commentaire = "(= Névralgie d’Arnold) avec du CONTRASTE et de l’HYDROCORTANCYL ")
    Exam("geste", "sous scanner"," infiltration épidurale lombaire", commentaire ="Avec du CONTRASTE et de l’HYDROCORTANCYL")
    Exam("geste", "sous scanner"," infiltrations sacro-iliaques")
    Exam("geste", "sous scanner"," infiltrations articulaires postérieures lombaires", commentaire ="articulaires postérieures (=zygapophysaires).Avec du CONTRASTE et de l’HYDROCORTANCYL")

    #sous échographie
    Exam("geste", "sous echo"," cytoponction thyroidienne")
    Exam("geste", "sous echo"," cytoponction ganglionnaire")
    Exam("geste", "sous echo"," infiltration epaule", commentaire ="Xylo, Diprostène", )
    Exam("geste", "sous echo"," infiltration genou", commentaire ="Xylo, Diprostène.")
    Exam("geste", "sous echo"," infiltration cheville", commentaire ="Xylo, Diprostène.")
    Exam("geste", "sous echo"," infiltration poignet", commentaire ="Xylo, Diprostène.")
    Exam("geste", "sous echo"," infiltration main", commentaire ="Xylo, Diprostène.")
    Exam("geste", "sous echo"," infiltration hanche", commentaire ="Xylo, Diprostène.")
    Exam("geste", "sous echo"," biopsie foie")
    Exam("geste", "sous echo"," biopsie rein")
    Exam("geste", "sous echo"," drainage collection")
    Exam("geste", "sous echo"," biopsie rein")

    #sous radio
    Exam("geste", "sous radio"," TOGD")
    Exam("geste", "sous radio"," cystographie")
    Exam("geste", "sous radio"," hysterographie")
    Exam("geste", "sous radio"," transit du grêle")
    Exam("geste", "sous radio"," infiltration acromio-clav", commentaire ="Contraste, Xylo, Diporstène.")
    Exam("geste", "sous radio"," infiltration sous-acromiale", commentaire ="Contraste, Xylo, Diporstène.")
    Exam("geste", "sous radio"," infiltration poignet", commentaire ="Contraste, Xylo, Diporstène.")
    Exam("geste", "sous radio"," infiltration genou", commentaire ="Contraste, Xylo, Diporstène.")
    Exam("geste", "sous radio"," infiltration cheville", commentaire ="Contraste, Xylo, Diporstène.")
    Exam("geste", "sous radio"," articulaire postérieure", commentaire ="Contraste, Xylo, Diporstène.")



    listeExamens = Exam.liste
    MesExamensRealises = Examen.objects.filter(realisant = request.user)
    tousLesExamens = Examen.objects.all()
    for e1 in listeExamens :
        for e2 in MesExamensRealises:
            if e1.machine == e2.machine:
                if e1.region == e2.region:
                    if e1.intitule == e2.intitule:
                        e1.realise = "oui"

    for e1 in listeExamens :
        for e3 in tousLesExamens:
            if e1.machine == e3.machine:
                if e1.region == e3.region:
                    if e1.intitule == e3.intitule:
                        e1.validationRequise = e3.validationRequise

    """
    examens = Examen.objects.all()
    for examen in examens:
        for e in Exam.liste:
            if examen.machine == e.machine:
                if examen.region == e.region:
                    if examen.intitule == e.intitule:
                        examen.commentaire = e.commentaire
                        examen.save()
                        print(examen.commentaire)
    """

    return render(request, 'gererMesExamens.html', {"listeExamens" : listeExamens, "titrePage":"gerer mes examens"})


def quiFaitQuoi(request):

    examens = Examen.objects.all()

    for examen in examens:
        print(examen.commentaire)
        personnes = ""
        for personne in examen.realisant.all():
            personnes = personnes +  personne.username +  ", "
        examen.personnes = personnes



    return render(request, 'quiFaitQuoi.html', {"examens" : examens, "titrePage":"quiFaitQuoi?"})

def enregistrerMesExamens(request):
    examensRealises = request.GET["examensRealises"]
    examensNonRealises = request.GET["examensNonRealises"]

    listeDesExamensRealises = examensRealises.replace("%20", " ").split("XXX")
    listeDesExamensNonRealises = examensNonRealises.replace("%20", " ").split("XXX")

    def reinitialiserExamens():
        examens = Examen.objects.filter()
        for examen in examens:
            examen.delete()




    for examen in listeDesExamensRealises[1:]:
        examen = examen.split("/")
        #print("examen réalisé:", examen)
        e = Examen.objects.get_or_create(machine = examen[0], region=examen[1], intitule = examen[2])
        e = e[0]
        e.save()
        e.realisant.add(request.user)
        e.validationRequise = examen[3]
        e.commentaire = examen[4]
        e.save()
        #print(e.realisant.all())

    for examen in listeDesExamensNonRealises[1:]:
        examen = examen.split("/")
        #print("examen non réalisé", examen)
        e = Examen.objects.get_or_create(machine = examen[0], region=examen[1], intitule = examen[2])
        e = e[0]
        e.commentaire = examen[4]
        e.validationRequise = examen[3]
        e.save()
        e.realisant.remove(request.user)
        e.save()





    return render(request, "accueil.html")





