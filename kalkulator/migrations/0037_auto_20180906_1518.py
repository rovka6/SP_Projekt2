# Generated by Django 2.1 on 2018-09-06 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kalkulator', '0036_kabel'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Zvocna',
        ),
        migrations.AddField(
            model_name='maticna',
            name='graficna',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='maticna',
            name='ram',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
    ]
