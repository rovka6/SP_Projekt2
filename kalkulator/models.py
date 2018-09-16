from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.

class Kategorija(models.Model):
    kategorija = models.CharField(max_length=20) 
    podkategorija = models.CharField(max_length=20)
    image = models.ImageField(upload_to='komponente/kategorije', default="/media/no-image.jpg")
   
class Graficna(models.Model):     
    znamka = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    pomnilnik = models.CharField(max_length=20)
    vodilo = models.CharField(max_length=20)
    izhod = models.CharField(max_length=20)
    opis = models.CharField(max_length=20)
    kolicina = models.CharField(max_length=20)
    image = models.ImageField(upload_to='komponente/graficne', default="/media/no-image.jpg")
    
    def __str__(self):
        return self.znamka + ", " + self.model + ", " + self.pomnilnik + ", " + self.vodilo + ", " + self.izhod + ", " + self.opis + ", " + self.kolicina       

class Procesor(models.Model):     
    znamka = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    podnozje = models.CharField(max_length=20) 
    opis = models.CharField(max_length=20)
    kolicina = models.CharField(max_length=20)
    image = models.ImageField(upload_to='komponente/procesorji', default="/media/no-image.jpg")
    
    def __str__(self):
        return self.znamka + ", " + self.model + ", " + self.podnozje + ", " + self.opis + ", " + self.kolicina
        
class Maticna(models.Model):     
    znamka = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    podnozje = models.CharField(max_length=20)
    ram = models.CharField(max_length=20)
    graficna = models.CharField(max_length=20)
    opis = models.CharField(max_length=20)
    kolicina = models.CharField(max_length=20)
    image = models.ImageField(upload_to='komponente/maticne', default="/media/no-image.jpg")
    
    def __str__(self):
        return self.znamka + ", " + self.model + ", " + self.podnozje + ", " + self.ram + ", " + self.graficna + ", " + self.opis + ", " + self.kolicina  
    
class Napajalnik(models.Model):    
    vrsta = models.CharField(max_length=20)
    znamka = models.CharField(max_length=20)    
    moc = models.CharField(max_length=20)
    voltaza = models.CharField(max_length=20)       
    amperaza = models.CharField(max_length=20)    
    opis = models.CharField(max_length=20)
    kolicina = models.CharField(max_length=20)
    image = models.ImageField(upload_to='komponente/napajalniki', default="/media/no-image.jpg")   
    
    def __str__(self):
        return self.znamka + ", " + self.vrsta + ", " + self.moc + ", " + self.voltaza + ", " + self.amperaza + ", " + self.opis + ", " + self.kolicina

class Disk(models.Model):     
    znamka = models.CharField(max_length=20)    
    prikljucek = models.CharField(max_length=20)       
    velikost = models.CharField(max_length=20) 
    opis = models.CharField(max_length=20)
    kolicina = models.CharField(max_length=20)
    image = models.ImageField(upload_to='komponente/diski', default="/media/no-image.jpg")    
    
    def __str__(self):
        return self.znamka + ", " + self.prikljucek + ", " + self.velikost  + ", " + self.opis + ", " + self.kolicina
	
class Ram(models.Model):
    znamka = models.CharField(max_length=20)
    vrsta = models.CharField(max_length=20)
    velikost = models.CharField(max_length=20)
    opis = models.CharField(max_length=20)
    kolicina = models.CharField(max_length=20)
    image = models.ImageField(upload_to='komponente/rami', default="/media/no-image.jpg")
    
    def __str__(self):
        return self.znamka + ", " + self.vrsta + ", " + self.velikost + ", " + self.opis + ", " + self.kolicina
     
class Razsiritvena(models.Model):
    znamka = models.CharField(max_length=20)
    model = models.CharField(max_length=20) 
    vrsta = models.CharField(max_length=20)
    prikljucek = models.CharField(max_length=20)    
    opis = models.CharField(max_length=20)
    kolicina = models.CharField(max_length=20)
    image = models.ImageField(upload_to='komponente/razsiritvene', default="/media/no-image.jpg") 
    
    def __str__(self):
        return self.znamka + ", " + self.model + ", " + self.vrsta + ", " + self.prikljucek + ", " + self.opis + ", " + self.kolicina
   
class Zaslon(models.Model):
    znamka = models.CharField(max_length=20)
    model = models.CharField(max_length=20)    
    vrsta = models.CharField(max_length=20)
    velikost = models.CharField(max_length=20)
    input = models.CharField(max_length=20)
    opis = models.CharField(max_length=20)
    kolicina = models.CharField(max_length=20)
    image = models.ImageField(upload_to='komponente/zasloni', default="/media/no-image.jpg") 
    
    def __str__(self):
        return self.znamka + ", " + self.model + ", " + self.vrsta + ", " + self.velikost + ", " + self.input + ", " + self.opis + ", " + self.kolicina
    
class Kabel(models.Model):        
    vrsta = models.CharField(max_length=20)   
    opis = models.CharField(max_length=20)
    kolicina = models.CharField(max_length=20)
    image = models.ImageField(upload_to='komponente/kabli', default="/media/no-image.jpg")   
    
    def __str__(self):
        return self.vrsta + ", " + self.opis + ", " + self.kolicina
    
class Input(models.Model):   
    vrsta = models.CharField(max_length=20)
    znamka = models.CharField(max_length=20)    
    prikljucek = models.CharField(max_length=20)       
    povezava = models.CharField(max_length=20) 
    opis = models.CharField(max_length=20)
    kolicina = models.CharField(max_length=20)
    image = models.ImageField(upload_to='komponente/inputi', default="/media/no-image.jpg")  
    
    def __str__(self):
        return self.znamka + ", " + self.vrsta + ", " + self.prikljucek + ", " + self.povezava + ", " + self.opis + ", " + self.kolicina
  

class Tiskalnik(models.Model):  
    vrsta = models.CharField(max_length=20)
    tip = models.CharField(max_length=20)
    priklop = models.CharField(max_length=20)
    opis = models.CharField(max_length=20)
    kolicina = models.CharField(max_length=20)
    image = models.ImageField(upload_to='komponente/tiskalniki', default="/media/no-image.jpg")
    
    def __str__(self):
        return self.vrsta + ", " + self.tip + ", " + self.priklop + ", " + self.opis + ", " + self.kolicina
 
class Drugo(models.Model): 
    vrsta = models.CharField(max_length=20)
    ime = models.CharField(max_length=20)
    opis = models.CharField(max_length=20)
    kolicina = models.CharField(max_length=20)
    image = models.ImageField(upload_to='komponente/tiskalniki', default="/media/no-image.jpg") 
    
    def __str__(self):
        return self.vrsta + ", " + self.ime + ", " + self.opis + ", " + self.kolicina

class Periferija(models.Model): 
    vrsta = models.CharField(max_length=20)
    ime = models.CharField(max_length=20)
    opis = models.CharField(max_length=20)
    kolicina = models.CharField(max_length=20)
    image = models.ImageField(upload_to='komponente/tiskalniki', default="/media/no-image.jpg") 
    
    def __str__(self):
        return self.vrsta + ", " + self.ime + ", " + self.opis + ", " + self.kolicina
        
   