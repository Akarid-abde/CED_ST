# Generated by Django 4.0.4 on 2023-02-05 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0023_album_demandeced_musician'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='demandeced',
            name='Nom',
        ),
        migrations.AddField(
            model_name='demandeced',
            name='doctorantApogee',
            field=models.IntegerField(default=0, verbose_name='Appogee'),
        ),
        migrations.AddField(
            model_name='demandeced',
            name='doctorantCNE_Masser',
            field=models.CharField(default='', max_length=255, verbose_name='CNE/MASSAR'),
        ),
        migrations.AddField(
            model_name='demandeced',
            name='doctorantNom',
            field=models.CharField(default='', max_length=255, verbose_name='Nom.Doctorant'),
        ),
        migrations.AddField(
            model_name='demandeced',
            name='doctorantPrenom',
            field=models.CharField(default='', max_length=255, verbose_name='Prenom.Doctorant'),
        ),
    ]
