# Generated by Django 4.0.4 on 2023-01-13 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_login'),
    ]

    operations = [
        migrations.AddField(
            model_name='login',
            name='cv',
            field=models.FileField(default='cv/22/11/24/cv.pdf', upload_to='cv/%y/%m/%d'),
        ),
        migrations.AddField(
            model_name='login',
            name='these',
            field=models.FileField(default='these/22/11/24/these.pdf', upload_to='these/%y/%m/%d'),
        ),
        migrations.DeleteModel(
            name='Username',
        ),
    ]
