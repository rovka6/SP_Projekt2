# Generated by Django 2.1.1 on 2018-09-12 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kalkulator', '0004_tiskalnik'),
    ]

    operations = [
        migrations.AddField(
            model_name='tiskalnik',
            name='image',
            field=models.ImageField(default='/media/no-image.jpg', upload_to='komponente/tiskalniki'),
        ),
        migrations.AddField(
            model_name='tiskalnik',
            name='kolicina',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tiskalnik',
            name='opis',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
    ]
