# Generated by Django 2.1 on 2018-08-21 16:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('kalkulator', '0012_tipkovnice_uporabnik'),
    ]

    operations = [
        migrations.CreateModel(
            name='Racun1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ime', models.CharField(max_length=20)),
                ('stanje', models.DecimalField(decimal_places=2, max_digits=100)),
                ('uporabnik', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='tipkovnice',
            name='uporabnik',
        ),
    ]
