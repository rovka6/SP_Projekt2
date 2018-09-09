from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.
   
class Graficna(models.Model):     
    znamka = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    pomnilnik = models.CharField(max_length=20)
    povezava = models.CharField(max_length=20)
    opis = models.CharField(max_length=20)
    kolicina = models.CharField(max_length=20)
    image = models.ImageField(upload_to='komponente/graficne', default="/media/no-image.jpg")

class Procesor(models.Model):     
    znamka = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    podnozje = models.CharField(max_length=20) 
    opis = models.CharField(max_length=20)
    kolicina = models.CharField(max_length=20)
    image = models.ImageField(upload_to='komponente/procesorji', default="/media/no-image.jpg")
    
class Maticna(models.Model):     
    znamka = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    podnozje = models.CharField(max_length=20)
    ram = models.CharField(max_length=20)
    graficna = models.CharField(max_length=20)
    opis = models.CharField(max_length=20)
    kolicina = models.CharField(max_length=20)
    image = models.ImageField(upload_to='komponente/maticne', default="/media/no-image.jpg")
    
class Napajalnik(models.Model):    
    vrsta = models.CharField(max_length=20)
    znamka = models.CharField(max_length=20)    
    moc = models.CharField(max_length=20)       
    opis = models.CharField(max_length=20)
    kolicina = models.CharField(max_length=20)
    image = models.ImageField(upload_to='komponente/napajalniki', default="/media/no-image.jpg")   

class Disk(models.Model):     
    znamka = models.CharField(max_length=20)    
    prikljucek = models.CharField(max_length=20)       
    velikost = models.CharField(max_length=20) 
    opis = models.CharField(max_length=20)
    kolicina = models.CharField(max_length=20)
    image = models.ImageField(upload_to='komponente/diski', default="/media/no-image.jpg")    
	
class Ram(models.Model):
    znamka = models.CharField(max_length=20)
    vrsta = models.CharField(max_length=20)
    velikost = models.CharField(max_length=20)
    opis = models.CharField(max_length=20)
    kolicina = models.CharField(max_length=20)
    image = models.ImageField(upload_to='komponente/rami', default="/media/no-image.jpg")
     
class Razsiritvena(models.Model):
    znamka = models.CharField(max_length=20)
    model = models.CharField(max_length=20) 
    vrsta = models.CharField(max_length=20)
    prikljucek = models.CharField(max_length=20)    
    opis = models.CharField(max_length=20)
    kolicina = models.CharField(max_length=20)
    image = models.ImageField(upload_to='komponente/razsiritvene', default="/media/no-image.jpg") 
   
class Zaslon(models.Model):
    znamka = models.CharField(max_length=20)
    model = models.CharField(max_length=20)    
    vrsta = models.CharField(max_length=20)
    velikost = models.CharField(max_length=20)
    input = models.CharField(max_length=20)
    opis = models.CharField(max_length=20)
    kolicina = models.CharField(max_length=20)
    image = models.ImageField(upload_to='komponente/zasloni', default="/media/no-image.jpg") 
    
class Kabel(models.Model):        
    vrsta = models.CharField(max_length=20)   
    opis = models.CharField(max_length=20)
    kolicina = models.CharField(max_length=20)
    image = models.ImageField(upload_to='komponente/kabli', default="/media/no-image.jpg")   
    
class Input(models.Model):   
    vrsta = models.CharField(max_length=20)
    znamka = models.CharField(max_length=20)    
    prikljucek = models.CharField(max_length=20)       
    povezava = models.CharField(max_length=20) 
    opis = models.CharField(max_length=20)
    kolicina = models.CharField(max_length=20)
    image = models.ImageField(upload_to='komponente/inputi', default="/media/no-image.jpg")  
   
class Adapter(models.Model):   
    vrsta = models.CharField(max_length=20)
    znamka = models.CharField(max_length=20)    
    voltaza = models.CharField(max_length=20)       
    amperaza = models.CharField(max_length=20) 
    opis = models.CharField(max_length=20)
    kolicina = models.CharField(max_length=20)
    image = models.ImageField(upload_to='komponente/adapterji', default="/media/no-image.jpg")

   