# Generated by Django 4.0.4 on 2023-01-24 09:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0017_rename_nom_prenom_professeur_nomcomplete_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='demande',
            name='NomPrenom',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pages.professeur'),
        ),
    ]