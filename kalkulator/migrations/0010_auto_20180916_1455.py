# Generated by Django 2.1.1 on 2018-09-16 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kalkulator', '0009_auto_20180913_0041'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Adapter',
        ),
        migrations.AddField(
            model_name='napajalnik',
            name='amperaza',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='napajalnik',
            name='voltaza',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
    ]