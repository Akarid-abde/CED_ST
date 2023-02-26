# Generated by Django 4.0.4 on 2023-01-23 21:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0013_remove_demande_created_remove_demande_dateproposee_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='demande',
            name='Created',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='Date de demande'),
        ),
        migrations.AddField(
            model_name='demande',
            name='Heure',
            field=models.CharField(choices=[('1', '9:00AM'), ('2', '9:30AM'), ('3', '10:00AM'), ('4', '10:30AM'), ('5', '11:00AM'), ('6', '11:30AM'), ('7', '12:00PM'), ('8', '12:30PM'), ('9', '1:00PM'), ('10', '1:30PM'), ('11', '2:00PM'), ('12', '2:30PM'), ('13', '3:00PM'), ('14', '3:30PM'), ('15', '4:00PM'), ('16', '4:30PM'), ('17', '5:00PM'), ('18', '5:30PM')], default='', max_length=255, verbose_name='Choisir une heur'),
        ),
        migrations.AddField(
            model_name='demande',
            name='Jury',
            field=models.TextField(default='', verbose_name='Les membre de jury'),
        ),
        migrations.AlterField(
            model_name='demande',
            name='AvisSoutnance',
            field=models.ImageField(default='photos/22/11/24/cv.png', upload_to='photos/%y/%m/%d', verbose_name='Image Avis de soutnance'),
        ),
    ]
