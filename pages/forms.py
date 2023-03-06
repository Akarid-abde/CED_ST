from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CEDForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CEDForm, self).__init__(*args, **kwargs)

    class Meta:
        model = DemandeCED
        fields = ("NomPrenom", "Heure")


class PROF(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PROF, self).__init__(*args, **kwargs)

    class Meta:
        model = Professeur
        fields = '__all__'


class DemandeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(DemandeForm, self).__init__(*args, **kwargs)
        self.fields["Created"].disabled = True
        self.fields["Jury"].widget = forms.Textarea(
            attrs={'placeholder': 'Pr.Nom Prenom || Etablissement || Role \nPr.Ahmed Ahmed || FS Tetouan || examinateur'})
        self.fields["Tele"].widget = forms.TextInput(
            attrs={'placeholder': '+2126xxxxxxxx'})
        self.fields["Email"].widget = forms.EmailInput(
            attrs={'placeholder': 'YourEmail@gmail.com'})
        # self.fields["DateProposee"].widget = forms.DateTimeInput(attrs={
        #     'class': 'form-control datetimepicker-input',
        # })
        for field_name in self.fields:
            field = self.fields.get(field_name)
            if field:
                if type(field.widget) in (forms.TextInput, forms.IntegerField):
                    field.widget = forms.TextInput(
                        attrs={'placeholder': field.label})

    class Meta:
        model = Demande
        fields = '__all__'
        # fields =  ("DOTI", "Nom", "Prenom", "Heure","DateProposee")


class PofForm(forms.ModelForm):
    class Meta:
        model = Professeur
        # fields = ['nom']
        fields = '__all__'

# Create your forms here.


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


# class AlbumForm(forms.ModelForm):
#     class Meta:
#         model = Album
#         fields = '__all__'


# class MusicForm(forms.ModelForm):
#     class Meta:
#         model = Musician
#         fields = '__all__'
