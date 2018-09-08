from django.shortcuts import render
from .models import Graficna, Procesor, Maticna, Napajalnik,  Disk, Ram, Razsiritvena, Zaslon, Kabel, Input, Adapter
from django.http import HttpResponse
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from email.utils import parseaddr
from django.db.models.functions import Length
from django.db.models.functions import Lower
from .form_config.forms import ImageUploadForm

import logging
logger = logging.getLogger(__name__)   

def main(request):          
    context = {}
    
    
    return render(request, 'kalkulator/main.html', context)
  
 
def vrsteNapajalnikov(request):          
    context = {}
    
    
    return render(request, 'kalkulator/vrsteNapajalnikov.html', context)

 
def adapterji(request):          
    context = {} 
    adapterji = Adapter.objects.all() 
        
    # S temi parametri napolnimo dropdown-e v htmlju, torej npr. seznam vseh znamk
    vrste = Adapter.objects.values('vrsta').distinct().order_by(Lower('vrsta')).values_list('vrsta', flat=True)
    znamke = Adapter.objects.values('znamka').distinct().order_by(Lower('znamka')).values_list('znamka', flat=True)
    voltaze = Adapter.objects.values('voltaza').distinct().order_by(Lower('voltaza')).values_list('voltaza', flat=True)
    amperaze = Adapter.objects.values('amperaza').distinct().order_by(Lower('amperaza')).values_list('amperaza', flat=True)
    context['vrste'] = vrste 
    context['znamke'] = znamke 
    context['voltaze'] = voltaze
    context['amperaze'] = amperaze

    # Če želimo samo tipkovnice z določenim priključkom
    if request.method == 'GET'  and 'znamka' in request.GET: 
             
        # izbran prikljucek v dropdown listu 
        vrsta = request.GET['vrsta']
        znamka = request.GET['znamka']        
        voltaza = request.GET['voltaza']
        amperaza = request.GET['amperaza']
        
        # v primeru da so izbrani vsi priljučki, prikažemo vse tipkovnice  
        if vrsta != 'Vsi':    
            adapterji = Adapter.objects.filter(vrsta=vrsta)           
        
        if znamka != 'Vsi':                          
            adapterji = adapterji.filter(znamka=znamka)   

      
        if voltaza != 'Vsi':    
            adapterji = adapterji.filter(voltaza=voltaza)    

        if amperaza != 'Vsi':    
            adapterji = adapterji.filter(amperaza=amperaza)    
            
        context['adapterji'] = adapterji
        return render(request, 'kalkulator/adapterji.html', context)
          
    zasloni = Adapter.objects.all()       
    context['adapterji'] = adapterji  
    
    return render(request, 'kalkulator/adapterji.html', context)
     
  
 
def zasloni(request):   

    context = {} 
    zasloni = Zaslon.objects.all() 
        
    # S temi parametri napolnimo dropdown-e v htmlju, torej npr. seznam vseh znamk
    znamke = Zaslon.objects.values('znamka').distinct().order_by(Lower('znamka')).values_list('znamka', flat=True)
    velikosti = Zaslon.objects.values('velikost').distinct().order_by(Lower('velikost')).values_list('velikost', flat=True)
    inputi = Zaslon.objects.values('input').distinct().order_by(Lower('input')).values_list('input', flat=True)
    context['znamke'] = znamke 
    context['velikosti'] = velikosti
    context['inputi'] = inputi

    # Če želimo samo tipkovnice z določenim priključkom
    if request.method == 'GET'  and 'znamka' in request.GET: 
             
        # izbran prikljucek v dropdown listu  
        znamka = request.GET['znamka']
        vrsta = request.GET['vrsta']
        velikost = request.GET['velikost']
        input = request.GET['input']
        
        # v primeru da so izbrani vsi priljučki, prikažemo vse tipkovnice  
        if znamka != 'Vsi':                          
            zasloni = Zaslon.objects.filter(znamka=znamka)   

        if vrsta != 'Vsi':    
            zasloni = zasloni.filter(vrsta=vrsta)
            
        if velikost != 'Vsi':    
            zasloni = zasloni.filter(velikost=velikost)    

        if input != 'Vsi':    
            zasloni = zasloni.filter(input=input)    
            
        context['zasloni'] = zasloni
        return render(request, 'kalkulator/zasloni.html', context)
          
    zasloni = Zaslon.objects.all()       
    context['zasloni'] = zasloni  
    
    return render(request, 'kalkulator/zasloni.html', context)
 
 
 
 
def graficne(request):    
    
    context = {}
    graficne = Graficna.objects.all() 

    # S temi parametri napolnimo dropdown-e v htmlju, torej npr. seznam vseh znamk
    znamke = Graficna.objects.values('znamka').distinct().order_by(Lower('znamka')).values_list('znamka', flat=True)
    povezave = Graficna.objects.values('povezava').distinct().order_by(Lower('povezava')).values_list('povezava', flat=True)
    pomnilniki = Graficna.objects.values('pomnilnik').distinct().order_by('pomnilnik').values_list('pomnilnik', flat=True)
    print(pomnilniki)
    context['znamke'] = znamke
    context['povezave'] = povezave
    context['pomnilniki'] = pomnilniki
      
      
    # Če želimo samo grafične z izbranimi parametri iz dropdowna
    if request.method == 'GET'  and 'znamka' in request.GET:   
           
          
        # izbran prikljucek v dropdown listu  
        znamka1 = request.GET['znamka']   
        povezava1 = request.GET['povezava'] 
        pomnilnik = request.GET['pomnilnik']              
                
        if znamka1 != 'Vsi':            
            graficne = Graficna.objects.filter(znamka=znamka1) 
            
        if povezava1 != 'Vsi':    
            graficne = graficne.filter(povezava=povezava1)

        if pomnilnik != 'Vsi':    
            graficne = graficne.filter(pomnilnik=pomnilnik)          
                          
        context['graficne'] = graficne
        return render(request, 'kalkulator/graficne.html', context)
                  
    context['graficne'] = graficne  
    
    return render(request, 'kalkulator/graficne.html', context)   
 
 
def rami(request):    
    
    context = {}
    rami = Ram.objects.all() 

    # S temi parametri napolnimo dropdown-e v htmlju, torej npr. seznam vseh znamk
    znamke = Ram.objects.values('znamka').distinct().order_by(Lower('znamka')).values_list('znamka', flat=True)
    vrste = Ram.objects.values('vrsta').distinct().order_by(Lower('vrsta')).values_list('vrsta', flat=True)
    velikosti = Ram.objects.values('velikost').distinct().order_by(Lower('velikost')).values_list('velikost', flat=True)
    context['znamke'] = znamke 
    context['vrste'] = vrste
    context['velikosti'] = velikosti    
      
    # Če želimo samo grafične z izbranimi parametri iz dropdowna
    if request.method == 'GET'  and 'znamka' in request.GET:   
               
        # izbran prikljucek v dropdown listu  
        znamka = request.GET['znamka']   
        vrsta = request.GET['vrsta'] 
        velikost = request.GET['velikost']              
                
        if znamka != 'Vsi':            
            rami = Ram.objects.filter(znamka=znamka) 
            
        if vrsta != 'Vsi':    
            rami = rami.filter(vrsta=vrsta)

        if velikost != 'Vsi':    
            rami = rami.filter(velikost=velikost)          
                          
        context['rami'] = rami
        return render(request, 'kalkulator/rami.html', context)
                  
    context['rami'] = rami  
    
    return render(request, 'kalkulator/rami.html', context)   
  
 
 
 
def procesorji(request):    
    
    context = {}
    procesorji = Procesor.objects.all()  
    
    # S temi parametri napolnimo dropdown-e v htmlju, torej npr. seznam vseh znamk
    znamke = Procesor.objects.values('znamka').distinct().order_by(Lower('znamka')).values_list('znamka', flat=True)
    podnozja = Procesor.objects.values('podnozje').distinct().order_by(Lower('podnozje')).values_list('podnozje', flat=True)    
    context['znamke'] = znamke 
    context['podnozja'] = podnozja
   
    
    
    # Če želimo samo procesorje z izbranimi parametri iz dropdowna
    if request.method == 'GET'  and 'znamka' in request.GET:                   
          
        # izbran prikljucek v dropdown listu  
        znamka = request.GET['znamka'].upper()   
        model = request.GET['model'].upper()
        podnozje = request.GET['podnozje'] 
                
        if znamka != '':
            procesorji = Procesor.objects.filter(znamka=znamka)
         
        if model != '':   
            procesorji = procesorji.filter(model=model)         
            
        if podnozje != '':    
            procesorji = procesorji.filter(podnozje=podnozje)   
                          
        context['procesorji'] = procesorji
        return render(request, 'kalkulator/procesorji.html', context)
                  
    context['procesorji'] = procesorji  
    
    return render(request, 'kalkulator/procesorji.html', context)

 
def maticne(request):     
    
    context = {}
    maticne = Maticna.objects.all() 

    # S temi parametri napolnimo dropdown-e v htmlju, torej npr. seznam vseh znamk
    znamke = Maticna.objects.values('znamka').distinct().order_by(Lower('znamka')).values_list('znamka', flat=True)
    podnozja = Maticna.objects.values('podnozje').distinct().order_by(Lower('podnozje')).values_list('podnozje', flat=True) 
    rami = Maticna.objects.values('ram').distinct().order_by(Lower('ram')).values_list('ram', flat=True)
    graficne = Maticna.objects.values('graficna').distinct().order_by(Lower('graficna')).values_list('graficna', flat=True)    
    context['znamke'] = znamke 
    context['podnozja'] = podnozja   
    context['rami'] = rami
    context['graficne'] = graficne   
    
    # Če želimo samo procesorje z izbranimi parametri iz dropdowna
    if request.method == 'GET'  and 'znamka' in request.GET:                   
                 
        # izbran prikljucek v dropdown listu  
        znamka = request.GET['znamka']         
        podnozje = request.GET['podnozje'] 
        ram = request.GET['ram']
        graficna = request.GET['graficna']
        
        if znamka != 'Vsi':            
            maticne = Maticna.objects.filter(znamka=znamka)                     
            
        if podnozje != 'Vsi':    
            maticne = maticne.filter(podnozje=podnozje) 

        if ram != 'Vsi':    
            maticne = maticne.filter(ram=ram)
        
        if graficna != 'Vsi':    
            maticne = maticne.filter(graficna=graficna)
            
                          
        context['maticne'] = maticne
        return render(request, 'kalkulator/maticne.html', context)
                  
    context['maticne'] = maticne  
    
    return render(request, 'kalkulator/maticne.html', context)

 
def napajalniki(request):    
    
    context = {}
    napajalniki = Napajalnik.objects.all() 

    # S temi parametri napolnimo dropdown-e v htmlju, torej npr. seznam vseh znamk    
    vrste = Napajalnik.objects.values('vrsta').distinct().order_by(Lower('vrsta')).values_list('vrsta', flat=True)
    znamke = Napajalnik.objects.values('znamka').distinct().order_by(Lower('znamka')).values_list('znamka', flat=True)
    moci = Napajalnik.objects.values('moc').distinct().order_by(Lower('moc')).values_list('moc', flat=True)  
    context['vrste'] = vrste
    context['znamke'] = znamke 
    context['moci'] = moci 
    
    # Če želimo samo zvocne z izbranimi parametri iz dropdowna
    if request.method == 'GET'  and 'znamka' in request.GET:                   
          
        # izbran prikljucek v dropdown listu         
        vrsta = request.GET['vrsta']
        if vrsta != 'Vsi':
            napajalniki = Napajalnik.objects.filter(vrsta=vrsta)                     
        znamka = request.GET['znamka']  
        if znamka != 'Vsi':
            napajalniki = Napajalnik.objects.filter(znamka=znamka)
        moc = request.GET['moc'] 
        if moc != 'Vsi':   
            napajalniki = napajalniki.filter(moc=moc)         
                                
        context['napajalniki'] = napajalniki
        return render(request, 'kalkulator/napajalniki.html', context)
                  
    context['napajalniki'] = napajalniki  
    
    return render(request, 'kalkulator/napajalniki.html', context)    

 
def kabli(request):    
    
    context = {}
    kabli = Kabel.objects.all() 

    # S temi parametri napolnimo dropdown-e v htmlju, torej npr. seznam vseh znamk
    vrste = Kabel.objects.values('vrsta').distinct().order_by(Lower('vrsta')).values_list('vrsta', flat=True)    
    context['vrste'] = vrste 
    
    # Če želimo samo zvocne z izbranimi parametri iz dropdowna
    if request.method == 'GET'  and 'vrsta' in request.GET:                   
          
        # izbran prikljucek v dropdown listu  
        vrsta = request.GET['vrsta']                            
         
        if vrsta != 'Vsi':
            kabli = Kabel.objects.filter(vrsta=vrsta)
         
                 
                                
        context['kabli'] = kabli
        return render(request, 'kalkulator/kabli.html', context)
                  
    context['kabli'] = kabli  
    
    return render(request, 'kalkulator/kabli.html', context)    
   
    
    
 
def inputi(request):    
    
    context = {}
    inputi = Input.objects.all()  
    
    # S temi parametri napolnimo dropdown-e v htmlju, torej npr. seznam vseh znamk
    vrste = Input.objects.values('vrsta').distinct().order_by(Lower('vrsta')).values_list('vrsta', flat=True)
    znamke = Input.objects.values('znamka').distinct().order_by(Lower('vrsta')).values_list('znamka', flat=True)
    prikljucki = Input.objects.values('prikljucek').distinct().order_by(Lower('vrsta')).values_list('prikljucek', flat=True)
    context['znamke'] = znamke
    context['vrste'] = vrste
    context['prikljucki'] = prikljucki
        
    # Če želimo samo zvocne z izbranimi parametri iz dropdowna
    if request.method == 'GET'  and 'znamka' in request.GET:                   
          
        # izbran prikljucek v dropdown listu  
        vrsta = request.GET['vrsta']
        znamka = request.GET['znamka']  
        prikljucek = request.GET['prikljucek']
        povezava = request.GET['povezava']
         
        if vrsta != 'Vsi':
            inputi = Input.objects.filter(vrsta=vrsta) 
         
        if znamka != 'Vsi':
            inputi = inputi.filter(znamka=znamka)
          
        if prikljucek != 'Vsi':   
            inputi = inputi.filter(prikljucek=prikljucek)         
         
        if povezava != 'Vsi':   
            inputi = inputi.filter(povezava=povezava)         
                  
        context['inputi'] = inputi
        return render(request, 'kalkulator/inputi.html', context)
                  
    context['inputi'] = inputi  
    
    return render(request, 'kalkulator/inputi.html', context)    

 
def razsiritvene(request):    
    
    context = {}
    razsiritvene = Razsiritvena.objects.all()  
    
    # S temi parametri napolnimo dropdown-e v htmlju, torej npr. seznam vseh znamk
    znamke = Razsiritvena.objects.values('znamka').distinct().order_by(Lower('znamka')).values_list('znamka', flat=True)
    vrste = Razsiritvena.objects.values('vrsta').distinct().order_by(Lower('vrsta')).values_list('vrsta', flat=True)
    prikljucki = Razsiritvena.objects.values('prikljucek').distinct().order_by(Lower('prikljucek')).values_list('prikljucek', flat=True)
    context['znamke'] = znamke
    context['vrste'] = vrste  
    context['prikljucki'] = prikljucki  
        
    # Če želimo samo zvocne z izbranimi parametri iz dropdowna
    if request.method == 'GET'  and 'znamka' in request.GET:                   
          
        # izbran prikljucek v dropdown listu  
        znamka = request.GET['znamka'] 
        vrsta = request.GET['vrsta']  
        prikljucek = request.GET['prikljucek']
                 
        if znamka != 'Vsi':
            razsiritvene = Razsiritvena.objects.filter(znamka=znamka)
         
        if vrsta != 'Vsi':   
            razsiritvene = razsiritvene.filter(vrsta=vrsta)         
         
        if prikljucek != 'Vsi':   
            razsiritvene = razsiritvene.filter(prikljucek=prikljucek)         
         
      
         
        context['razsiritvene'] = razsiritvene
        return render(request, 'kalkulator/razsiritvene.html', context)
                  
    context['razsiritvene'] = razsiritvene  
    
    return render(request, 'kalkulator/razsiritvene.html', context)    
 
    
 
def diski(request):    
    
    context = {}
    diski = Disk.objects.all()  
    
    # S temi parametri napolnimo dropdown-e v htmlju, torej npr. seznam vseh znamk
    znamke = Disk.objects.values('znamka').distinct().order_by(Lower('znamka')).values_list('znamka', flat=True)  
    velikosti = Disk.objects.values('velikost').distinct().order_by(Lower('znamka')).values_list('velikost', flat=True)
    context['znamke'] = znamke   
    context['velikosti'] = velikosti           
    
    # Če želimo samo zvocne z izbranimi parametri iz dropdowna
    if request.method == 'GET'  and 'znamka' in request.GET:                   
          
        # izbran prikljucek v dropdown listu  
        znamka = request.GET['znamka'] 
        prikljucek = request.GET['prikljucek']
        velikost = request.GET['velikost']
                 
        if znamka != 'Vsi':
            diski = Disk.objects.filter(znamka=znamka)
         
        if prikljucek != 'Vsi':   
            diski = diski.filter(prikljucek=prikljucek)         
         
        if velikost != 'Vsi':   
            diski = diski.filter(velikost=velikost)         
         
         
        context['diski'] = diski
        return render(request, 'kalkulator/diski.html', context)
                  
    context['diski'] = diski  
    
    return render(request, 'kalkulator/diski.html', context)    
 
 

    


def dodajDisk(request):
    
    context = {}
        
    # S temi parametri napolnimo dropdown-e v htmlju, torej npr. seznam vseh znamk
    znamke = Disk.objects.values('znamka').distinct().order_by(Lower('znamka')).values_list('znamka', flat=True)  
    velikosti = Disk.objects.values('velikost').distinct().order_by(Lower('velikost')).values_list('velikost', flat=True)
    context['znamke'] = znamke   
    context['velikosti'] = velikosti        

    if request.method == 'GET'  and 'znamka' in request.GET:

        znamka = request.GET['znamka']
        if(request.GET['znamka1'] != ''):
            znamka = request.GET['znamka1']  
        prikljucek = request.GET['prikljucek']
        velikost = request.GET['velikost']
        if(request.GET['velikost1'] != ''):
            velikost = request.GET['velikost1']  
        opis = request.GET['opis']       
        kolicina = request.GET['kolicina']
        
        nov_disk = Disk(znamka=znamka, prikljucek=prikljucek, velikost=velikost, opis=opis, kolicina=kolicina)
        nov_disk.save()
            
    return render(request, 'kalkulator/dodajDisk.html', context) 
  

def dodajRam(request):
    
    context = {}
        
    # S temi parametri napolnimo dropdown-e v htmlju, torej npr. seznam vseh znamk
    znamke = Ram.objects.values('znamka').distinct().order_by(Lower('znamka')).values_list('znamka', flat=True)
    vrste = Ram.objects.values('vrsta').distinct().order_by(Lower('vrsta')).values_list('vrsta', flat=True)
    velikosti = Ram.objects.values('velikost').distinct().order_by('velikost').values_list('velikost', flat=True)
    context['znamke'] = znamke   
    context['vrste'] = vrste        
    context['velikosti'] = velikosti 
    
    if request.method == 'GET'  and 'znamka' in request.GET:

        znamka = request.GET['znamka']
        if(request.GET['znamka1'] != ''):
            znamka = request.GET['znamka1']  
        vrsta = request.GET['vrsta']
        if(request.GET['vrsta1'] != ''):
            vrsta = request.GET['vrsta1'] 
        velikost = request.GET['velikost']
        if(request.GET['velikost1'] != ''):
            velikost = request.GET['velikost1']  
        opis = request.GET['opis']       
        kolicina = request.GET['kolicina']
        
        nov_disk = Ram(znamka=znamka, vrsta=vrsta, velikost=velikost, opis=opis, kolicina=kolicina)
        nov_disk.save()
            
    return render(request, 'kalkulator/dodajRam.html', context) 
 
  

def dodajMaticno(request):
    
    context = {}
    
    # S temi parametri napolnimo dropdown-e v htmlju, torej npr. seznam vseh znamk
    znamke = Maticna.objects.values('znamka').distinct().order_by(Lower('znamka')).values_list('znamka', flat=True)
    podnozja = Maticna.objects.values('podnozje').distinct().order_by(Lower('podnozje')).values_list('podnozje', flat=True) 
    rami = Maticna.objects.values('ram').distinct().order_by(Lower('ram')).values_list('ram', flat=True)
    graficne = Maticna.objects.values('graficna').distinct().order_by(Lower('graficna')).values_list('graficna', flat=True) 
    context['znamke'] = znamke 
    context['podnozja'] = podnozja
    context['rami'] = rami
    context['graficne'] = graficne
    
    
    
    if request.method == 'GET'  and 'znamka' in request.GET:

        znamka = request.GET['znamka']
        if(request.GET['znamka1'] != ''):
            znamka = request.GET['znamka1']
        model = request.GET['model']       
        podnozje = request.GET['podnozje']
        if(request.GET['podnozje1'] != ''):
            podnozje = request.GET['podnozje1']
        ram = request.GET['ram']
        if(request.GET['ram1'] != ''):
            ram = request.GET['ram1'] 
        graficna = request.GET['graficna']
        if(request.GET['graficna1'] != ''):
            graficna = request.GET['graficna1']        
        opis = request.GET['opis']
        kolicina = request.GET['kolicina']
        
        nova_maticna = Maticna(znamka=znamka, model=model, podnozje=podnozje, ram=ram, graficna=graficna, opis=opis, kolicina=kolicina)
        nova_maticna.save()
            
    return render(request, 'kalkulator/dodajMaticno.html', context)    
 

def dodajNapajalnik(request):
    
    context = {}
    
    
    # S temi parametri napolnimo dropdown-e v htmlju, torej npr. seznam vseh znamk
    vrste = Napajalnik.objects.values('vrsta').distinct().order_by(Lower('vrsta')).values_list('vrsta', flat=True)
    znamke = Napajalnik.objects.values('znamka').distinct().order_by(Lower('znamka')).values_list('znamka', flat=True)
    moci = Napajalnik.objects.values('moc').distinct().order_by(Lower('moc')).values_list('moc', flat=True)  
    context['vrste'] = vrste
    context['znamke'] = znamke 
    context['moci'] = moci
    

    if request.method == 'GET'  and 'znamka' in request.GET:

        vrsta = request.GET['vrsta']
        if(request.GET['vrsta1'] != ''):
            vrsta = request.GET['vrsta1']
        znamka = request.GET['znamka']
        if(request.GET['znamka1'] != ''):
            znamka = request.GET['znamka1']
        moc = request.GET['moc']  
        if(request.GET['moc1'] != ''):
            moc = request.GET['moc1']
        opis = request.GET['opis']
        kolicina = request.GET['kolicina']
        
        nov_napajalnik = Napajalnik(vrsta=vrsta, znamka=znamka, moc=moc, opis=opis, kolicina=kolicina)
        nov_napajalnik.save()
            
    return render(request, 'kalkulator/dodajNapajalnik.html', context)  
   

def dodajInput(request):
    
    context = {}
        
    # S temi parametri napolnimo dropdown-e v htmlju, torej npr. seznam vseh znamk
    vrste = Input.objects.values('vrsta').distinct().order_by(Lower('vrsta')).values_list('vrsta', flat=True)
    znamke = Input.objects.values('znamka').distinct().order_by(Lower('znamka')).values_list('znamka', flat=True)
    prikljucki = Input.objects.values('prikljucek').distinct().order_by(Lower('prikljucek')).values_list('prikljucek', flat=True)
    context['znamke'] = znamke
    context['vrste'] = vrste
    context['prikljucki'] = prikljucki
        
    if request.method == 'GET'  and 'vrsta' in request.GET:

        vrsta = request.GET['vrsta']
        if(request.GET['vrsta1'] != ''):
          vrsta = request.GET['vrsta1']
        znamka = request.GET['znamka']
        if(request.GET['znamka1'] != ''):
          znamka = request.GET['znamka1']
        prikljucek = request.GET['prikljucek']
        if(request.GET['prikljucek1'] != ''):
          prikljucek = request.GET['prikljucek1']
        povezava = request.GET['povezava']    
        opis = request.GET['opis']
        kolicina = request.GET['kolicina']
        
        nov_input = Input(vrsta=vrsta, znamka=znamka, prikljucek=prikljucek, povezava=povezava, opis=opis, kolicina=kolicina)
        nov_input.save()
            
    return render(request, 'kalkulator/dodajInput.html', context) 
    

def dodajGraficno(request):
    
    context = {}
    
    # S temi parametri napolnimo dropdown-e v htmlju, torej npr. seznam vseh znamk
    znamke = Graficna.objects.values('znamka').distinct().order_by(Lower('znamka')).values_list('znamka', flat=True)  
    pomnilniki = Graficna.objects.values('pomnilnik').distinct().order_by(Lower('pomnilnik')).values_list('pomnilnik', flat=True)
    context['znamke'] = znamke   
    context['pomnilniki'] = pomnilniki
    if request.method == 'POST'  and 'znamka' in request.POST:

        znamka = request.POST['znamka']
        if(request.POST['znamka1'] != ''):
            znamka = request.POST['znamka1']
        model = request.POST['model']
        pomnilnik = request.POST['pomnilnik']
        if(request.POST['pomnilnik1'] != ''):
            pomnilnik = request.POST['pomnilnik1'] 
        povezava = request.POST['povezava']
        opis = request.POST['opis']
        kolicina = request.POST['kolicina']
        nova_graficna = Graficna(znamka=znamka, model=model, pomnilnik=pomnilnik, povezava=povezava, opis=opis, kolicina=kolicina)
        
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            nova_graficna.image = form.cleaned_data['image']
            nova_graficna.save()
            
    return render(request, 'kalkulator/dodajGraficno.html', context)    
  

def dodajProcesor(request):
    
    context = {}
    
    # S temi parametri napolnimo dropdown-e v htmlju, torej npr. seznam vseh znamk
    znamke = Procesor.objects.values('znamka').distinct().order_by(Lower('znamka')).values_list('znamka', flat=True)
    podnozja = Procesor.objects.values('podnozje').distinct().order_by(Lower('podnozje')).values_list('podnozje', flat=True)    
    context['znamke'] = znamke 
    context['podnozja'] = podnozja

    if request.method == 'GET'  and 'znamka' in request.GET:

        znamka = request.GET['znamka'].upper()
        if(request.GET['znamka1'] != ''):
            znamka = request.GET['znamka1']
        model = request.GET['model'].upper()        
        podnozje = request.GET['podnozje'].upper()
        if(request.GET['podnozje1'] != ''):
            podnozje = request.GET['podnozje1']
        kolicina = request.GET['kolicina']
        
        nov_procesor = Procesor(znamka=znamka, model=model, podnozje=podnozje, kolicina=kolicina)
        nov_procesor.save()
            
    return render(request, 'kalkulator/dodajProcesor.html', context)    


def dodajKabel(request):
    
    context = {}
    
    # S temi parametri napolnimo dropdown-e v htmlju, torej npr. seznam vseh znamk
    vrste = Kabel.objects.values('vrsta').distinct().order_by(Lower('vrsta')).values_list('vrsta', flat=True)   
    context['vrste'] = vrste
    
    if request.method == 'GET'  and 'vrsta' in request.GET:

        vrsta = request.GET['vrsta']
        if(request.GET['vrsta1'] != ''):
            vrsta = request.GET['vrsta1']
        opis = request.GET['opis']
        kolicina = request.GET['kolicina']
        
        nov_kabel = Kabel(vrsta=vrsta, opis=opis, kolicina=kolicina)
        nov_kabel.save()
            
    return render(request, 'kalkulator/dodajKabel.html', context)    
    
    
    

def dodajZaslon(request):
    
    context = {}
    
    # S temi parametri napolnimo dropdown-e v htmlju, torej npr. seznam vseh znamk
    znamke = Zaslon.objects.values('znamka').distinct().order_by(Lower('znamka')).values_list('znamka', flat=True)
    velikosti = Zaslon.objects.values('velikost').distinct().order_by(Lower('velikost')).values_list('velikost', flat=True)
    inputi = Zaslon.objects.values('input').distinct().order_by(Lower('input')).values_list('input', flat=True)
    context['znamke'] = znamke     
    context['velikosti'] = velikosti
    context['inputi'] = inputi

    
    if request.method == 'GET'  and 'znamka' in request.GET:

        znamka = request.GET['znamka']
        if(request.GET['znamka1'] != ''):
            znamka = request.GET['znamka1']
        model = request.GET['model']        
        vrsta = request.GET['vrsta']
        velikost = request.GET['velikost']
        if(request.GET['velikost1'] != ''):
            velikost = request.GET['velikost1']
        input = request.GET['input']
        if(request.GET['input1'] != ''):
            input = request.GET['input1']    
        opis = request.GET['opis']
        kolicina = request.GET['kolicina']
        
        print(input)
        
        nov_zaslon = Zaslon(znamka=znamka, model=model, vrsta=vrsta, velikost=velikost, input=input, opis=opis, kolicina=kolicina)
        nov_zaslon.save()
            
    return render(request, 'kalkulator/dodajZaslon.html', context) 
 

def dodajRazsiritveno(request):
    
    context = {}
        
    # S temi parametri napolnimo dropdown-e v htmlju, torej npr. seznam vseh znamk
    znamke = Razsiritvena.objects.values('znamka').distinct().order_by(Lower('znamka')).values_list('znamka', flat=True)
    vrste = Razsiritvena.objects.values('vrsta').distinct().order_by(Lower('vrsta')).values_list('vrsta', flat=True)
    prikljucki = Razsiritvena.objects.values('prikljucek').distinct().order_by(Lower('prikljucek')).values_list('prikljucek', flat=True)
    context['znamke'] = znamke
    context['vrste'] = vrste  
    context['prikljucki'] = prikljucki
    
    if request.method == 'GET'  and 'znamka' in request.GET:        
        znamka = request.GET['znamka']        
        if(request.GET['znamka1'] != ''):
            znamka = request.GET['znamka1']
        model = request.GET['model']      
        vrsta = request.GET['vrsta']  
        if(request.GET['vrsta1'] != ''):
            vrsta = request.GET['vrsta1']    
        prikljucek = request.GET['prikljucek']
        if(request.GET['prikljucek1'] != ''):
            prikljucek = request.GET['prikljucek1']
        opis = request.GET['opis']   
        kolicina = request.GET['kolicina']         
               
        nova_razsiritvena = Razsiritvena(znamka=znamka, model=model, vrsta=vrsta, prikljucek=prikljucek, opis=opis, kolicina=kolicina)
        nova_razsiritvena.save()
            
    return render(request, 'kalkulator/dodajRazsiritveno.html', context)    


def dodajAdapter(request):
    
    context = {}
        
    # S temi parametri napolnimo dropdown-e v htmlju, torej npr. seznam vseh znamk
    vrste = Adapter.objects.values('vrsta').distinct().order_by(Lower('vrsta')).values_list('vrsta', flat=True)
    znamke = Adapter.objects.values('znamka').distinct().order_by(Lower('znamka')).values_list('znamka', flat=True)
    voltaze = Adapter.objects.values('voltaza').distinct().order_by(Lower('voltaza')).values_list('voltaza', flat=True)
    amperaze = Adapter.objects.values('amperaza').distinct().order_by(Lower('amperaza')).values_list('amperaza', flat=True)
    context['vrste'] = vrste 
    context['znamke'] = znamke 
    context['voltaze'] = voltaze
    context['amperaze'] = amperaze
    
    if request.method == 'GET'  and 'znamka' in request.GET:        
        vrsta = request.GET['vrsta']  
        if(request.GET['vrsta1'] != ''):
            vrsta = request.GET['vrsta1']
        znamka = request.GET['znamka']        
        if(request.GET['znamka1'] != ''):
            znamka = request.GET['znamka1']                     
        voltaza = request.GET['voltaza']
        if(request.GET['voltaza1'] != ''):
            voltaza = request.GET['voltaza1']
        amperaza = request.GET['amperaza']
        if(request.GET['amperaza1'] != ''):
            amperaza = request.GET['amperaza1']    
        opis = request.GET['opis']   
        kolicina = request.GET['kolicina']         
               
        nov_adapter = Adapter(vrsta=vrsta, znamka=znamka, voltaza=voltaza, amperaza=amperaza, opis=opis, kolicina=kolicina)
        nov_adapter.save()
            
    return render(request, 'kalkulator/dodajAdapter.html', context)    
    
 


 


 