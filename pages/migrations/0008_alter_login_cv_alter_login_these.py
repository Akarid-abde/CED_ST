# Generated by Django 4.0.4 on 2023-01-13 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0007_alter_login_cv_alter_login_these'),
    ]

    operations = [
        migrations.AlterField(
            model_name='login',
            name='cv',
            field=models.FileField(default='cvs/22/11/24/cv.pdf', upload_to='cvs/%y/%m/%d', verbose_name='cvs'),
        ),
        migrations.AlterField(
            model_name='login',
            name='these',
            field=models.FileField(default='theses/22/11/24/these.pdf', upload_to='theses/%y/%m/%d', verbose_name='theses'),
        ),
    ]