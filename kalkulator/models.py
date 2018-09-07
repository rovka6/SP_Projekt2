from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.
   
class Graficna(models.Model):     
    znamka = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    pomnilnik = models.CharField(max_length=20)
    povezava = models.CharField(max_length=20)
    opis = models.CharField(max_length=100)
    kolicina = models.CharField(max_length=20)

class Procesor(models.Model):     
    znamka = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    podnozje = models.CharField(max_length=20)    
    kolicina = models.CharField(max_length=20)
    
class Maticna(models.Model):     
    znamka = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    podnozje = models.CharField(max_length=20)
    ram = models.CharField(max_length=20)
    graficna = models.CharField(max_length=20)
    opis = models.CharField(max_length=20) 
    kolicina = models.CharField(max_length=20)
    
class Napajalnik(models.Model):     
    znamka = models.CharField(max_length=20)    
    moc = models.CharField(max_length=20)       
    opis = models.CharField(max_length=20) 
    kolicina = models.CharField(max_length=20)   

class Disk(models.Model):     
    znamka = models.CharField(max_length=20)    
    prikljucek = models.CharField(max_length=20)       
    velikost = models.CharField(max_length=20) 
    opis = models.CharField(max_length=20)
    kolicina = models.CharField(max_length=20)    
	
class Ram(models.Model):
    znamka = models.CharField(max_length=20)
    vrsta = models.CharField(max_length=20)
    velikost = models.CharField(max_length=20)
    opis = models.CharField(max_length=20)
    kolicina = models.CharField(max_length=20)
     
class Razsiritvena(models.Model):
    znamka = models.CharField(max_length=20)
    model = models.CharField(max_length=20) 
    vrsta = models.CharField(max_length=20)
    prikljucek = models.CharField(max_length=20)    
    opis = models.CharField(max_length=20)
    kolicina = models.CharField(max_length=20) 
   
class Zaslon(models.Model):
    znamka = models.CharField(max_length=20)
    model = models.CharField(max_length=20)    
    vrsta = models.CharField(max_length=20)
    velikost = models.CharField(max_length=20)
    input = models.CharField(max_length=20)
    opis = models.CharField(max_length=20)
    kolicina = models.CharField(max_length=20) 
    
class Kabel(models.Model):        
    vrsta = models.CharField(max_length=20)   
    opis = models.CharField(max_length=20)
    kolicina = models.CharField(max_length=20)   
    
class Input(models.Model):   
    vrsta = models.CharField(max_length=20)
    znamka = models.CharField(max_length=20)    
    prikljucek = models.CharField(max_length=20)       
    povezava = models.CharField(max_length=20) 
    opis = models.CharField(max_length=20)
    kolicina = models.CharField(max_length=20)  
       