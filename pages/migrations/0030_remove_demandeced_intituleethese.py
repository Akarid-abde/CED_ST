# Generated by Django 4.0.4 on 2023-02-20 21:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0029_demandeced_cv_demandeced_heure_demandeced_nomprenom'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='demandeced',
            name='IntituleeThese',
        ),
    ]
