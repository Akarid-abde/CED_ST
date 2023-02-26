from django.db import models
from datetime import datetime

DEPARTEMENT = (
    ('1', 'Maths'),
    ('2', 'Physique'),
    ('3', 'Biologie'),
    ('4', 'Chimie'),
    ('5', 'Géologie'),
    ('6', 'Informatique'),
    ('7', 'LC'),
)


class Professeur(models.Model):
    DOTI = models.CharField(max_length=50)
    nomComplete = models.CharField(max_length=255)
    Grade = models.CharField(max_length=255, default="")
    DEPART = models.CharField(
        max_length=255, null=False, choices=DEPARTEMENT, default="----",
        verbose_name='DEPARTEMENT')

    def __str__(self) -> str:
        return self.DOTI + '   '+self.nomComplete


CHOICES_Heur = (
    ('9:00AM', '9:00AM'),
    ('9:30AM', '9:30AM'),
    ('10:00AM', '10:00AM'),
    ('10:30AM', '10:30AM'),
    ('11:00AM', '11:00AM'),
    ('11:30AM', '11:30AM'),
    ('12:00PM', '12:00PM'),
    ('12:30PM', '12:30PM'),
    ('1:00PM', '1:00PM'),
    ('1:30PM', '1:30PM'),
    ('2:00PM', '2:00PM'),
    ('2:30PM', '2:30PM'),
    ('3:00PM', '3:00PM'),
    ('3:30PM', '3:30PM'),
    ('4:00PM', '4:00PM'),
    ('4:30PM', '4:30PM'),
    ('5:00PM', '5:00PM'),
    ('5:30PM', '5:30PM'),
)


class Demande(models.Model):
    NomPrenom = models.ForeignKey(
        Professeur, null=True, on_delete=models.CASCADE)
    DOTI = models.IntegerField(null=False, default="",
                               verbose_name='DOTI')
    Nom = models.CharField(max_length=255, null=False, default="",
                           verbose_name='Pr. Nom')
    Prenom = models.CharField(max_length=255, null=False, default="",
                              verbose_name='Pr. Prenom')

    Email = models.EmailField(max_length=255, null=False, default="",
                              verbose_name='Email')
    Tele = models.CharField(max_length=255, null=False, default="",
                            verbose_name='Téléphone')
    Heure = models.CharField(
        max_length=255, null=False, choices=CHOICES_Heur, default="",
        verbose_name='Choisir une heur')

    Doctorant = models.CharField(max_length=255, null=False, default="",
                                 verbose_name='Mr. Doctorant')

    # DateProposee = models.DateField(default=datetime.date, blank=True,
    #                                 verbose_name='Date Propose')

    Cv = models.FileField(upload_to='cvs/%y/%m/%d',
                          verbose_name='Cv', default="cvs/22/11/24/cv.pdf")
    ThesePiece = models.FileField(upload_to='theses/%y/%m/%d',
                                  verbose_name='These', default="theses/22/11/24/these.pdf")
    AvisSoutnance = models.ImageField(upload_to='photos/%y/%m/%d',
                                      verbose_name='Image Avis de soutnance', default="photos/22/11/24/cv.png")

    Created = models.DateTimeField(
        default=datetime.now, verbose_name='Date de demande')
    Jury = models.TextField(null=False, default="",
                            verbose_name='Jury NomPrenom || Etablissement || Role')

    def __str__(self) -> str:
        return self.Nom


class DemandeCED(models.Model):

    #  demande de monsieur

    NomPrenom = models.ForeignKey(
        Professeur, null=True, on_delete=models.CASCADE)

    DatePropose = models.DateField(blank=True, null=True,
                                   verbose_name='Proposition de date de soutenance ')

    Heure = models.CharField(
        max_length=255, null=False, choices=CHOICES_Heur, default="",
        verbose_name='Choisir une heur')

    # information Doctorant

    doctorantNom = models.CharField(max_length=255, null=False, default="",
                                    verbose_name='Nom.Doctorant')
    doctorantPrenom = models.CharField(max_length=255, null=False, default="",
                                       verbose_name='Prenom.Doctorant')
    doctorantCNE_Masser = models.CharField(max_length=255, null=False, default="",
                                           verbose_name='CNE/MASSAR')
    doctorantApogee = models.IntegerField(
        null=False, default=0, verbose_name='Appogee')

    Cv = models.FileField(upload_to='cvs/%y/%m/%d',
                          verbose_name='Cv', default="cvs/22/11/24/cv.pdf")

    # information sur la thése
    TitreThese = models.CharField(max_length=255, null=False, default="",
                                  verbose_name='Titre de thèse')
    DesciplineThese = models.CharField(max_length=255, null=False, default="",
                                       verbose_name='discipline de thèse ')
    SpeciliteThses = models.CharField(max_length=255, null=False, default="",
                                      verbose_name='spécialité de thèse')
    # IntituleeThese = models.CharField(max_length=255, null=False, default="",
    #                                   verbose_name='intitulé de thèse')
    DateInscriptionThese = models.DateField(blank=True, null=True,
                                            verbose_name='date de 1ére inscription dans la thèse')

    # demande de soutenance
    Brevet = models.FileField(upload_to='Brevet/%y/%m/%d',
                                        verbose_name='Brevet', default="Brevet/22/11/24/Brevet.pdf")

    ChapitreLivre = models.FileField(upload_to='ChapitreLivre/%y/%m/%d',
                                     verbose_name='ChapitreLivre', default="ChapitreLivre/22/11/24/Brevet.pdf")

    DemandeDirecteur = models.FileField(upload_to='DemandeDirecteur/%y/%m/%d',
                                        verbose_name='DemandeDirecteur', default="DemandeDirecteur/22/11/24/DemandeDirecteur.pdf")

    DemandeDoctorant = models.FileField(upload_to='DemandeDoctorant/%y/%m/%d',
                                        verbose_name='DemandeDoctorant', default="DemandeDoctorant/22/11/24/DemandeDoctorant.pdf")

    RapportDirecteur = models.FileField(upload_to='RapportDirecteur/%y/%m/%d',
                                        verbose_name='RapportDirecteur', default="RapportDirecteur/22/11/24/RapportDirecteur.pdf")

    These = models.FileField(upload_to='These/%y/%m/%d',
                             verbose_name='These', default="These/22/11/24/These.pdf")

    lienPub1 = models.CharField(max_length=255, null=False, default="",
                                verbose_name='Lien Publication 1')

    lienPub2 = models.CharField(max_length=255, null=False, default="",
                                verbose_name='Lien Publication 2')

    lienPub3 = models.CharField(max_length=255, null=True, default="",
                                verbose_name='Lien Publication 3')

    lienPub4 = models.CharField(max_length=255, null=True, default="",
                                verbose_name='Lien Publication 4')

    Communication = models.FileField(upload_to='Communication/%y/%m/%d',
                                     verbose_name='Communication', default="Communication/22/11/24/Communication.pdf")
    CommunicationOrale = models.FileField(upload_to='CommunicationOrale/%y/%m/%d',
                                          verbose_name='CommunicationOrale', default="CommunicationOrale/22/11/24/CommunicationOrale.pdf")
    CommunicationPoster = models.ImageField(upload_to='CommunicationPoster/%y/%m/%d',
                                            verbose_name='CommunicationPoster', default="CommunicationPoster/22/11/24/CommunicationPoster.png")

    # demande de soutenance
    NomRapporteur = models.CharField(
        max_length=255, null=False, default="", verbose_name='Nom Rapporteur1')

    PrenomRapporteur = models.CharField(max_length=255, null=False, default="",
                                        verbose_name='Prenom Rapporteur1')
    EtablisementRapporteur = models.CharField(max_length=255, null=False, default="",
                                              verbose_name='Etablisement Rapporteur1')
    EmailRapporteur = models.CharField(max_length=255, null=False, default="",
                                       verbose_name='Email Rapporteur1')
    TeleRapporteur = models.CharField(max_length=255, null=False, default="",
                                      verbose_name='Tele Rapporteur1')

    NomRapporteur2 = models.CharField(
        max_length=255, null=False, default="", verbose_name='Nom Rapporteur2')
    PrenomRapporteur2 = models.CharField(
        max_length=255, null=False, default="", verbose_name='Prenom Rapporteur2')
    EtablisementRapporteur2 = models.CharField(
        max_length=255, null=False, default="", verbose_name='Etablissement Rapporteur2')
    EmailRapporteur2 = models.CharField(
        max_length=255, null=False, default="", verbose_name='Email Rapporteur2')
    TeleRapporteur2 = models.CharField(
        max_length=255, null=False, default="", verbose_name='Tele Rapporteur2')

    NomRapporteur3 = models.CharField(
        max_length=255, null=False, default="", verbose_name='Nom Rapporteur3')
    PrenomRapporteur3 = models.CharField(
        max_length=255, null=False, default="", verbose_name='Prenom Rapporteur3')
    EtablisementRapporteur3 = models.CharField(
        max_length=255, null=False, default="", verbose_name='Etablissement Rapporteur3')
    EmailRapporteur3 = models.CharField(
        max_length=255, null=False, default="", verbose_name='Email Rapporteurs3')
    TeleRapporteur3 = models.CharField(
        max_length=255, null=False, default="", verbose_name='Tele Rapporteur3')

    NomExaminateur = models.CharField(
        max_length=255, null=False, default="", verbose_name='Nom Examinateur')
    PrenomExaminateur = models.CharField(
        max_length=255, null=False, default="", verbose_name='Prenom Examinateur')
    EtablisementExaminateur = models.CharField(
        max_length=255, null=False, default="", verbose_name='Etablissement')
    EmailExaminateur = models.CharField(
        max_length=255, null=False, default="", verbose_name='Email Examinateur')
    TeleExaminateur = models.CharField(
        max_length=255, null=False, default="", verbose_name='Tele Examinateur')

    NomExaminateur2 = models.CharField(
        max_length=255, null=False, default="", verbose_name='Nom Examinateur2')
    PrenomExaminateur2 = models.CharField(
        max_length=255, null=False, default="", verbose_name='Prenom Examinateur2')
    EtablisementExaminateur2 = models.CharField(
        max_length=255, null=False, default="", verbose_name='Etablissement Examinateur2')
    EmailExaminateur2 = models.CharField(
        max_length=255, null=False, default="", verbose_name='Email Examinateur2')
    TeleExaminateur2 = models.CharField(
        max_length=255, null=False, default="", verbose_name='Tele Examinateur2')

    NomPresident = models.CharField(
        max_length=255, null=False, default="", verbose_name='Nom Président')
    PrenomPresident = models.CharField(
        max_length=255, null=False, default="", verbose_name='Prenom Président')
    EtablisementPresident = models.CharField(
        max_length=255, null=False, default="", verbose_name='Etablissement Président')
    EmailPresident = models.CharField(
        max_length=255, null=False, default="", verbose_name='Email Président')
    TelePresident = models.CharField(
        max_length=255, null=False, default="", verbose_name='Tele Président')

    def __str__(self) -> str:
        return f"{self.doctorantNom}, {self.DateInscriptionThese}"
