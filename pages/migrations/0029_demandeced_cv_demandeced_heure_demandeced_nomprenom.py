# Generated by Django 4.0.4 on 2023-02-12 15:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0028_demandeced_nomexaminateur2_demandeced_nomrapporteur_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='demandeced',
            name='Cv',
            field=models.FileField(default='cvs/22/11/24/cv.pdf', upload_to='cvs/%y/%m/%d', verbose_name='Cv'),
        ),
        migrations.AddField(
            model_name='demandeced',
            name='Heure',
            field=models.CharField(choices=[('9:00AM', '9:00AM'), ('9:30AM', '9:30AM'), ('10:00AM', '10:00AM'), ('10:30AM', '10:30AM'), ('11:00AM', '11:00AM'), ('11:30AM', '11:30AM'), ('12:00PM', '12:00PM'), ('12:30PM', '12:30PM'), ('1:00PM', '1:00PM'), ('1:30PM', '1:30PM'), ('2:00PM', '2:00PM'), ('2:30PM', '2:30PM'), ('3:00PM', '3:00PM'), ('3:30PM', '3:30PM'), ('4:00PM', '4:00PM'), ('4:30PM', '4:30PM'), ('5:00PM', '5:00PM'), ('5:30PM', '5:30PM')], default='', max_length=255, verbose_name='Choisir une heur'),
        ),
        migrations.AddField(
            model_name='demandeced',
            name='NomPrenom',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pages.professeur'),
        ),
    ]
