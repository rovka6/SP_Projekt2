# Generated by Django 2.1 on 2018-08-21 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kalkulator', '0013_auto_20180821_1636'),
    ]

    operations = [
        migrations.AddField(
            model_name='tipkovnice',
            name='znamka',
            field=models.CharField(default='neznana', max_length=20),
            preserve_default=False,
        ),
    ]
