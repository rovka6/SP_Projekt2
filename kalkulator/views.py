from django.shortcuts import render
from .models import Graficna, Tipkovnica, Procesor, Maticna, Zvocna, Napajalnik, Miska, Disk
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

    # Če želimo samo tipkovnice z določenim priključkom
    if request.method == 'GET'  and 'prikljucek' in request.GET: 
             
        # izbran prikljucek v dropdown listu  
        prikljucek1 = request.GET['prikljucek'].upper()   
          
        # v primeru da so izbrani vsi priljučki, prikažemo vse tipkovnice  
        if prikljucek1 != '':         
            
            context = {}   
            tipkovnice = Tipkovnica.objects.filter(prikljucek=prikljucek1)        
            context['tipkovnice'] = tipkovnice
            return render(request, 'kalkulator/tipkovnice.html', context)
         
    context = {}
    tipkovnice = Tipkovnica.objects.all()       
    context['tipkovnice'] = tipkovnice  
    
    return render(request, 'kalkulator/tipkovnice.html', context)
 
@login_required 
def graficne(request):    
    
    context = {}
    graficne = Graficna.objects.all()  
    
    # Če želimo samo grafične z izbranimi parametri iz dropdowna
    if request.method == 'GET'  and 'znamka' in request.GET:                   
          
        # izbran prikljucek v dropdown listu  
        znamka1 = request.GET['znamka'].upper()   
        povezava1 = request.GET['povezava'].upper() 
                
        if znamka1 != '':
            graficne = Graficna.objects.filter(znamka=znamka1) 
            
        if povezava1 != '':    
            graficne = graficne.filter(povezava=povezava1)   
                          
        context['graficne'] = graficne
        return render(request, 'kalkulator/graficne.html', context)
                  
    context['graficne'] = graficne  
    
    return render(request, 'kalkulator/graficne.html', context)   
 
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
    
    # Če želimo samo procesorje z izbranimi parametri iz dropdowna
    if request.method == 'GET'  and 'znamka' in request.GET:                   
          
        # izbran prikljucek v dropdown listu  
        znamka = request.GET['znamka'].upper()   
        model = request.GET['model'].upper()
        podnozje = request.GET['podnozje'] 
        opis = request.GET['opis'] 
                
        if znamka != '':
            maticne = Maticna.objects.filter(znamka=znamka)
         
        if model != '':   
            maticne = maticne.filter(model=model)         
            
        if podnozje != '':    
            maticne = maticne.filter(podnozje=podnozje)   
                          
        context['maticne'] = maticne
        return render(request, 'kalkulator/maticne.html', context)
                  
    context['maticne'] = maticne  
    
    return render(request, 'kalkulator/maticne.html', context)

@login_required 
def zvocne(request):    
    
    context = {}
    zvocne = Zvocna.objects.all()  
    
    # Če želimo samo zvocne z izbranimi parametri iz dropdowna
    if request.method == 'GET'  and 'znamka' in request.GET:                   
          
        # izbran prikljucek v dropdown listu  
        znamka = request.GET['znamka'].upper()   
        model = request.GET['model'].upper()
        prikljucek = request.GET['prikljucek'].upper()                 
         
        if znamka != '':
            zvocne = Zvocna.objects.filter(znamka=znamka)
         
        if model != '':   
            zvocne = zvocne.filter(model=model)         
            
        if prikljucek != '':    
            zvocne = zvocne.filter(prikljucek=prikljucek)   
                          
        context['zvocne'] = zvocne
        return render(request, 'kalkulator/zvocne.html', context)
                  
    context['zvocne'] = zvocne  
    
    return render(request, 'kalkulator/zvocne.html', context)
 
@login_required 
def napajalniki(request):    
    
    context = {}
    napajalniki = Napajalnik.objects.all()  
    
    # Če želimo samo zvocne z izbranimi parametri iz dropdowna
    if request.method == 'GET'  and 'znamka' in request.GET:                   
          
        # izbran prikljucek v dropdown listu  
        znamka = request.GET['znamka'].upper()   
        moc = request.GET['moc'].upper()                        
         
        if znamka != '':
            napajalniki = Napajalnik.objects.filter(znamka=znamka)
         
        if moc != '':   
            napajalniki = napajalniki.filter(moc=moc)         
                                
        context['napajalniki'] = napajalniki
        return render(request, 'kalkulator/napajalniki.html', context)
                  
    context['napajalniki'] = napajalniki  
    
    return render(request, 'kalkulator/napajalniki.html', context)    

@login_required 
def miske(request):    
    
    context = {}
    miske = Miska.objects.all()  
    
    # Če želimo samo zvocne z izbranimi parametri iz dropdowna
    if request.method == 'GET'  and 'znamka' in request.GET:                   
          
        # izbran prikljucek v dropdown listu  
        znamka = request.GET['znamka'].upper()   
        prikljucek = request.GET['prikljucek'].upper()
        povezava = request.GET['povezava'].upper()
         
        if znamka != '':
            miske = Miska.objects.filter(znamka=znamka)
         
        if prikljucek != '':   
            miske = miske.filter(prikljucek=prikljucek)         
         
        if povezava != '':   
            miske = miske.filter(povezava=povezava)         
         
         
        context['miske'] = miske
        return render(request, 'kalkulator/miske.html', context)
                  
    context['miske'] = miske  
    
    return render(request, 'kalkulator/miske.html', context)    
 
@login_required 
def diski(request):    
    
    context = {}
    diski = Disk.objects.all()  
    
    # Če želimo samo zvocne z izbranimi parametri iz dropdowna
    if request.method == 'GET'  and 'znamka' in request.GET:                   
          
        # izbran prikljucek v dropdown listu  
        znamka = request.GET['znamka'].upper()   
        prikljucek = request.GET['prikljucek'].upper()
        velikost = request.GET['velikost'].upper()
                 
        if znamka != '':
            diski = Disk.objects.filter(znamka=znamka)
         
        if prikljucek != '':   
            diski = diski.filter(prikljucek=prikljucek)         
         
        if velikost != '':   
            diski = diski.filter(velikost=velikost)         
         
         
        context['diski'] = diski
        return render(request, 'kalkulator/diski.html', context)
                  
    context['diski'] = diski  
    
    return render(request, 'kalkulator/diski.html', context)    
 
 
 


    
@login_required
def dodajTipkovnico(request):
    
    context = {}

    if request.method == 'GET'  and 'znamka' in request.GET:

        znamka = request.GET['znamka'].upper()
        prikljucek = request.GET['prikljucek'].upper()
        povezava = request.GET['povezava'].upper()
        kolicina = request.GET['kolicina']
                
        print(znamka)
        
        nova_tipkovnica = Tipkovnica(znamka=znamka, prikljucek=prikljucek, povezava=povezava, kolicina=kolicina)
        nova_tipkovnica.save()
            
    return render(request, 'kalkulator/dodajTipkovnico.html', context)    
    
@login_required
def dodajGraficno(request):
    
    context = {}

    if request.method == 'GET'  and 'znamka' in request.GET:

        znamka = request.GET['znamka'].upper()
        model = request.GET['model'].upper()
        pomnilnik = request.GET['pomnilnik']        
        povezava = request.GET['povezava'].upper()
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
def dodajMaticno(request):
    
    context = {}

    if request.method == 'GET'  and 'znamka' in request.GET:

        znamka = request.GET['znamka'].upper()
        model = request.GET['model'].upper()        
        podnozje = request.GET['podnozje'].upper()
        opis = request.GET['opis']
        kolicina = request.GET['kolicina']
        
        nova_maticna = Maticna(znamka=znamka, model=model, podnozje=podnozje, opis=opis, kolicina=kolicina)
        nova_maticna.save()
            
    return render(request, 'kalkulator/dodajMaticno.html', context)    
    
@login_required
def dodajZvocno(request):
    
    context = {}

    if request.method == 'GET'  and 'znamka' in request.GET:

        znamka = request.GET['znamka'].upper()
        model = request.GET['model'].upper()        
        prikljucek = request.GET['prikljucek'].upper()
        opis = request.GET['opis'].upper()
        kolicina = request.GET['kolicina']
        
        nova_zvocna = Zvocna(znamka=znamka, model=model, prikljucek=prikljucek, opis=opis, kolicina=kolicina)
        nova_zvocna.save()
            
    return render(request, 'kalkulator/dodajZvocno.html', context) 
 
@login_required
def dodajNapajalnik(request):
    
    context = {}

    if request.method == 'GET'  and 'znamka' in request.GET:

        znamka = request.GET['znamka'].upper()
        moc = request.GET['moc'].upper()      
        opis = request.GET['opis'].upper()
        kolicina = request.GET['kolicina']
        
        nov_napajalnik = Napajalnik(znamka=znamka, moc=moc, opis=opis, kolicina=kolicina)
        nov_napajalnik.save()
            
    return render(request, 'kalkulator/dodajNapajalnik.html', context) 
 
@login_required
def dodajMisko(request):
    
    context = {}

    if request.method == 'GET'  and 'znamka' in request.GET:

        znamka = request.GET['znamka'].upper()
        prikljucek = request.GET['prikljucek'].upper() 
        povezava = request.GET['povezava'].upper()       
        kolicina = request.GET['kolicina']
        
        nova_miska = Miska(znamka=znamka, prikljucek=prikljucek, povezava=povezava, kolicina=kolicina)
        nova_miska.save()
            
    return render(request, 'kalkulator/dodajMisko.html', context) 

@login_required
def dodajDisk(request):
    
    context = {}

    if request.method == 'GET'  and 'znamka' in request.GET:

        znamka = request.GET['znamka'].upper()
        prikljucek = request.GET['prikljucek'].upper() 
        velikost = request.GET['velikost'].upper()
        opis = request.GET['opis'].upper()        
        kolicina = request.GET['kolicina']
        
        nov_disk = Disk(znamka=znamka, prikljucek=prikljucek, velikost=velikost, opis=opis, kolicina=kolicina)
        nov_disk.save()
            
    return render(request, 'kalkulator/dodajDisk.html', context) 
     

 
   
        

  
  
  
  