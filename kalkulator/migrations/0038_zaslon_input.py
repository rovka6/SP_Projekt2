# Generated by Django 2.1 on 2018-09-06 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kalkulator', '0037_auto_20180906_1518'),
    ]

    operations = [
        migrations.AddField(
            model_name='zaslon',
            name='input',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
    ]
