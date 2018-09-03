from django.shortcuts import render
from .models import Graficna, Tipkovnica, Procesor, Maticna, Zvocna, Napajalnik, Miska, Disk, Ram, Mrezna, Zaslon
from django.http import HttpResponse
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from email.utils import parseaddr

import logging
logger = logging.getLogger(__name__)
    
def registracija(request):
    
    context = {}
    
    if request.method == 'GET' and 'ime' in request.GET:
    
        #racuni = Racun.objects.all()        
        #context['racuni'] = racuni  
        
        ime = request.GET['ime']
        geslo = request.GET['geslo']
        geslo1 = request.GET['geslo1']
        email = request.GET['email']       
        
        # validacija - preveri če so vsa polja vnešena, če sta gesli enaki in če je @ v email-u 
        if ime=="" or geslo=="" or geslo1=="" or email=="":
            context['warning'] = "Izpolnite vsa polja!"
            return render(request, 'kalkulator/registracija.html', context)
        
        if not geslo==geslo1:
            context['warning'] = "Gesli se ne ujemata!"
            return render(request, 'kalkulator/registracija.html', context)        
        
        if '@' not in email: 
            context['warning'] = "Vnesite veljaven email naslov!"
            return render(request, 'kalkulator/registracija.html', context)   
                  
        a = User.objects.create_user(username=ime, password=geslo, email=email)
        group = Group.objects.get(name='user')
        a.groups.add(group)        
        a.save()                       
                
        login(request, a)
        
        context = {}            
    
        return render(request, 'kalkulator/main.html', context)
    
    return render(request, 'kalkulator/registracija.html')
    
    
 
@login_required 
def main(request):          
    context = {}
    
    
    return render(request, 'kalkulator/main.html', context)
    
@login_required 
def tipkovnice(request):   

    context = {} 
    tipkovnice = Tipkovnica.objects.all() 
        
    # S temi parametri napolnimo dropdown-e v htmlju, torej npr. seznam vseh znamk
    znamke = Tipkovnica.objects.values_list('znamka', flat=True).distinct()
    prikljucki = Tipkovnica.objects.values_list('prikljucek', flat=True).distinct()
    povezave = Tipkovnica.objects.values_list('povezava', flat=True).distinct()    
    context['znamke'] = znamke 
    context['prikljucki'] = prikljucki
    context['povezave'] = povezave

    # Če želimo samo tipkovnice z določenim priključkom
    if request.method == 'GET'  and 'prikljucek' in request.GET: 
             
        # izbran prikljucek v dropdown listu  
        znamka = request.GET['znamka']
        prikljucek = request.GET['prikljucek']
        povezava = request.GET['povezava']
        
        # v primeru da so izbrani vsi priljučki, prikažemo vse tipkovnice  
        if znamka != 'Vsi':                          
            tipkovnice = Tipkovnica.objects.filter(znamka=znamka)   

        if prikljucek != 'Vsi':    
            tipkovnice = tipkovnice.filter(prikljucek=prikljucek)
            
        if povezava != 'Vsi':    
            tipkovnice = tipkovnice.filter(povezava=povezava)    

            
        context['tipkovnice'] = tipkovnice
        return render(request, 'kalkulator/tipkovnice.html', context)
          
    tipkovnice = Tipkovnica.objects.all()       
    context['tipkovnice'] = tipkovnice  
    
    return render(request, 'kalkulator/tipkovnice.html', context)
 
@login_required 
def zasloni(request):   

    context = {} 
    zasloni = Zaslon.objects.all() 
        
    # S temi parametri napolnimo dropdown-e v htmlju, torej npr. seznam vseh znamk
    znamke = Zaslon.objects.values_list('znamka', flat=True).distinct()
    velikosti = Zaslon.objects.values_list('velikost', flat=True).distinct()      
    context['znamke'] = znamke 
    context['velikosti'] = velikosti
 

    # Če želimo samo tipkovnice z določenim priključkom
    if request.method == 'GET'  and 'znamka' in request.GET: 
             
        # izbran prikljucek v dropdown listu  
        znamka = request.GET['znamka']
        vrsta = request.GET['vrsta']
        velikost = request.GET['velikost']
        
        # v primeru da so izbrani vsi priljučki, prikažemo vse tipkovnice  
        if znamka != 'Vsi':                          
            zasloni = Zaslon.objects.filter(znamka=znamka)   

        if vrsta != 'Vsi':    
            zasloni = zasloni.filter(vrsta=vrsta)
            
        if velikost != 'Vsi':    
            zasloni = zasloni.filter(velikost=velikost)    

            
        context['zasloni'] = zasloni
        return render(request, 'kalkulator/zasloni.html', context)
          
    zasloni = Zaslon.objects.all()       
    context['zasloni'] = zasloni  
    
    return render(request, 'kalkulator/zasloni.html', context)
 
 
 
@login_required 
def graficne(request):    
    
    context = {}
    graficne = Graficna.objects.all() 

    # S temi parametri napolnimo dropdown-e v htmlju, torej npr. seznam vseh znamk
    znamke = Graficna.objects.values_list('znamka', flat=True).distinct()
    povezave = Graficna.objects.values_list('povezava', flat=True).distinct()
    pomnilniki = Graficna.objects.values_list('pomnilnik', flat=True).distinct()
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
 
@login_required 
def rami(request):    
    
    context = {}
    rami = Ram.objects.all() 

    # S temi parametri napolnimo dropdown-e v htmlju, torej npr. seznam vseh znamk
    znamke = Ram.objects.values_list('znamka', flat=True).distinct()
    vrste = Ram.objects.values_list('vrsta', flat=True).distinct()
    velikosti = Ram.objects.values_list('velikost', flat=True).distinct()
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
  
 
 
@login_required 
def procesorji(request):    
    
    context = {}
    procesorji = Procesor.objects.all()  
    
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

@login_required 
def maticne(request):    
    
    context = {}
    maticne = Maticna.objects.all() 

    # S temi parametri napolnimo dropdown-e v htmlju, torej npr. seznam vseh znamk
    znamke = Maticna.objects.values_list('znamka', flat=True).distinct()
    podnozja = Maticna.objects.values_list('podnozje', flat=True).distinct()   
    context['znamke'] = znamke 
    context['podnozja'] = podnozja    
    
    # Če želimo samo procesorje z izbranimi parametri iz dropdowna
    if request.method == 'GET'  and 'znamka' in request.GET:                   
                 
        # izbran prikljucek v dropdown listu  
        znamka = request.GET['znamka']  
        model = request.GET['model']
        podnozje = request.GET['podnozje'] 
        opis = request.GET['opis'] 
                            
        if znamka != 'Vsi':            
            maticne = Maticna.objects.filter(znamka=znamka)
       
        if model != '':
            maticne = maticne.filter(model=model)         
            
        if podnozje != 'Vsi':    
            maticne = maticne.filter(podnozje=podnozje)   
                          
        context['maticne'] = maticne
        return render(request, 'kalkulator/maticne.html', context)
                  
    context['maticne'] = maticne  
    
    return render(request, 'kalkulator/maticne.html', context)

@login_required 
def zvocne(request):    
    
    context = {}
    zvocne = Zvocna.objects.all()  
    
    # S temi parametri napolnimo dropdown-e v htmlju, torej npr. seznam vseh znamk
    znamke = Zvocna.objects.values_list('znamka', flat=True).distinct()       
    context['znamke'] = znamke 
    
    
    # Če želimo samo zvocne z izbranimi parametri iz dropdowna
    if request.method == 'GET'  and 'znamka' in request.GET:                   
          
        # izbran prikljucek v dropdown listu  
        znamka = request.GET['znamka']
        model = request.GET['model']
        prikljucek = request.GET['prikljucek']               
         
        if znamka != 'Vsi':
            zvocne = Zvocna.objects.filter(znamka=znamka)
         
        if model != '':   
            zvocne = zvocne.filter(model=model)         
            
        if prikljucek != 'Vsi':    
            zvocne = zvocne.filter(prikljucek=prikljucek)   
                          
        context['zvocne'] = zvocne
        return render(request, 'kalkulator/zvocne.html', context)
                  
    context['zvocne'] = zvocne  
    
    return render(request, 'kalkulator/zvocne.html', context)
 
@login_required 
def napajalniki(request):    
    
    context = {}
    napajalniki = Napajalnik.objects.all() 

    # S temi parametri napolnimo dropdown-e v htmlju, torej npr. seznam vseh znamk
    znamke = Napajalnik.objects.values_list('znamka', flat=True).distinct() 
    moci = Napajalnik.objects.values_list('moc', flat=True).distinct()  
    context['znamke'] = znamke 
    context['moci'] = moci 
    
    # Če želimo samo zvocne z izbranimi parametri iz dropdowna
    if request.method == 'GET'  and 'znamka' in request.GET:                   
          
        # izbran prikljucek v dropdown listu  
        znamka = request.GET['znamka']  
        moc = request.GET['moc']                     
         
        if znamka != 'Vsi':
            napajalniki = Napajalnik.objects.filter(znamka=znamka)
         
        if moc != 'Vsi':   
            napajalniki = napajalniki.filter(moc=moc)         
                                
        context['napajalniki'] = napajalniki
        return render(request, 'kalkulator/napajalniki.html', context)
                  
    context['napajalniki'] = napajalniki  
    
    return render(request, 'kalkulator/napajalniki.html', context)    

@login_required 
def miske(request):    
    
    context = {}
    miske = Miska.objects.all()  
    
    # S temi parametri napolnimo dropdown-e v htmlju, torej npr. seznam vseh znamk
    znamke = Miska.objects.values_list('znamka', flat=True).distinct()       
    context['znamke'] = znamke         
        
    # Če želimo samo zvocne z izbranimi parametri iz dropdowna
    if request.method == 'GET'  and 'znamka' in request.GET:                   
          
        # izbran prikljucek v dropdown listu  
        znamka = request.GET['znamka']  
        prikljucek = request.GET['prikljucek']
        povezava = request.GET['povezava']
         
        if znamka != 'Vsi':
            miske = Miska.objects.filter(znamka=znamka)
         
        if prikljucek != 'Vsi':   
            miske = miske.filter(prikljucek=prikljucek)         
         
        if povezava != 'Vsi':   
            miske = miske.filter(povezava=povezava)         
         
         
        context['miske'] = miske
        return render(request, 'kalkulator/miske.html', context)
                  
    context['miske'] = miske  
    
    return render(request, 'kalkulator/miske.html', context)    

@login_required 
def mrezne(request):    
    
    context = {}
    mrezne = Mrezna.objects.all()  
    
    # S temi parametri napolnimo dropdown-e v htmlju, torej npr. seznam vseh znamk
    znamke = Mrezna.objects.values_list('znamka', flat=True).distinct()       
    context['znamke'] = znamke         
        
    # Če želimo samo zvocne z izbranimi parametri iz dropdowna
    if request.method == 'GET'  and 'znamka' in request.GET:                   
          
        # izbran prikljucek v dropdown listu  
        znamka = request.GET['znamka']  
        prikljucek = request.GET['prikljucek']
        vrsta = request.GET['vrsta']
         
        if znamka != 'Vsi':
            mrezne = Mrezna.objects.filter(znamka=znamka)
         
        if prikljucek != 'Vsi':   
            mrezne = mrezne.filter(prikljucek=prikljucek)         
         
        if vrsta != 'Vsi':   
            mrezne = mrezne.filter(vrsta=vrsta)         
         
         
        context['mrezne'] = mrezne
        return render(request, 'kalkulator/mrezne.html', context)
                  
    context['mrezne'] = mrezne  
    
    return render(request, 'kalkulator/mrezne.html', context)    
 
    
@login_required 
def diski(request):    
    
    context = {}
    diski = Disk.objects.all()  
    
    # S temi parametri napolnimo dropdown-e v htmlju, torej npr. seznam vseh znamk
    znamke = Disk.objects.values_list('znamka', flat=True).distinct()   
    velikosti = Disk.objects.values_list('velikost', flat=True).distinct()
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
 
 
 


    
@login_required
def dodajTipkovnico(request):
    
    context = {}
    
    # S temi parametri napolnimo dropdown-e v htmlju, torej npr. seznam vseh znamk
    znamke = Tipkovnica.objects.values_list('znamka', flat=True).distinct()     
    context['znamke'] = znamke   
    
    if request.method == 'GET'  and 'znamka' in request.GET:        
        znamka = request.GET['znamka']        
        if(request.GET['znamka1'] != ''):
            znamka = request.GET['znamka1']            
        prikljucek = request.GET['prikljucek']
        povezava = request.GET['povezava']
        opis = request.GET['opis']   
        kolicina = request.GET['kolicina']         
               
        nova_tipkovnica = Tipkovnica(znamka=znamka, prikljucek=prikljucek, povezava=povezava, opis=opis, kolicina=kolicina)
        nova_tipkovnica.save()
            
    return render(request, 'kalkulator/dodajTipkovnico.html', context)    

@login_required
def dodajDisk(request):
    
    context = {}
        
    # S temi parametri napolnimo dropdown-e v htmlju, torej npr. seznam vseh znamk
    znamke = Disk.objects.values_list('znamka', flat=True).distinct()   
    velikosti = Disk.objects.values_list('velikost', flat=True).distinct()
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
  
@login_required
def dodajRam(request):
    
    context = {}
        
    # S temi parametri napolnimo dropdown-e v htmlju, torej npr. seznam vseh znamk
    znamke = Ram.objects.values_list('znamka', flat=True).distinct() 
    vrste = Ram.objects.values_list('vrsta', flat=True).distinct()    
    velikosti = Ram.objects.values_list('velikost', flat=True).distinct()
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
 
  
@login_required
def dodajMaticno(request):
    
    context = {}
    
    # S temi parametri napolnimo dropdown-e v htmlju, torej npr. seznam vseh znamk
    znamke = Maticna.objects.values_list('znamka', flat=True).distinct()
    podnozja = Maticna.objects.values_list('podnozje', flat=True).distinct()   
    context['znamke'] = znamke 
    context['podnozja'] = podnozja
    
    if request.method == 'GET'  and 'znamka' in request.GET:

        znamka = request.GET['znamka']
        if(request.GET['znamka1'] != ''):
            znamka = request.GET['znamka1']
        model = request.GET['model']       
        podnozje = request.GET['podnozje']
        if(request.GET['podnozje1'] != ''):
            podnozje = request.GET['podnozje1']
        opis = request.GET['opis']
        kolicina = request.GET['kolicina']
        
        nova_maticna = Maticna(znamka=znamka, model=model, podnozje=podnozje, opis=opis, kolicina=kolicina)
        nova_maticna.save()
            
    return render(request, 'kalkulator/dodajMaticno.html', context)    
 
@login_required
def dodajNapajalnik(request):
    
    context = {}
    
    # S temi parametri napolnimo dropdown-e v htmlju, torej npr. seznam vseh znamk
    znamke = Napajalnik.objects.values_list('znamka', flat=True).distinct() 
    moci = Napajalnik.objects.values_list('moc', flat=True).distinct()  
    context['znamke'] = znamke 
    context['moci'] = moci
    

    if request.method == 'GET'  and 'znamka' in request.GET:

        znamka = request.GET['znamka']
        if(request.GET['znamka1'] != ''):
            znamka = request.GET['znamka1']
        moc = request.GET['moc']  
        if(request.GET['moc1'] != ''):
            moc = request.GET['moc1']
        opis = request.GET['opis']
        kolicina = request.GET['kolicina']
        
        nov_napajalnik = Napajalnik(znamka=znamka, moc=moc, opis=opis, kolicina=kolicina)
        nov_napajalnik.save()
            
    return render(request, 'kalkulator/dodajNapajalnik.html', context)  
 
 
@login_required
def dodajZvocno(request):
    
    context = {}
    
    # S temi parametri napolnimo dropdown-e v htmlju, torej npr. seznam vseh znamk
    znamke = Zvocna.objects.values_list('znamka', flat=True).distinct()       
    context['znamke'] = znamke     
    
    if request.method == 'GET'  and 'znamka' in request.GET:

        znamka = request.GET['znamka']
        if(request.GET['znamka1'] != ''):
            znamka = request.GET['znamka1']
        model = request.GET['model']        
        prikljucek = request.GET['prikljucek']
        opis = request.GET['opis']
        kolicina = request.GET['kolicina']
        
        nova_zvocna = Zvocna(znamka=znamka, model=model, prikljucek=prikljucek, opis=opis, kolicina=kolicina)
        nova_zvocna.save()
            
    return render(request, 'kalkulator/dodajZvocno.html', context) 
 

 
@login_required
def dodajMisko(request):
    
    context = {}
        
    # S temi parametri napolnimo dropdown-e v htmlju, torej npr. seznam vseh znamk
    znamke = Miska.objects.values_list('znamka', flat=True).distinct()     
    context['znamke'] = znamke 
        
    if request.method == 'GET'  and 'znamka' in request.GET:

        znamka = request.GET['znamka']
        if(request.GET['znamka1'] != ''):
           znamka = request.GET['znamka1']
        prikljucek = request.GET['prikljucek']
        povezava = request.GET['povezava']    
        opis = request.GET['opis']
        kolicina = request.GET['kolicina']
        
        nova_miska = Miska(znamka=znamka, prikljucek=prikljucek, povezava=povezava, opis=opis, kolicina=kolicina)
        nova_miska.save()
            
    return render(request, 'kalkulator/dodajMisko.html', context) 
  
@login_required
def dodajMrezno(request):
    
    context = {}
        
    # S temi parametri napolnimo dropdown-e v htmlju, torej npr. seznam vseh znamk
    znamke = Mrezna.objects.values_list('znamka', flat=True).distinct()     
    context['znamke'] = znamke 
        
    if request.method == 'GET'  and 'znamka' in request.GET:

        znamka = request.GET['znamka']
        if(request.GET['znamka1'] != ''):
           znamka = request.GET['znamka1']
        prikljucek = request.GET['prikljucek']
        vrsta = request.GET['vrsta']    
        opis = request.GET['opis']
        kolicina = request.GET['kolicina']
        
        nova_mrezna = Mrezna(znamka=znamka, prikljucek=prikljucek, vrsta=vrsta, opis=opis, kolicina=kolicina)
        nova_mrezna.save()
            
    return render(request, 'kalkulator/dodajMrezno.html', context) 
   
  
  
@login_required
def dodajGraficno(request):
    
    context = {}
    
    # S temi parametri napolnimo dropdown-e v htmlju, torej npr. seznam vseh znamk
    znamke = Graficna.objects.values_list('znamka', flat=True).distinct()  
    pomnilniki = Graficna.objects.values_list('pomnilnik', flat=True).distinct()
    context['znamke'] = znamke   
    context['pomnilniki'] = pomnilniki
        
    if request.method == 'GET'  and 'znamka' in request.GET:

        znamka = request.GET['znamka']
        if(request.GET['znamka1'] != ''):
            znamka = request.GET['znamka1']
        model = request.GET['model']
        pomnilnik = request.GET['pomnilnik']
        if(request.GET['pomnilnik1'] != ''):
            pomnilnik = request.GET['pomnilnik1'] 
        povezava = request.GET['povezava']
        opis = request.GET['opis']
        kolicina = request.GET['kolicina']
        
        nova_graficna = Graficna(znamka=znamka, model=model, pomnilnik=pomnilnik, povezava=povezava, opis=opis, kolicina=kolicina)
        nova_graficna.save()
            
    return render(request, 'kalkulator/dodajGraficno.html', context)    
  
@login_required
def dodajProcesor(request):
    
    context = {}

    if request.method == 'GET'  and 'znamka' in request.GET:

        znamka = request.GET['znamka'].upper()
        model = request.GET['model'].upper()        
        podnozje = request.GET['podnozje'].upper()
        kolicina = request.GET['kolicina']
        
        nov_procesor = Procesor(znamka=znamka, model=model, podnozje=podnozje, kolicina=kolicina)
        nov_procesor.save()
            
    return render(request, 'kalkulator/dodajProcesor.html', context)    

    
@login_required
def dodajZaslon(request):
    
    context = {}
    
    # S temi parametri napolnimo dropdown-e v htmlju, torej npr. seznam vseh znamk
    znamke = Zaslon.objects.values_list('znamka', flat=True).distinct()  
    velikosti = Zaslon.objects.values_list('velikost', flat=True).distinct()     
    context['znamke'] = znamke     
    context['velikosti'] = velikosti

    
    if request.method == 'GET'  and 'znamka' in request.GET:

        znamka = request.GET['znamka']
        if(request.GET['znamka1'] != ''):
            znamka = request.GET['znamka1']
        model = request.GET['model']        
        vrsta = request.GET['vrsta']
        velikost = request.GET['velikost']
        if(request.GET['velikost1'] != ''):
            velikost = request.GET['velikost1']
        opis = request.GET['opis']
        kolicina = request.GET['kolicina']
        
        nov_zaslon = Zaslon(znamka=znamka, model=model, vrsta=vrsta, velikost=velikost, opis=opis, kolicina=kolicina)
        nov_zaslon.save()
            
    return render(request, 'kalkulator/dodajZaslon.html', context) 
 
  


 


 