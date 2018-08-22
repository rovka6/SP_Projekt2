from django.shortcuts import render
from .models import Racun, Vnos, Procesorji, Tipkovnice
from django.http import HttpResponse
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login
from kalkulator.models import Racun
from django.contrib.auth.decorators import login_required
from email.utils import parseaddr

import logging
logger = logging.getLogger(__name__)

def registracija(request):      
    return render(request, 'kalkulator/registracija.html')
  
def RegistracijaPodrobno(request):
    
    context = {}
    racuni = Racun.objects.all()        
    context['racuni'] = racuni  
    
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
    b = Racun.objects.create(ime="transakcijski racun", uporabnik=a, stanje=0 )
    b.save()
          
    racuni = Racun.objects.all()        
    context['racuni'] = racuni  
    
    login(request, a)
    
    context = {}
    racuni = Racun.objects.all()        
    context['racuni'] = racuni  

    return render(request, 'kalkulator/stanje.html', context)
 
@login_required 
def stanje(request):          
    context = {}
    racuni = Racun.objects.all()       
    context['racuni'] = racuni  
    
    return render(request, 'kalkulator/stanje.html', context)
    
@login_required 
def procesorji(request):          
    context = {}
    procesorji = Procesorji.objects.all()       
    context['procesorji'] = procesorji  
    
    return render(request, 'kalkulator/procesorji.html', context)
 
@login_required 
def tipkovnice(request):          
    context = {}
    tipkovnice = Tipkovnice.objects.all()       
    context['tipkovnice'] = tipkovnice  
    
    return render(request, 'kalkulator/tipkovnice.html', context)
    
    
@login_required     
def dodajRacun(request):
            
    context = {}   
    racuni = Racun.objects.all() 
    context['racuni'] = racuni       
    
    ime_racuna = request.GET['racun1']
      
    # preveri če so vsa polja vnešena  
    if ime_racuna == "":
       context['warning'] = "Ime racuna ne more biti prazno!"
       return render(request, 'kalkulator/stanje.html', context)
    
    obstojec_racun = Racun.objects.filter(uporabnik=request.user, ime=ime_racuna)
    
    if not obstojec_racun:          
        nov_racun = Racun(ime=ime_racuna, uporabnik=request.user, stanje=0)
        nov_racun.save()    
        context['racuni'] = Racun.objects.all()         
        return render(request, 'kalkulator/stanje.html', context)
     
    context['warning'] = "Racun z enakim imenom že obstaja!"
    
    return render(request, 'kalkulator/stanje.html', context)

@login_required     
def odstraniRacun(request):
    
    context = {}    
    context['racuni'] = Racun.objects.all()
    
    if request.method == 'GET' and 'racun' in request.GET:
        ime_racuna = request.GET['racun']
        nov_racun = Racun.objects.get(uporabnik=request.user, ime=ime_racuna)
        nov_racun.delete()
        return render(request, 'kalkulator/stanje.html', context)
    
    context['warning'] = "Nimate nobenega računa!"
    return render(request, 'kalkulator/stanje.html', context)
    
@login_required     
def StanjePodrobno(request):    
    context = {}     
    racuni = Racun.objects.all()    
    context['racuni'] = racuni   
   
    if request.method == 'GET' and 'dropdown' in request.GET:
        answer = request.GET['dropdown']        
        racun1 = Racun.objects.get(ime=answer, uporabnik=request.user)
        vnosi = Vnos.objects.filter(racun=racun1)
        context['vnosi'] = vnosi  
  
        sum = 0;    
        for vnos in vnosi:
             sum = sum + vnos.znesek
        context['vsota'] = sum
  
        return render(request, 'kalkulator/StanjePodrobno.html', context)
        
    context['warning'] = "Nimate nobenega računa!"            
    
    return render(request, 'kalkulator/Stanje.html', context)
    
@login_required         
def vpisiPrihodek(request):
    context = {}     
    racuni = Racun.objects.all()        
    context['racuni'] = racuni  
    return render(request, 'kalkulator/vpisiPrihodek.html', context)

@login_required     
def vpisiPrihodekPodrobno(request):

    context = {}
    racuni = Racun.objects.all()        
    context['racuni'] = racuni  

    if not 'racun' in request.GET:
        context['warning'] = "Nimate nobenega računa! Dodajte ga v zavihku stanje"
        return render(request, 'kalkulator/vpisiPrihodek.html', context) 

    kategorija = request.GET['kategorija'] 
    racun = request.GET['racun']
    znesek = request.GET['znesek']
    podrobnosti = request.GET['podrobnosti']   
    
    if not str(znesek).replace('.','',1).isdigit():        
        context['warning'] = "Znesek mora biti število!"
        return render(request, 'kalkulator/vpisiPrihodek.html', context)           
    
    racun = Racun.objects.get(uporabnik=request.user, ime=racun)
    
    a = Vnos(kategorija=kategorija, znesek=znesek, podrobnosti=podrobnosti, vrsta="prihodek", racun=racun)  
    a.save()          
    
    return render(request, 'kalkulator/vpisiPrihodekPodrobno.html', context)    
    
@login_required     
def vpisiOdhodek(request):
    context = {}     
    racuni = Racun.objects.all()        
    context['racuni'] = racuni  
    return render(request, 'kalkulator/vpisiOdhodek.html', context)

@login_required     
def vpisiOdhodekPodrobno(request):

    context = {}
    racuni = Racun.objects.all()        
    context['racuni'] = racuni
    
    if not 'racun' in request.GET:
        context['warning'] = "Nimate nobenega računa! Dodajte ga v zavihku stanje"
        return render(request, 'kalkulator/vpisiOdhodek.html', context) 
        
    kategorija = request.GET['kategorija'] 
    racun = request.GET['racun']
    znesek = request.GET['znesek']
    podrobnosti = request.GET['podrobnosti']
    
    if not str(znesek).replace('.','',1).isdigit():       
        context['warning'] = "Znesek mora biti število!"
        return render(request, 'kalkulator/vpisiPrihodek.html', context)
            
    znesek = int(znesek) * -1
    
    racun = Racun.objects.get(uporabnik=request.user, ime=racun)
    
    a = Vnos(kategorija=kategorija, znesek=znesek, podrobnosti=podrobnosti, vrsta="odhodek", racun=racun)   
    a.save()                  
    
    return render(request, 'kalkulator/vpisiOdhodekPodrobno.html', context)
    
@login_required     
def porocila(request):
    context = {}    
    racuni = Racun.objects.all()        
    context['racuni'] = racuni       
        
    return render(request, 'kalkulator/porocila.html', context)
    
@login_required     
def PorocilaPodrobno(request):
    context = {}
    racuni = Racun.objects.all()        
    context['racuni'] = racuni  
        
    if not 'racun' in request.GET:
        context['warning'] = "Nimate nobenega računa! Dodajte ga v zavihku stanje"
        return render(request, 'kalkulator/porocila.html', context) 
        
    kategorija = request.GET['kategorija'] 
    racun = request.GET['racun']                
            
    racun = Racun.objects.get(uporabnik=request.user, ime=racun)
    
    vnosi = Vnos.objects.filter(racun=racun, kategorija=kategorija)
    
    context['vnosi'] = vnosi     
    
    sum = 0;    
    for vnos in vnosi:
        sum = sum + vnos.znesek
    
    context['vsota'] = sum      
    
    return render(request, 'kalkulator/porocilaPodrobno.html', context)
          
@login_required            
def administracija(request):
    
    context = {}    
    
    if request.user.groups.filter(name='user').exists():       
       racuni = Racun.objects.all()        
       context['racuni'] = racuni 
       context['warning'] = "Nimate ustreznih pravic za dostop do administracije!!"
       return render(request, 'kalkulator/stanje.html', context)
        
    uporabniki = User.objects.all()
    context['uporabniki'] = uporabniki           
                                        
    return render(request, 'kalkulator/administracija.html', context)
    
@login_required      
def AdministracijaPodrobno(request):

    context = {}  

    if request.user.groups.filter(name='user').exists():       
       racuni = Racun.objects.all()        
       context['racuni'] = racuni 
       context['warning'] = "Nimate ustreznih pravic za dostop do administracije!!"
       return render(request, 'kalkulator/stanje.html', context)
    
    
    if not 'dropdown' in request.GET:
        context['warning'] = "Ni uporabnikov!"
        return render(request, 'kalkulator/administracija.html', context)         
           
    ime_uporabnika = request.GET['dropdown']     
    uporabnik = User.objects.get(username=ime_uporabnika)
    uporabnik.delete()  
  
    uporabniki = User.objects.all()
    context['uporabniki'] = uporabniki 
    
    context['warning'] = "uporabnik izbrisan!"
  
    return render(request, 'kalkulator/administracija.html', context)
  
  
  
  