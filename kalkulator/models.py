from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.
class Tipkovnice(models.Model):     
    znamka = models.CharField(max_length=20)
    prikljucek = models.CharField(max_length=20)
    povezava = models.CharField(max_length=20)
    kolicina = models.CharField(max_length=20)
    
class Graficne(models.Model):     
    znamka = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    pomnilnik = models.CharField(max_length=20)
    povezava = models.CharField(max_length=20)
    opis = models.CharField(max_length=100)
    kolicina = models.CharField(max_length=20)

    
class Racun(models.Model):
	uporabnik = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
	ime = models.CharField(max_length=20)
	stanje = models.DecimalField(decimal_places=2, max_digits=100)
		
	def __str__(self):
		return self.uporabnik.username + ": " + self.ime + ", " + str(self.stanje) + "€ "
		
class Vnos(models.Model):
	racun = models.ForeignKey(Racun, on_delete=models.CASCADE)	
	vrsta = models.CharField(max_length=20)	
	kategorija = models.CharField(max_length=20)
	znesek = models.DecimalField(decimal_places=2, max_digits=50, default=0)	
	podrobnosti = models.CharField(max_length=100)	
	datum = models.DateTimeField(default=datetime.datetime.now)				
		
	def __str__(self):
		#return self.datum.strftime('%Y-%m-%d %H:%M') + ": " + self.vrsta + ", " + self.kategorija +  ", "+ str(self.znesek) + "€, " +  self.podrobnosti
		return self.datum.strftime('%d.%m.%Y') + "   " + self.kategorija + " " + "  " +  str(self.znesek) + "€  " + self.podrobnosti
        
        
        
