# Generated by Django 4.0.4 on 2023-01-23 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0015_demande_tele_alter_demande_jury'),
    ]

    operations = [
        migrations.AddField(
            model_name='demande',
            name='Email',
            field=models.EmailField(default='', max_length=255, verbose_name='Email'),
        ),
    ]
