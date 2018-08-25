# Generated by Django 2.1 on 2018-08-23 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kalkulator', '0017_procesorji_vrsta'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tipkovnice',
            old_name='vrstaPrikljucka',
            new_name='povezava',
        ),
        migrations.RemoveField(
            model_name='procesorji',
            name='vrsta',
        ),
        migrations.RemoveField(
            model_name='tipkovnice',
            name='brezZicna',
        ),
        migrations.RemoveField(
            model_name='tipkovnice',
            name='vrsta',
        ),
        migrations.AddField(
            model_name='tipkovnice',
            name='prikljucek',
            field=models.CharField(default='zicna', max_length=20),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Komponenta',
        ),
    ]
