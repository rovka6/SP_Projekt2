# Generated by Django 2.1.1 on 2018-09-12 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kalkulator', '0006_drugo'),
    ]

    operations = [
        migrations.AddField(
            model_name='drugo',
            name='tip',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
    ]
