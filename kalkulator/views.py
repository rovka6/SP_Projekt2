from django.shortcuts import render
from .models import Graficna, Tipkovnica, Procesor, Maticna
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
        prikljucek1 = request.GET['prikljucek']   
          
        # v primeru da so izbrani vsi priljučki, prikažemo vse tipkovnice  
        if prikljucek1 != 'Vsi':         
            
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
        znamka1 = request.GET['znamka']   
        povezava1 = request.GET['povezava'] 
                
        if znamka1 != 'Vsi':
            graficne = Graficna.objects.filter(znamka=znamka1) 
            
        if povezava1 != 'Vsi':    
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
        znamka = request.GET['znamka']   
        model = request.GET['model']
        podnozje = request.GET['podnozje'] 
                
        if znamka != 'Vsi':
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
        znamka = request.GET['znamka']   
        model = request.GET['model']
        podnozje = request.GET['podnozje'] 
        opis = request.GET['podnozje'] 
                
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
def dodajTipkovnico(request):
    
    context = {}

    if request.method == 'GET'  and 'znamka' in request.GET:

        znamka = request.GET['znamka']
        prikljucek = request.GET['prikljucek']
        povezava = request.GET['povezava']
        kolicina = request.GET['kolicina']
        
        nova_tipkovnica = Tipkovnica(znamka=znamka, prikljucek=prikljucek, povezava=povezava, kolicina=kolicina)
        nova_tipkovnica.save()
            
    return render(request, 'kalkulator/dodajTipkovnico.html', context)    
    
@login_required
def dodajGraficno(request):
    
    context = {}

    if request.method == 'GET'  and 'znamka' in request.GET:

        znamka = request.GET['znamka']
        model = request.GET['model']
        pomnilnik = request.GET['pomnilnik']        
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

        znamka = request.GET['znamka']
        model = request.GET['model']        
        podnozje = request.GET['podnozje']
        kolicina = request.GET['kolicina']
        
        nov_procesor = Procesor(znamka=znamka, model=model, podnozje=podnozje, kolicina=kolicina)
        nov_procesor.save()
            
    return render(request, 'kalkulator/dodajProcesor.html', context)    

@login_required
def dodajMaticno(request):
    
    context = {}

    if request.method == 'GET'  and 'znamka' in request.GET:

        znamka = request.GET['znamka']
        model = request.GET['model']        
        podnozje = request.GET['podnozje']
        opis = request.GET['opis']
        kolicina = request.GET['kolicina']
        
        nova_maticna = Maticna(znamka=znamka, model=model, podnozje=podnozje, opis=opis, kolicina=kolicina)
        nova_maticna.save()
            
    return render(request, 'kalkulator/dodajMaticno.html', context)    
    

 


 
   
        

  
  
  
  