# Generated by Django 2.1 on 2018-09-06 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kalkulator', '0039_auto_20180906_1859'),
    ]

    operations = [
        migrations.AddField(
            model_name='input',
            name='vrsta',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
    ]