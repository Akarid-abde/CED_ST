from django.shortcuts import render, redirect
import pandas
from django.http import HttpResponse
from .models import Demande, DemandeCED, Professeur
from .forms import *
from django.views.decorators.clickjacking import xframe_options_deny
from django.views.decorators.clickjacking import xframe_options_sameorigin
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages

from django.contrib.auth import login, authenticate  # add this
from django.contrib.auth.forms import AuthenticationForm  # add this


# Create your views here.
def index(request):
    return render(request, 'pages/index.html')


def error_500(request):
    return render(request, '500.html')


def error_404(request, exception):
    return render(request, 'login_error.html', status=404)


def Logout(request):
    return render(request, 'pages/index.html')


def home(request):
    if not request.user.is_authenticated:
        return render(request, 'pages/login_error.html')
    else:
        return render(request, 'pages/demandeST.html')


def home2(request):
    return render(request, 'pages/demandeST.html', {'lf': DemandeForm})


# def page_not_found_view(request, exception):
#     return render(request, '404.html', status=404)

@ xframe_options_sameorigin
def demandeST(request):
    if not request.user.is_authenticated:
        usern = request.user.username
        # print(usern)
        return render(request, 'pages/login_error.html', {"user": usern})
    else:
        if request.method == 'POST':
            dataForm = DemandeForm(request.POST, request.FILES)
            if dataForm.is_valid():
                dataForm.save()
                messages.success(
                    request, f"La demande a été bien envoyer.Merci")
                return redirect('demandeST')
        else:
            # messages.error(request, f"Error")
            dataForm = DemandeForm()
        # nom = request.POST.get('nom')
        # password = request.POST.get('password')
        # data = Login(nom=nom, password=password)
        # data.save()
        return render(request, 'pages/demandeST.html', {'lf': DemandeForm})


def readExcel(request):
    if not request.user.is_authenticated:
        return render(request, 'pages/login_error.html')
    else:
        if request.method == 'POST':
            excel = request.FILES.get('excel')
            df = pandas.read_excel(excel)
            # count = len(df.index)
            count = 2
            for index, row in df.iterrows():
                # print(int(row[0]), end="\n\n")
                # print(row[1], end="\n\n")
                # print(row[2], end="\n\n")
                # print(row[3], end="\n\n")

                data = PROF(
                    DOTI=Professeur(DOTI=int(row[0])),
                    nomComplete=Professeur(nomComplete=row[1]),
                    Grade=Professeur(Grade=row[2]),
                    DEPART=Professeur(DEPART=row[3])
                )

                # print(data)
                # save data
                data.save()
                if index == count - 1:
                    break
        return render(request, 'pages/importExcel.html', {'form': PROF})


@ xframe_options_sameorigin
def DCED(request):
    if not request.user.is_authenticated:
        return render(request, 'pages/login_error.html')
    else:
        if request.method == 'POST':
            dataForm = CEDForm(request.POST)
            if dataForm.is_valid():
                NomPrenom = dataForm.data['NomPrenom']
                Heure = dataForm.data['Heure']

            NomPrenom_H = NomPrenom
            Heure_H = Heure
            DatePropose = request.POST.get('DatePropose')
            # data enter.
            doctorantNom = request.POST.get('doctorantNom')
            doctorantPrenom = request.POST.get('doctorantPrenom')
            doctorantCNE_Masser = request.POST.get('doctorantCNE_Masser')
            doctorantApogee = request.POST.get('doctorantApogee')
            Cv = request.FILES.get('Cv')

            TitreThese = request.POST.get('TitreThese')
            DesciplineThese = request.POST.get('DesciplineThese')
            SpeciliteThses = request.POST.get('SpeciliteThses')
            # IntituleeThese = request.POST.get('IntituleeThese')
            DateInscriptionThese = request.POST.get('DateInscriptionThese')

            Brevet = request.FILES.get('Brevet')
            ChapitreLivre = request.FILES.get('ChapitreLivre')
            DemandeDirecteur = request.FILES.get('DemandeDirecteur')
            DemandeDoctorant = request.FILES.get('DemandeDoctorant')
            RapportDirecteur = request.FILES.get('RapportDirecteur')
            These = request.FILES.get('These')
            lienPub1 = request.POST.get('lienPub1')
            lienPub2 = request.POST.get('lienPub2')
            lienPub3 = request.POST.get('lienPub3')
            lienPub4 = request.POST.get('lienPub4')
            Communication = request.FILES.get('Communication')
            CommunicationOrale = request.FILES.get('CommunicationOrale')
            CommunicationPoster = request.FILES.get('CommunicationPoster')

            NomRapporteur = request.POST.get('NomRapporteur')
            PrenomRapporteur = request.POST.get('PrenomRapporteur')
            EtablisementRapporteur = request.POST.get('EtablisementRapporteur')
            EmailRapporteur = request.POST.get('EmailRapporteur')
            TeleRapporteur = request.POST.get('TeleRapporteur')

            NomRapporteur2 = request.POST.get('NomRapporteur2')
            PrenomRapporteur2 = request.POST.get('PrenomRapporteur2')
            EtablisementRapporteur2 = request.POST.get(
                'EtablisementRapporteur2')
            EmailRapporteur2 = request.POST.get('EmailRapporteur2')
            TeleRapporteur2 = request.POST.get('TeleRapporteur2')

            PrenomRapporteur3 = request.POST.get('PrenomRapporteur3')
            EtablisementRapporteur3 = request.POST.get(
                'EtablisementRapporteur3')
            EmailRapporteur3 = request.POST.get('EmailRapporteur3')
            TeleRapporteur3 = request.POST.get('TeleRapporteur3')

            NomExaminateur = request.POST.get('NomExaminateur')
            PrenomExaminateur = request.POST.get('PrenomExaminateur')
            EtablisementExaminateur = request.POST.get(
                'EtablisementExaminateur')
            EmailExaminateur = request.POST.get('EmailExaminateur')
            TeleExaminateur = request.POST.get('TeleExaminateur')

            NomExaminateur2 = request.POST.get('NomExaminateur2')
            PrenomExaminateur2 = request.POST.get('PrenomExaminateur2')
            EtablisementExaminateur2 = request.POST.get(
                'EtablisementExaminateur2')
            EmailExaminateur2 = request.POST.get('EmailExaminateur2')
            TeleExaminateur2 = request.POST.get('TeleExaminateur2')

            NomPresident = request.POST.get('NomPresident')
            PrenomPresident = request.POST.get('NomPresident')
            EtablisementPresident = request.POST.get('NomPresident')
            EmailPresident = request.POST.get('NomPresident')
            TelePresident = request.POST.get('NomPresident')

            # data enter
            data = DemandeCED(

                NomPrenom=Professeur(id=NomPrenom_H),
                Heure=Heure_H,
                DatePropose=DatePropose,

                doctorantNom=doctorantNom,
                doctorantPrenom=doctorantPrenom,
                doctorantCNE_Masser=doctorantCNE_Masser,
                doctorantApogee=doctorantApogee,
                Cv=Cv,

                TitreThese=TitreThese,
                DesciplineThese=DesciplineThese,
                SpeciliteThses=SpeciliteThses,
                # IntituleeThese=IntituleeThese,
                DateInscriptionThese=DateInscriptionThese,

                Brevet=Brevet,
                ChapitreLivre=ChapitreLivre,
                DemandeDirecteur=DemandeDirecteur,
                DemandeDoctorant=DemandeDoctorant,
                RapportDirecteur=RapportDirecteur,
                These=These,
                lienPub1=lienPub1,
                lienPub2=lienPub2,
                lienPub3=lienPub3,
                lienPub4=lienPub4,
                Communication=Communication,
                CommunicationOrale=CommunicationOrale,
                CommunicationPoster=CommunicationPoster,


                NomRapporteur=NomRapporteur,
                PrenomRapporteur=PrenomRapporteur,
                EtablisementRapporteur=EtablisementRapporteur,
                EmailRapporteur=EmailRapporteur,
                TeleRapporteur=TeleRapporteur,

                NomRapporteur2=NomRapporteur2,
                PrenomRapporteur2=PrenomRapporteur2,
                EtablisementRapporteur2=EtablisementRapporteur2,
                EmailRapporteur2=EmailRapporteur2,
                TeleRapporteur2=TeleRapporteur2,

                PrenomRapporteur3=PrenomRapporteur3,
                EtablisementRapporteur3=EtablisementRapporteur3,
                EmailRapporteur3=EmailRapporteur3,
                TeleRapporteur3=TeleRapporteur3,

                NomExaminateur=NomExaminateur,
                PrenomExaminateur=PrenomExaminateur,
                EtablisementExaminateur=EtablisementExaminateur,
                EmailExaminateur=EmailExaminateur,
                TeleExaminateur=TeleExaminateur,

                NomExaminateur2=NomExaminateur2,
                PrenomExaminateur2=PrenomExaminateur2,
                EtablisementExaminateur2=EtablisementExaminateur2,
                EmailExaminateur2=EmailExaminateur2,
                TeleExaminateur2=TeleExaminateur2,

                NomPresident=NomPresident,
                PrenomPresident=PrenomPresident,
                EtablisementPresident=EtablisementPresident,
                EmailPresident=EmailPresident,
                TelePresident=TelePresident,
            )

           # save data
            data.save()
            messages.success(request, f"La demande a été bien envoyer.Merci")
            return redirect('demandeCED')
        else:
            return render(request, 'pages/demandeCED.html', {'form': CEDForm})


def listerdemande(request):
    return render(request, 'pages/listesDemande.html', {'demande': Demande.objects.all()})


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"New account created: {username}")
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect("/")
        else:
            messages.error(request, "Account creation failed")
            return redirect("register")
    form = NewUserForm()
    return render(request, template_name="pages/register.html", context={"register_form": form})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("index")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="pages/login.html", context={"login_form": form})


def Save2Form(request):
    if request.method == 'POST':
        print(request.POST)

        FormAlbum = AlbumForm(request.POST, prefix="fr1")
        FormMusic = MusicForm(request.POST, prefix="fr2")
        if FormAlbum.is_valid() and FormMusic.is_valid():
            FormMusic.save()
            FormAlbum.save()
            return redirect('demandeST')
    else:
        FormAlbum = AlbumForm(prefix="fr1")
        FormMusic = MusicForm(prefix="fr2")
    return render(request=request, template_name="pages/twoform.html", context={"fr1": AlbumForm, "fr2": MusicForm})
