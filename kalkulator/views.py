from django.shortcuts import render
from .models import Graficna, Procesor, Maticna, Napajalnik,  Disk, Ram, Razsiritvena, Zaslon, Kabel, Input,  Kategorija, Tiskalnik, Periferija, Drugo
from django.http import HttpResponse
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from email.utils import parseaddr
from django.db.models.functions import Length
from django.db.models.functions import Lower
from .form_config.forms import ImageUploadForm
from django.shortcuts import redirect

import logging
logger = logging.getLogger(__name__)   

def redirect_view(request):
    response = redirect('/redirect-success/')
    return response   
    
def rezerviraj(request, idKomponente, vrstaKomponente):           
     
    #request.SESSION_EXPIRE_AT_BROWSER_CLOSE = True  
    #request.session.set_expiry(1)  
    #context['idSeje'] = request.session.session_key 
     
    if(request.session.session_key == None):
        request.session.create
      
    if 'idKomponent' not in request.session:
        
        idKomponent = []
        vrstaKomponent = []
        #idKomponent.append(request.POST['idKomponente'])
        #vrstaKomponent.append(request.POST['vrstaKomponente'])
        idKomponent.append(idKomponente)
        vrstaKomponent.append(vrstaKomponente)
        request.session['idKomponent'] = idKomponent
        request.session['vrstaKomponent'] = vrstaKomponent                 
    else:
                   
        idKomponent = request.session['idKomponent']
        vrstaKomponent = request.session['vrstaKomponent']
        #idKomponent.append(request.POST['idKomponente'])
        #vrstaKomponent.append(request.POST['vrstaKomponente'])
        idKomponent.append(idKomponente)
        vrstaKomponent.append(vrstaKomponente)               
        request.session['idKomponent'] = idKomponent
        request.session['vrstaKomponent'] = vrstaKomponent        
                  
       
        
    return redirect(vrstaKomponente)   
 
def odstrani(request, idKomponente):

    idKomponent = request.session['idKomponent']    
    vrstaKomponent = request.session['vrstaKomponent']
    stElementov = len(idKomponent)
    
    for i in range(0, stElementov): 
        if idKomponent[i] == idKomponente:
            idKomponent[i] = '-1'
            vrstaKomponent[i] = '-1'
            break
    
    idKomponent.remove('-1') 
    vrstaKomponent.remove('-1') 

    request.session['idKomponent'] = idKomponent
    request.session['vrstaKomponent'] = vrstaKomponent    
        
    return redirect(kosarica) 

def potrditevNarocila(request):
    context = {}
    ime = request.POST['ime_in_priimek']
    stevilka = request.POST['stevilka']
    email = request.POST['email']
    
    idKomponent = request.session['idKomponent']    
    vrstaKomponent = request.session['vrstaKomponent']
	
    tekst = "Pozdravljeni! \n"  + " Sporočamo vam, da ste preko naše spletne strani upešno rezervirali naslednje komponente: \n" + "\n"
    
    for id, vrsta in zip(idKomponent, vrstaKomponent):
        tekst = tekst +  str(id) + "- " + str(vrsta) + "<br>" 
    
    from django.core.mail import send_mail  
    send_mail('Naročilo potrjeno',
    tekst,  
    'kristjan.bleiweis@gmail.com', #FROM
    [email],  #TO
    fail_silently=False,)
       
    context['ime_in_priimek'] = ime
    context['email'] = email
    context['idKomponent'] = idKomponent
    context['vrstaKomponent'] = vrstaKomponent
	
	
    return render(request, 'kalkulator/potrditevNarocila.html', context)
	
def kosarica(request):
    
    context = {}
    list = []
    context['opozorilo'] = ''
    
    if 'idKomponent' not in request.session:
        
        context['opozorilo'] = 'Kosarica je prazna'   
        return render(request, 'kalkulator/kosarica.html', context)
        
        
        
    
    idKomponent = request.session['idKomponent']    
    vrstaKomponent = request.session['vrstaKomponent']
        
    list = []
    stElementov = len(idKomponent)
    
    if stElementov == 0:        
        
        context['opozorilo'] = 'Kosarica je prazna'   
        return render(request, 'kalkulator/kosarica.html', context)
    
    
    for i in range(0, stElementov):           
    
        if vrstaKomponent[i] == 'graficne':
            list.append(Graficna.objects.get(id=idKomponent[i]))
         
        elif vrstaKomponent[i] == 'inputi':
            list.append(Input.objects.get(id=idKomponent[i]))
            
        elif vrstaKomponent[i] == 'diski':
            list.append(Disk.objects.get(id=idKomponent[i]))
            
        elif vrstaKomponent[i] == 'rami':
            list.append(Ram.objects.get(id=idKomponent[i]))
            
        elif vrstaKomponent[i] == 'razsiritvene':
            list.append(Razsiritvena.objects.get(id=idKomponent[i]))
            
        elif vrstaKomponent[i] == 'maticne':
            list.append(Maticna.objects.get(id=idKomponent[i]))
            
            
        elif vrstaKomponent[i] == 'zasloni':
            list.append(Zaslon.objects.get(id=idKomponent[i]))
            
            
        elif vrstaKomponent[i] == 'napajalniki':
            list.append(Napajalnik.objects.get(id=idKomponent[i]))

        elif vrstaKomponent[i] == 'kabli':
            list.append(Kabel.objects.get(id=idKomponent[i]))

        elif vrstaKomponent[i] == 'procesorji':
            list.append(Procesor.objects.get(id=idKomponent[i]))    
            
            
        elif vrstaKomponent[i] == 'drugo':
            list.append(Drugo.objects.get(id=idKomponent[i]))             
            
        else: 
            print('neznana komponenta')
            print(vrstaKomponent[i])        
            print('.')   
       
    context['komponente'] = list           
    
    return render(request, 'kalkulator/kosarica.html', context)
                  
  
def add(request, vrsta, id):     

    if vrsta == 'tiskalnik':
        tiskalnik = Tiskalnik.objects.get(pk=id)                
        tiskalnik.kolicina = (int(tiskalnik.kolicina) + 1)
        tiskalnik.save()
               
        return redirect('tiskalniki')

    if vrsta == 'drugo':
        drugo = Drugo.objects.get(pk=id)                
        drugo.kolicina = (int(drugo.kolicina) + 1)
        drugo.save()
               
        return redirect('drugo')
    
        
    if vrsta == 'graficna':
        graficna = Graficna.objects.get(pk=id)                
        graficna.kolicina = (int(graficna.kolicina) + 1)
        graficna.save()
               
        return redirect('graficne')
    
    if vrsta == 'input':
        input = Input.objects.get(pk=id)
        input.kolicina = (int(input.kolicina) + 1)
        input.save()
        
        return redirect('inputi')
    
    if vrsta == 'disk':
        disk = Disk.objects.get(pk=id)
        disk.kolicina = (int(disk.kolicina) + 1)
        disk.save()
     
        return redirect('diski')
        
    if vrsta == 'ram':
        ram = Ram.objects.get(pk=id)
        ram.kolicina = (int(ram.kolicina) + 1)
        ram.save()
      
        return redirect('rami')
        
    if vrsta == 'razsiritvena':
        razsiritvena = Razsiritvena.objects.get(pk=id)
        razsiritvena.kolicina = (int(razsiritvena.kolicina) + 1)
        razsiritvena.save()
        
        return redirect('razsiritvene')
        
    if vrsta == 'maticna':
        maticna = Maticna.objects.get(pk=id)
        maticna.kolicina = (int(maticna.kolicina) + 1)
        maticna.save()
        
        return redirect('maticne')
        
    if vrsta == 'zaslon':
        zaslon = Zaslon.objects.get(pk=id)
        zaslon.kolicina = (int(zaslon.kolicina) + 1)
        zaslon.save()
           
        return redirect('zasloni')
        
    if vrsta == 'napajalnik':
        napajalnik = Napajalnik.objects.get(pk=id)
        napajalnik.kolicina = (int(napajalnik.kolicina) + 1)
        napajalnik.save()
        
        return redirect('napajalniki')
    
    if vrsta == 'kabel':
        kabel = Kabel.objects.get(pk=id)
        kabel.kolicina = (int(kabel.kolicina) + 1)
        kabel.save()
       
        return redirect('kabli')
    
    if vrsta == 'adapter':
        adapter = Adapter.objects.get(pk=id)
        adapter.kolicina = (int(adapter.kolicina) + 1)
        adapter.save()
       
        return redirect('adapterji')
    
    
    if vrsta == 'procesor':
        procesor = Procesor.objects.get(pk=id)
        procesor.kolicina = (int(procesor.kolicina) + 1)
        procesor.save()
        
        return redirect('procesorji')
       
    return redirect('main')

def delete(request, vrsta, id):     

    if vrsta == 'tiskalnik':
        tiskalnik = Tiskalnik.objects.get(pk=id)                
        tiskalnik.kolicina = (int(tiskalnik.kolicina) - 1)
        tiskalnik.save()
        if(int(tiskalnik.kolicina) == 0):
            tiskalnik.delete()
        
        return redirect('tiskalniki')

    if vrsta == 'drugo':
        drugo = Drugo.objects.get(pk=id)                
        drugo.kolicina = (int(drugo.kolicina) - 1)
        drugo.save()
        if(int(drugo.kolicina) == 0):
            drugo.delete()
        
        return redirect('drugo')    
               
        
    if vrsta == 'graficna':
        graficna = Graficna.objects.get(pk=id)                
        graficna.kolicina = (int(graficna.kolicina) - 1)
        graficna.save()
        if(int(graficna.kolicina) == 0):
            graficna.delete()
        
        return redirect('graficne')
    
    if vrsta == 'input':
        input = Input.objects.get(pk=id)
        input.kolicina = (int(input.kolicina) - 1)
        input.save()
        if(int(input.kolicina) == 0):
            input.delete()
        return redirect('inputi')
    
    if vrsta == 'disk':
        disk = Disk.objects.get(pk=id)
        disk.kolicina = (int(disk.kolicina) - 1)
        disk.save()
        if(int(disk.kolicina) == 0):
            disk.delete()
        return redirect('diski')
        
    if vrsta == 'ram':
        ram = Ram.objects.get(pk=id)
        ram.kolicina = (int(ram.kolicina) - 1)
        ram.save()
        if(int(ram.kolicina) == 0):
            ram.delete()
        return redirect('rami')
        
    if vrsta == 'razsiritvena':
        razsiritvena = Razsiritvena.objects.get(pk=id)
        razsiritvena.kolicina = (int(razsiritvena.kolicina) - 1)
        razsiritvena.save()
        if(int(razsiritvena.kolicina) == 0):
            razsiritvena.delete()
        return redirect('razsiritvene')
        
    if vrsta == 'maticna':
        maticna = Maticna.objects.get(pk=id)
        maticna.kolicina = (int(maticna.kolicina) - 1)
        maticna.save()
        if(int(maticna.kolicina) == 0):
            maticna.delete()    
        return redirect('maticne')
        
    if vrsta == 'zaslon':
        zaslon = Zaslon.objects.get(pk=id)
        zaslon.kolicina = (int(zaslon.kolicina) - 1)
        zaslon.save()
        if(int(zaslon.kolicina) == 0):
            zaslon.delete()     
        return redirect('zasloni')
        
    if vrsta == 'napajalnik':
        napajalnik = Napajalnik.objects.get(pk=id)
        napajalnik.kolicina = (int(napajalnik.kolicina) - 1)
        napajalnik.save()
        if(int(napajalnik.kolicina) == 0):
            napajalnik.delete()
        return redirect('napajalniki')
    
    if vrsta == 'kabel':
        kabel = Kabel.objects.get(pk=id)
        kabel.kolicina = (int(kabel.kolicina) - 1)
        kabel.save()
        if(int(kabel.kolicina) == 0):
            kabel.delete()
        return redirect('kabli')
    
    if vrsta == 'adapter':
        adapter = Adapter.objects.get(pk=id)
        adapter.kolicina = (int(adapter.kolicina) - 1)
        adapter.save()
        if(int(adapter.kolicina) == 0):
            adapter.delete()
        return redirect('adapterji')
    
    
    if vrsta == 'procesor':
        procesor = Procesor.objects.get(pk=id)
        procesor.kolicina = (int(procesor.kolicina) - 1)
        procesor.save()
        procesor.delete()
        if(int(procesor.kolicina) == 0):
            procesor.delete()
        return redirect('procesorji')
       
    return redirect('main')
    
def main(request):          
    context = {}
    
    
          
         
                   
    return render(request, 'kalkulator/main.html', context)
 
def vrsteNapajalnikov(request):          
    context = {}
    
    if request.method == 'POST'  and 'podkategorija' in request.POST:  
    
        podkategorija = request.POST['podkategorija']
        nova_kategorija = Kategorija(kategorija='napajalnik', podkategorija=podkategorija)
                
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():           
            nova_kategorija.image = form.cleaned_data['image']
          
        if podkategorija == '':
            return redirect('vrsteNapajalnikov')
          
        nova_kategorija.save()        
    
    kategorije = Kategorija.objects.filter(kategorija='napajalnik')
    context['kategorije'] = kategorije
    
            
        
    return render(request, 'kalkulator/vrsteNapajalnikov.html', context)

def vrsteDiskov(request):          
    context = {}         

    if request.method == 'POST'  and 'podkategorija' in request.POST:  
    
        podkategorija = request.POST['podkategorija']
        nova_kategorija = Kategorija(kategorija='disk', podkategorija=podkategorija)
                
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():           
            nova_kategorija.image = form.cleaned_data['image']
        
        if podkategorija == '':
            return redirect('vrsteDiskov')
        
        nova_kategorija.save()        
    
    kategorije = Kategorija.objects.filter(kategorija='disk')
    context['kategorije'] = kategorije
            
    return render(request, 'kalkulator/vrsteDiskov.html', context)          

def vrsteGraficnih(request):          
    context = {}         

    if request.method == 'POST'  and 'podkategorija' in request.POST:  
    
        podkategorija = request.POST['podkategorija']
        nova_kategorija = Kategorija(kategorija='graficna', podkategorija=podkategorija)
                
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():           
            nova_kategorija.image = form.cleaned_data['image']
          
        if podkategorija == '':
            return redirect('vrsteGraficnih')
          
        nova_kategorija.save()        
    
    kategorije = Kategorija.objects.filter(kategorija='graficna')
    context['kategorije'] = kategorije
            
    return render(request, 'kalkulator/vrsteGraficnih.html', context)          
  
def vrsteInputov(request):          

    context = {}
     
    if request.method == 'POST'  and 'podkategorija' in request.POST:  
    
        podkategorija = request.POST['podkategorija']
        nova_kategorija = Kategorija(kategorija='input', podkategorija=podkategorija)
                
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():           
            nova_kategorija.image = form.cleaned_data['image']
         
        if podkategorija == '':
            return redirect('vrsteInputov')
         
        nova_kategorija.save()        
    
    kategorije = Kategorija.objects.filter(kategorija='input')
    context['kategorije'] = kategorije
     

            

        
    return render(request, 'kalkulator/vrsteInputov.html', context)    
    
def vrsteRazsiritvenih(request):          
    context = {}         

    if request.method == 'POST'  and 'podkategorija' in request.POST:  
    
        podkategorija = request.POST['podkategorija']
        nova_kategorija = Kategorija(kategorija='razsiritvena', podkategorija=podkategorija)
                
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():           
            nova_kategorija.image = form.cleaned_data['image']
         
        if podkategorija == '':
            return redirect('vrsteRazsiritvenih')
         
        nova_kategorija.save()        
    
    kategorije = Kategorija.objects.filter(kategorija='razsiritvena')
    context['kategorije'] = kategorije
            
    return render(request, 'kalkulator/vrsteRazsiritvenih.html', context)          

def vrsteDrugo(request):          
    context = {}         

    if request.method == 'POST'  and 'podkategorija' in request.POST:  
    
        podkategorija = request.POST['podkategorija']
        nova_kategorija = Kategorija(kategorija='drugo', podkategorija=podkategorija)
                
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():           
            nova_kategorija.image = form.cleaned_data['image']
         
        if podkategorija == '':
            return redirect('vrsteDrugo')
         
        nova_kategorija.save()        
    
    kategorije = Kategorija.objects.filter(kategorija='drugo')
    context['kategorije'] = kategorije
            
    return render(request, 'kalkulator/vrsteDrugo.html', context)          

def vrstePeriferije(request):          
    context = {}         

    if request.method == 'POST'  and 'podkategorija' in request.POST:  
    
        podkategorija = request.POST['podkategorija']
        nova_kategorija = Kategorija(kategorija='periferija', podkategorija=podkategorija)
                
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():           
            nova_kategorija.image = form.cleaned_data['image']
         
        if podkategorija == '':
            return redirect('vrstePeriferija')
         
        nova_kategorija.save()        
    
    kategorije = Kategorija.objects.filter(kategorija='periferija')
    context['kategorije'] = kategorije
            
    return render(request, 'kalkulator/vrstePeriferije.html', context)          
 
    
  
def vrsteTiskalnikov(request):          
    context = {}         

    if request.method == 'POST'  and 'podkategorija' in request.POST:  
    
        podkategorija = request.POST['podkategorija']
        nova_kategorija = Kategorija(kategorija='tiskalnik', podkategorija=podkategorija)
                
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():           
            nova_kategorija.image = form.cleaned_data['image']
        
        if podkategorija == '':
            return redirect('vrsteTiskalnikov')

        
        nova_kategorija.save()        
    
    kategorije = Kategorija.objects.filter(kategorija='tiskalnik')
    context['kategorije'] = kategorije
            
    return render(request, 'kalkulator/vrsteTiskalnikov.html', context)          
    
def vrsteKablov(request):          
    context = {}         

    if request.method == 'POST'  and 'podkategorija' in request.POST:  
    
        podkategorija = request.POST['podkategorija']
        nova_kategorija = Kategorija(kategorija='kabel', podkategorija=podkategorija)
                
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():           
            nova_kategorija.image = form.cleaned_data['image']
        
        if podkategorija == '':
            return redirect('vrsteKablov')
        
        nova_kategorija.save()        
    
    kategorije = Kategorija.objects.filter(kategorija='kabel')
    context['kategorije'] = kategorije
            
    return render(request, 'kalkulator/vrsteKablov.html', context) 
    
def vrsteRama(request):          
    context = {}         

    if request.method == 'POST'  and 'podkategorija' in request.POST:  
    
        podkategorija = request.POST['podkategorija']
        nova_kategorija = Kategorija(kategorija='ram', podkategorija=podkategorija)
                
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():           
            nova_kategorija.image = form.cleaned_data['image']
        
        if podkategorija == '':
            return redirect('vrsteRama')
        
        nova_kategorija.save()        
    
    kategorije = Kategorija.objects.filter(kategorija='ram')
    context['kategorije'] = kategorije
            
    return render(request, 'kalkulator/vrsteRama.html', context)          
 
def vrsteMaticnih(request):          
    context = {}         

    if request.method == 'POST'  and 'podkategorija' in request.POST:  
    
        podkategorija = request.POST['podkategorija']
        nova_kategorija = Kategorija(kategorija='maticna', podkategorija=podkategorija)
                
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():           
            nova_kategorija.image = form.cleaned_data['image']
        
        if podkategorija == '':
            return redirect('vrsteMaticnih')
        
        nova_kategorija.save()        
    
    kategorije = Kategorija.objects.filter(kategorija='maticna')
    context['kategorije'] = kategorije
            
    return render(request, 'kalkulator/vrsteMaticnih.html', context)          

def vrsteProcesorjev(request):          
    context = {}         

    if request.method == 'POST'  and 'podkategorija' in request.POST:  
    
        podkategorija = request.POST['podkategorija']
        nova_kategorija = Kategorija(kategorija='procesor', podkategorija=podkategorija)
                
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():           
            nova_kategorija.image = form.cleaned_data['image']
        
        if podkategorija == '':
            return redirect('vrsteProcesorjev')
        
        nova_kategorija.save()        
    
    kategorije = Kategorija.objects.filter(kategorija='procesor')
    context['kategorije'] = kategorije
            
    return render(request, 'kalkulator/vrsteProcesorjev.html', context)          
  
def zasloni(request):   

    context = {} 
    zasloni = Zaslon.objects.all() 
        
    # S temi parametri napolnimo dropdown-e v htmlju, torej npr. seznam vseh znamk
    znamke = Zaslon.objects.values('znamka').distinct().order_by(Lower('znamka')).values_list('znamka', flat=True)
    velikosti = Zaslon.objects.values('velikost').distinct().order_by(Lower('velikost')).values_list('velikost', flat=True)
    inputi = Zaslon.objects.values('input').distinct().order_by(Lower('input')).values_list('input', flat=True)
    context['znamke'] = znamke 
    context['velikosti'] = convertToInteger(velikosti)
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
    
    # napolnimo dropdown samo s tistimi podkategorijami, ki smo jih prej dodali
    vodila = Kategorija.objects.values('podkategorija').order_by(Lower('podkategorija')).values_list('podkategorija', flat=True)
    vodila = vodila.filter(kategorija='graficna')
    context['vodila'] = vodila
    
    # S temi parametri napolnimo dropdown-e v htmlju, torej npr. seznam vseh znamk
    znamke = Graficna.objects.values('znamka').distinct().order_by(Lower('znamka')).values_list('znamka', flat=True)
    vodilo = Graficna.objects.values('vodilo').distinct().order_by(Lower('vodilo')).values_list('vodilo', flat=True)
    pomnilniki = Graficna.objects.values('pomnilnik').distinct().order_by('pomnilnik').values_list('pomnilnik', flat=True)
 
    context['znamke'] = znamke
    context['vodilo'] = vodilo
    context['pomnilniki'] = convertToInteger(pomnilniki)
      
      
    # Če želimo samo grafične z izbranimi parametri iz dropdowna
    if request.method == 'GET'  and 'znamka' in request.GET:   
                 
        # izbran prikljucek v dropdown listu  
        znamka = request.GET['znamka']   
        vodilo = request.GET['vodilo'] 
        pomnilnik = request.GET['pomnilnik']              
         
        
         
        if znamka != 'Vsi':            
            graficne = graficne.filter(znamka=znamka) 
            
        if vodilo != 'Vsi':    
            graficne = graficne.filter(vodilo=vodilo)

        if pomnilnik != 'Vsi':    
            graficne = graficne.filter(pomnilnik=pomnilnik)          
                          
        context['graficne'] = graficne
        return render(request, 'kalkulator/graficne.html', context)
    
    izbrani = request.GET.get('izbrani', False)
    
    
    if izbrani != False:
        context['izbrani'] = izbrani      
        graficne = graficne.filter(vodilo=izbrani) 
 
        
    
    context['izbrani'] = izbrani         
    context['graficne'] = graficne  
    
    return render(request, 'kalkulator/graficne.html', context)   
 
def rami(request):    
    
    context = {}
    rami = Ram.objects.all() 

    # S temi parametri napolnimo dropdown-e v htmlju, torej npr. seznam vseh znamk
    znamke = Ram.objects.values('znamka').distinct().order_by(Lower('znamka')).values_list('znamka', flat=True)
    #vrste = Ram.objects.values('vrsta').distinct().order_by(Lower('vrsta')).values_list('vrsta', flat=True)
    velikosti = Ram.objects.values('velikost').distinct().order_by(Lower('velikost')).values_list('velikost', flat=True)
    context['znamke'] = znamke
    #context['vrste'] = vrste
    context['velikosti'] = convertToInteger(velikosti)  

    # napolnimo samo s tistimi podkategorijami, ki smo jih prej dodali
    vrste = Kategorija.objects.values('podkategorija').order_by(Lower('podkategorija')).values_list('podkategorija', flat=True)
    vrste = vrste.filter(kategorija='ram')
    context['vrste'] = vrste
    
      
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
      
    izbrani = request.GET.get('izbrani', False)
    
    if izbrani != False:
        rami = rami.filter(vrsta=izbrani)          
        
        
    context['izbrani'] = izbrani  
    context['rami'] = rami  
           
    
    
    return render(request, 'kalkulator/rami.html', context)   
 
def procesorji(request):    
    
    context = {}
    procesorji = Procesor.objects.all()  
    
    # S temi parametri napolnimo dropdown-e v htmlju, torej npr. seznam vseh znamk
    znamke = Procesor.objects.values('znamka').distinct().order_by(Lower('znamka')).values_list('znamka', flat=True)
    #podnozja = Procesor.objects.values('podnozje').distinct().order_by(Lower('podnozje')).values_list('podnozje', flat=True)    
    context['znamke'] = znamke 
    #context['podnozja'] = podnozja
   
    izbrani = request.GET.get('izbrani', False)
    context['izbrani'] = izbrani
    
    if izbrani != False:
        procesorji = procesorji.filter(podnozje=izbrani)

    # napolnimo samo s tistimi podkategorijami, ki smo jih prej dodali
    podnozja = Kategorija.objects.values('podkategorija').order_by(Lower('podkategorija')).values_list('podkategorija', flat=True)
    podnozja = podnozja.filter(kategorija='procesor')
    context['podnozja'] = podnozja
    
    
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
            
        if podnozje != 'Vsi':    
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
    #podnozja = Maticna.objects.values('podnozje').distinct().order_by(Lower('podnozje')).values_list('podnozje', flat=True) 
    rami = Maticna.objects.values('ram').distinct().order_by(Lower('ram')).values_list('ram', flat=True)
    graficne = Maticna.objects.values('graficna').distinct().order_by(Lower('graficna')).values_list('graficna', flat=True)    
    context['znamke'] = znamke 
    #context['podnozja'] = podnozja   
    context['rami'] = rami
    context['graficne'] = graficne  

    izbrani = request.GET.get('izbrani', False)
    context['izbrani'] = izbrani
    
    if izbrani != False:
        maticne = maticne.filter(podnozje=izbrani)

    # napolnimo samo s tistimi podkategorijami, ki smo jih prej dodali
    podnozja = Kategorija.objects.values('podkategorija').order_by(Lower('podkategorija')).values_list('podkategorija', flat=True)
    podnozja = podnozja.filter(kategorija='maticna')
    context['podnozja'] = podnozja      
    
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
    znamke = Napajalnik.objects.values('znamka').distinct().order_by(Lower('znamka')).values_list('znamka', flat=True)
    moci = Napajalnik.objects.values('moc').distinct().order_by(Lower('moc')).values_list('moc', flat=True)  
    voltaze = Napajalnik.objects.values('voltaza').distinct().order_by(Lower('voltaza')).values_list('voltaza', flat=True)
    amperaze = Napajalnik.objects.values('amperaza').distinct().order_by(Lower('amperaza')).values_list('amperaza', flat=True)    
    context['znamke'] = znamke 
    context['moci'] = convertToInteger(moci) 
    context['voltaze'] = convertToInteger(voltaze)
    context['amperaze'] = convertToInteger(amperaze)
    
    
    izbrani = request.GET.get('izbrani', False)
    
    if izbrani != False:
        napajalniki = napajalniki.filter(vrsta=izbrani)
    
    # napolnimo samo s tistimi podkategorijami, ki smo jih prej dodali
    vrste = Kategorija.objects.values('podkategorija').order_by(Lower('podkategorija')).values_list('podkategorija', flat=True)
    vrste = vrste.filter(kategorija='napajalnik')
    context['vrste'] = vrste       
    
    context['izbrani'] = izbrani 
    
   
    
    
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
            napajalniki = Napajalnik.objects.filter(moc=moc)        
        voltaza = request.GET['voltaza']
        if voltaza != 'Vsi':
            napajalniki = Napajalnik.objects.filter(voltaza=voltaza) 
        amperaza = request.GET['amperaza']
        if amperaza != 'Vsi':
            napajalniki = Napajalnik.objects.filter(amperaza=amperaza)         
                                                   
        context['napajalniki'] = napajalniki
        return render(request, 'kalkulator/napajalniki.html', context)
                  
    context['napajalniki'] = napajalniki  
    
    return render(request, 'kalkulator/napajalniki.html', context)    
 
def kabli(request):    
    
    context = {}
    kabli = Kabel.objects.all() 

    # S temi parametri napolnimo dropdown-e v htmlju, torej npr. seznam vseh znamk
    #vrste = Kabel.objects.values('vrsta').distinct().order_by(Lower('vrsta')).values_list('vrsta', flat=True)    
    #context['vrste'] = vrste 
    
    izbrani = request.GET.get('izbrani', False)
    context['izbrani'] = izbrani
    
    if izbrani != False:
        kabli = kabli.filter(vrsta=izbrani)

    # napolnimo samo s tistimi podkategorijami, ki smo jih prej dodali
    vrste = Kategorija.objects.values('podkategorija').order_by(Lower('podkategorija')).values_list('podkategorija', flat=True)
    vrste = vrste.filter(kategorija='kabel')
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
    
    # napolnimo samo s tistimi podkategorijami, ki smo jih prej dodali
    povezave = Kategorija.objects.values('podkategorija').order_by(Lower('podkategorija')).values_list('podkategorija', flat=True)
    povezave = povezave.filter(kategorija='input')
    context['povezave'] = povezave
    
        
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
    
    izbrani = request.GET.get('izbrani', False)
    
    if izbrani != False:
        context['izbrani'] = izbrani
        inputi = inputi.filter(povezava=izbrani)
     
    context['inputi'] = inputi
    
    
    return render(request, 'kalkulator/inputi.html', context)    

def tiskalniki(request):          
   
    context = {}      
            
    # napolnimo dropdown samo s tistimi podkategorijami, ki smo jih prej dodali
    vrste = Kategorija.objects.values('podkategorija').order_by(Lower('podkategorija')).values_list('podkategorija', flat=True)
    vrste = vrste.filter(kategorija='tiskalnik')
    context['vrste'] = vrste
    
    # S temi parametri napolnimo dropdown-e v htmlju, torej npr. seznam vseh znamk
    tipi = Tiskalnik.objects.values('tip').distinct().order_by(Lower('tip')).values_list('tip', flat=True)    
    priklopi = Tiskalnik.objects.values('priklop').distinct().order_by(Lower('priklop')).values_list('priklop', flat=True)        
    context['tipi'] = tipi    
    context['priklopi'] = priklopi                        
                   
    # Če želimo samo zvocne z izbranimi parametri iz dropdowna
    if request.method == 'GET'  and 'vrsta' in request.GET:                  
         
        tiskalniki = Tiskalnik.objects.all() 
         
        # izbran prikljucek v dropdown listu  
        vrsta = request.GET['vrsta'] 
        tip = request.GET['tip'] 
        priklop = request.GET['priklop']                
        
        if vrsta != 'Vsi':
            tiskalniki = tiskalniki.filter(vrsta=vrsta)
         
        if tip != 'Vsi':             
            tiskalniki = tiskalniki.filter(tip=tip) 
                     
        if priklop != 'Vsi':   
            tiskalniki = tiskalniki.filter(priklop=priklop)         
                        
        context['tiskalniki'] = tiskalniki
        return render(request, 'kalkulator/tiskalniki.html', context)
     
    # preverimo katero podkategorijo smo izbrali
    izbrani = request.GET.get('izbrani', False)    
    if izbrani != False:
        tiskalniki = Tiskalnik.objects.filter(vrsta=izbrani) 
    else: 
        tiskalniki = Tiskalnik.objects.all()
        
    context['izbrani'] = izbrani          
    context['tiskalniki'] = tiskalniki               
    
    return render(request, 'kalkulator/tiskalniki.html', context)    
     
def drugo(request):          
   
    context = {}      
            
    # napolnimo dropdown samo s tistimi podkategorijami, ki smo jih prej dodali
    vrste = Kategorija.objects.values('podkategorija').order_by(Lower('podkategorija')).values_list('podkategorija', flat=True)
    vrste = vrste.filter(kategorija='drugo')
    context['vrste'] = vrste                               
                   
    # Če želimo samo zvocne z izbranimi parametri iz dropdowna
    if request.method == 'GET'  and 'vrsta' in request.GET:                  
         
        drugi = Drugo.objects.all() 
         
        # izbran prikljucek v dropdown listu  
        vrsta = request.GET['vrsta']                     
        
        if vrsta != 'Vsi':
            drugi = drugi.filter(vrsta=vrsta)
                    
        context['drugi'] = drugi
        return render(request, 'kalkulator/drugo.html', context)
     
    # preverimo katero podkategorijo smo izbrali
    izbrani = request.GET.get('izbrani', False)    
    if izbrani != False:
        drugi = Drugo.objects.filter(vrsta=izbrani) 
    else: 
        drugi = Drugo.objects.all()
        
    context['izbrani'] = izbrani          
    context['drugi'] = drugi               
    
    return render(request, 'kalkulator/drugo.html', context)    

def periferija(request):          
   
    context = {}      
            
    # napolnimo dropdown samo s tistimi podkategorijami, ki smo jih prej dodali
    vrste = Kategorija.objects.values('podkategorija').order_by(Lower('podkategorija')).values_list('podkategorija', flat=True)
    vrste = vrste.filter(kategorija='periferija')
    context['vrste'] = vrste                               
                   
    # Če želimo samo zvocne z izbranimi parametri iz dropdowna
    if request.method == 'GET'  and 'vrsta' in request.GET:                  
         
        drugi = Periferija.objects.all() 
         
        # izbran prikljucek v dropdown listu  
        vrsta = request.GET['vrsta']                     
        
        if vrsta != 'Vsi':
            drugi = drugi.filter(vrsta=vrsta)
                    
        context['drugi'] = drugi
        return render(request, 'kalkulator/periferija.html', context)
     
    # preverimo katero podkategorijo smo izbrali
    izbrani = request.GET.get('izbrani', False)    
    if izbrani != False:
        drugi = Periferija.objects.filter(vrsta=izbrani) 
    else: 
        drugi = Periferija.objects.all()
        
    context['izbrani'] = izbrani          
    context['drugi'] = drugi               
    
    return render(request, 'kalkulator/periferija.html', context)    
 

    
def razsiritvene(request):          
   
    context = {}
    razsiritvene = Razsiritvena.objects.all()  
    
    # S temi parametri napolnimo dropdown-e v htmlju, torej npr. seznam vseh znamk
    znamke = Razsiritvena.objects.values('znamka').distinct().order_by(Lower('znamka')).values_list('znamka', flat=True)    
    prikljucki = Razsiritvena.objects.values('prikljucek').distinct().order_by(Lower('prikljucek')).values_list('prikljucek', flat=True)
    context['znamke'] = znamke      
    context['prikljucki'] = prikljucki     
    
    
    izbrani = request.GET.get('izbrani', False)
    
    if izbrani != False:
        razsiritvene = razsiritvene.filter(vrsta=izbrani)
    
    # napolnimo samo s tistimi podkategorijami, ki smo jih prej dodali
    vrste = Kategorija.objects.values('podkategorija').order_by(Lower('podkategorija')).values_list('podkategorija', flat=True)
    vrste = vrste.filter(kategorija='razsiritvena')
    context['vrste'] = vrste       
    
    context['izbrani1'] = izbrani        
        
    # Če želimo samo zvocne z izbranimi parametri iz dropdowna
    if request.method == 'GET'  and 'znamka' in request.GET:                  
         
        razsiritvene = Razsiritvena.objects.all() 
         
        # izbran prikljucek v dropdown listu  
        znamka = request.GET['znamka'] 
        vrsta = request.GET['vrsta']  
        prikljucek = request.GET['prikljucek']
        
        
        if znamka != 'Vsi':
            razsiritvene = razsiritvene.filter(znamka=znamka)
         
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
    
    
    # napolnimo samo s tistimi podkategorijami, ki smo jih prej dodali
    prikljucki = Kategorija.objects.values('podkategorija').order_by(Lower('podkategorija')).values_list('podkategorija', flat=True)
    prikljucki = prikljucki.filter(kategorija='disk')
    context['prikljucki'] = prikljucki 
    
    # S temi parametri napolnimo dropdown-e v htmlju, torej npr. seznam vseh znamk
    znamke = Disk.objects.values('znamka').distinct().order_by(Lower('znamka')).values_list('znamka', flat=True)  
    velikosti = Disk.objects.values('velikost').distinct().order_by(Lower('velikost')).values_list('velikost', flat=True)
    context['znamke'] = znamke   
    context['velikosti'] = convertToInteger(velikosti)  
           
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
    

    izbrani = request.GET.get('izbrani', False)
    
    if izbrani != False:
        context['izbrani'] = izbrani
        diski = diski.filter(prikljucek=izbrani)
        
    context['diski'] = diski  
    
    return render(request, 'kalkulator/diski.html', context)    

@login_required
def dodajDisk(request):
    
    context = {}
        
    # napolnimo samo s tistimi podkategorijami, ki smo jih prej dodali
    prikljucki = Kategorija.objects.values('podkategorija').order_by(Lower('podkategorija')).values_list('podkategorija', flat=True)
    prikljucki = prikljucki.filter(kategorija='disk')
    context['prikljucki'] = prikljucki     
        
        
    # S temi parametri napolnimo dropdown-e v htmlju, torej npr. seznam vseh znamk
    znamke = Disk.objects.values('znamka').distinct().order_by(Lower('znamka')).values_list('znamka', flat=True)  
    velikosti = Disk.objects.values('velikost').distinct().order_by(Lower('velikost')).values_list('velikost', flat=True)
    context['znamke'] = znamke   
    context['velikosti'] = velikosti        

    if request.method == 'POST'  and 'znamka' in request.POST:

        znamka = request.POST['znamka']
        if(request.POST['znamka1'] != ''):
            znamka = request.POST['znamka1']  
        prikljucek = request.POST['prikljucek']
        velikost = request.POST['velikost']
        if(request.POST['velikost1'] != ''):
            velikost = request.POST['velikost1']  
        opis = request.POST['opis']       
        kolicina = request.POST['kolicina']
       
        if znamka == 'Vsi' or velikost == 'Vsi':
             return redirect(dodajDisk)
       
        nov_disk = Disk(znamka=znamka, prikljucek=prikljucek, velikost=velikost, opis=opis, kolicina=kolicina)

        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            nov_disk.image = form.cleaned_data['image']
            nov_disk.save()
            
    return render(request, 'kalkulator/dodajDisk.html', context) 
  
@login_required
def dodajRam(request):
    
    context = {}
        
    # S temi parametri napolnimo dropdown-e v htmlju, torej npr. seznam vseh znamk
    znamke = Ram.objects.values('znamka').distinct().order_by(Lower('znamka')).values_list('znamka', flat=True)
    #vrste = Ram.objects.values('vrsta').distinct().order_by(Lower('vrsta')).values_list('vrsta', flat=True)
    velikosti = Ram.objects.values('velikost').distinct().order_by('velikost').values_list('velikost', flat=True)
    context['znamke'] = znamke   
    #context['vrste'] = vrste        
    context['velikosti'] = velikosti 
    
    if request.method == 'POST'  and 'znamka' in request.POST:

        znamka = request.POST['znamka']
        if(request.POST['znamka1'] != ''):
            znamka = request.POST['znamka1']  
        vrsta = request.POST['vrsta']
        if(request.POST['vrsta1'] != ''):
            vrsta = request.POST['vrsta1'] 
        velikost = request.POST['velikost']
        if(request.POST['velikost1'] != ''):
            velikost = request.POST['velikost1']  
        opis = request.POST['opis']       
        kolicina = request.POST['kolicina']
        
        if znamka == 'Vsi' or velikost == 'Vsi':
             return redirect(dodajRam)
        
        nov_ram = Ram(znamka=znamka, vrsta=vrsta, velikost=velikost, opis=opis, kolicina=kolicina)

        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            nov_ram.image = form.cleaned_data['image']
            nov_ram.save()
       
    # napolnimo samo s tistimi podkategorijami, ki smo jih prej dodali
    vrste = Kategorija.objects.values('podkategorija').order_by(Lower('podkategorija')).values_list('podkategorija', flat=True)
    vrste = vrste.filter(kategorija='ram')
    context['vrste'] = vrste

       
    return render(request, 'kalkulator/dodajRam.html', context) 
  
@login_required
def dodajMaticno(request):
    
    context = {}
    
    # S temi parametri napolnimo dropdown-e v htmlju, torej npr. seznam vseh znamk
    znamke = Maticna.objects.values('znamka').distinct().order_by(Lower('znamka')).values_list('znamka', flat=True)
    #podnozja = Maticna.objects.values('podnozje').distinct().order_by(Lower('podnozje')).values_list('podnozje', flat=True) 
    rami = Maticna.objects.values('ram').distinct().order_by(Lower('ram')).values_list('ram', flat=True)
    graficne = Maticna.objects.values('graficna').distinct().order_by(Lower('graficna')).values_list('graficna', flat=True) 
    context['znamke'] = znamke 
    #context['podnozja'] = podnozja
    context['rami'] = rami
    context['graficne'] = graficne
    
    # napolnimo samo s tistimi podkategorijami, ki smo jih prej dodali
    podnozja = Kategorija.objects.values('podkategorija').order_by(Lower('podkategorija')).values_list('podkategorija', flat=True)
    podnozja = podnozja.filter(kategorija='maticna')
    context['podnozja'] = podnozja 
    
    
    
    
    
    if request.method == 'POST'  and 'znamka' in request.POST:

        znamka = request.POST['znamka']
        if(request.POST['znamka1'] != ''):
            znamka = request.POST['znamka1']
        model = request.POST['model']       
        podnozje = request.POST['podnozje']
        if(request.POST['podnozje1'] != ''):
            podnozje = request.POST['podnozje1']
        ram = request.POST['ram']
        if(request.POST['ram1'] != ''):
            ram = request.POST['ram1'] 
        graficna = request.POST['graficna']
        if(request.POST['graficna1'] != ''):
            graficna = request.POST['graficna1']        
        opis = request.POST['opis']
        kolicina = request.POST['kolicina']
       
        if znamka == 'Vsi' or ram == 'Vsi' or graficna == 'Vsi':
             return redirect(dodajMaticno)

       
        nova_maticna = Maticna(znamka=znamka, model=model, podnozje=podnozje, ram=ram, graficna=graficna, opis=opis, kolicina=kolicina)

        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            nova_maticna.image = form.cleaned_data['image']
            nova_maticna.save()
            
    return render(request, 'kalkulator/dodajMaticno.html', context)    
 
@login_required
def dodajNapajalnik(request):
    
    context = {}
    
    
    # S temi parametri napolnimo dropdown-e v htmlju, torej npr. seznam vseh znamk        
    znamke = Napajalnik.objects.values('znamka').distinct().order_by(Lower('znamka')).values_list('znamka', flat=True)
    moci = Napajalnik.objects.values('moc').distinct().order_by(Lower('moc')).values_list('moc', flat=True)  
    voltaze = Napajalnik.objects.values('voltaza').distinct().order_by(Lower('voltaza')).values_list('voltaza', flat=True)
    amperaze = Napajalnik.objects.values('amperaza').distinct().order_by(Lower('amperaza')).values_list('amperaza', flat=True)    
    context['znamke'] = znamke 
    context['moci'] = convertToInteger(moci) 
    context['voltaze'] = convertToInteger(voltaze)
    context['amperaze'] = convertToInteger(amperaze)
    
    # napolnimo samo s tistimi podkategorijami, ki smo jih prej dodali
    vrste = Kategorija.objects.values('podkategorija').order_by(Lower('podkategorija')).values_list('podkategorija', flat=True)
    vrste = vrste.filter(kategorija='napajalnik')
    context['vrste'] = vrste
    
    
    

    if request.method == 'POST'  and 'znamka' in request.POST:

        vrsta = request.POST['vrsta']
        if(request.POST['vrsta1'] != ''):
            vrsta = request.POST['vrsta1']
        znamka = request.POST['znamka']
        if(request.POST['znamka1'] != ''):
            znamka = request.POST['znamka1']
        moc = request.POST['moc']  
        if(request.POST['moc1'] != ''):
            moc = request.POST['moc1']
        voltaza = request.POST['voltaza']
        if(request.POST['voltaza1'] != ''):
            voltaza = request.POST['voltaza1']
        amperaza = request.POST['amperaza']
        if(request.POST['amperaza1'] != ''):
            amperaza = request.POST['amperaza1']    
        opis = request.POST['opis']
        kolicina = request.POST['kolicina']
        
        if amperaza == 'Vsi':  
            amperaza = 0
            
        if voltaza == 'Vsi':
            voltaza = 0
            
        if moc == 'Vsi':
            moc = amperaza * voltaza
            
        
        
        if znamka == 'Vsi' or moc == 'Vsi' or vrsta == 'Vsi':
             return redirect(dodajNapajalnik)
        
        nov_napajalnik = Napajalnik(vrsta=vrsta, znamka=znamka, moc=moc, amperaza=amperaza, voltaza=voltaza, opis=opis, kolicina=kolicina)

        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            nov_napajalnik.image = form.cleaned_data['image']
            nov_napajalnik.save()
            
    return render(request, 'kalkulator/dodajNapajalnik.html', context)  
   
@login_required
def dodajInput(request):
    
    context = {}          
      
    # S temi parametri napolnimo dropdown-e v htmlju, torej npr. seznam vseh znamk
    vrste = Input.objects.values('vrsta').distinct().order_by(Lower('vrsta')).values_list('vrsta', flat=True)
    znamke = Input.objects.values('znamka').distinct().order_by(Lower('znamka')).values_list('znamka', flat=True)
    prikljucki = Input.objects.values('prikljucek').distinct().order_by(Lower('prikljucek')).values_list('prikljucek', flat=True)
    context['znamke'] = znamke
    context['vrste'] = vrste
    context['prikljucki'] = prikljucki
    
    # napolnimo samo s tistimi podkategorijami, ki smo jih prej dodali
    povezave = Kategorija.objects.values('podkategorija').order_by(Lower('podkategorija')).values_list('podkategorija', flat=True)
    povezave = povezave.filter(kategorija='input')
    context['povezave'] = povezave
    
    
        
    if request.method == 'POST'  and 'vrsta' in request.POST:

        vrsta = request.POST['vrsta']
        if(request.POST['vrsta1'] != ''):
          vrsta = request.POST['vrsta1']
        znamka = request.POST['znamka']
        if(request.POST['znamka1'] != ''):
          znamka = request.POST['znamka1']
        prikljucek = request.POST['prikljucek']
        if(request.POST['prikljucek1'] != ''):
          prikljucek = request.POST['prikljucek1']
        povezava = request.POST['povezava']    
        opis = request.POST['opis']
        kolicina = request.POST['kolicina']
        
        if znamka == 'Vsi' or prikljucek == 'Vsi' or povezava == 'Vsi':
             return redirect(dodajInput)
                
        nov_input = Input(vrsta=vrsta, znamka=znamka, prikljucek=prikljucek, povezava=povezava, opis=opis, kolicina=kolicina)

        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            nov_input.image = form.cleaned_data['image']
            nov_input.save()
            
    return render(request, 'kalkulator/dodajInput.html', context) 
    
@login_required
def dodajGraficno(request):
    
    context = {}
    
    # napolnimo samo s tistimi podkategorijami, ki smo jih prej dodali
    vodila = Kategorija.objects.values('podkategorija').order_by(Lower('podkategorija')).values_list('podkategorija', flat=True)
    vodila = vodila.filter(kategorija='graficna')
    context['vodila'] = vodila
        
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
        vodilo = request.POST['vodilo']
        opis = request.POST['opis']
        kolicina = request.POST['kolicina']
        
        if znamka == 'Vsi' or pomnilnik == 'Vsi':
             return redirect(dodajGraficno)  
                
        nova_graficna = Graficna(znamka=znamka, model=model, pomnilnik=pomnilnik, vodilo=vodilo, opis=opis, kolicina=kolicina)
        
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            nova_graficna.image = form.cleaned_data['image']
            nova_graficna.save()
            
    return render(request, 'kalkulator/dodajGraficno.html', context)    
  
@login_required
def dodajProcesor(request):
    
    context = {}
    
    # S temi parametri napolnimo dropdown-e v htmlju, torej npr. seznam vseh znamk
    znamke = Procesor.objects.values('znamka').distinct().order_by(Lower('znamka')).values_list('znamka', flat=True)
    #podnozja = Procesor.objects.values('podnozje').distinct().order_by(Lower('podnozje')).values_list('podnozje', flat=True)    
    context['znamke'] = znamke 
    #context['podnozja'] = podnozja
    
    # napolnimo samo s tistimi podkategorijami, ki smo jih prej dodali
    podnozja = Kategorija.objects.values('podkategorija').order_by(Lower('podkategorija')).values_list('podkategorija', flat=True)
    podnozja = podnozja.filter(kategorija='maticna')
    context['podnozja'] = podnozja 
    
    

    if request.method == 'POST'  and 'znamka' in request.POST:

        znamka = request.POST['znamka'].upper()
        if(request.POST['znamka1'] != ''):
            znamka = request.POST['znamka1']
        model = request.POST['model'].upper()        
        podnozje = request.POST['podnozje'].upper()
        if(request.POST['podnozje1'] != ''):
            podnozje = request.POST['podnozje1']
        opis = request.POST['opis']    
        kolicina = request.POST['kolicina']
        
        if znamka == 'Vsi' or model == '':
             return redirect(dodajProcesor)
        
        nov_procesor = Procesor(znamka=znamka, model=model, podnozje=podnozje, opis=opis, kolicina=kolicina)

        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            nov_procesor.image = form.cleaned_data['image']
            nov_procesor.save()
            
    return render(request, 'kalkulator/dodajProcesor.html', context)    

@login_required
def dodajKabel(request):
    
    context = {}
    
    # S temi parametri napolnimo dropdown-e v htmlju, torej npr. seznam vseh znamk
    #vrste = Kabel.objects.values('vrsta').distinct().order_by(Lower('vrsta')).values_list('vrsta', flat=True)   
    #context['vrste'] = vrste
    
    # napolnimo samo s tistimi podkategorijami, ki smo jih prej dodali
    vrste = Kategorija.objects.values('podkategorija').order_by(Lower('podkategorija')).values_list('podkategorija', flat=True)
    vrste = vrste.filter(kategorija='kabel')
    context['vrste'] = vrste
    
    
    
    if request.method == 'POST'  and 'vrsta' in request.POST:

        vrsta = request.POST['vrsta']
        if(request.POST['vrsta1'] != ''):
            vrsta = request.POST['vrsta1']
        opis = request.POST['opis']
        kolicina = request.POST['kolicina']
        
        nov_kabel = Kabel(vrsta=vrsta, opis=opis, kolicina=kolicina)

        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            nov_kabel.image = form.cleaned_data['image']
            nov_kabel.save()
            
    return render(request, 'kalkulator/dodajKabel.html', context)    
   
@login_required
def dodajZaslon(request):
    
    context = {}
    
    # S temi parametri napolnimo dropdown-e v htmlju, torej npr. seznam vseh znamk
    znamke = Zaslon.objects.values('znamka').distinct().order_by(Lower('znamka')).values_list('znamka', flat=True)
    velikosti = Zaslon.objects.values('velikost').distinct().order_by(Lower('velikost')).values_list('velikost', flat=True)
    inputi = Zaslon.objects.values('input').distinct().order_by(Lower('input')).values_list('input', flat=True)
    context['znamke'] = znamke     
    context['velikosti'] = velikosti
    context['inputi'] = inputi

    
    if request.method == 'POST'  and 'znamka' in request.POST:

        znamka = request.POST['znamka']
        if(request.POST['znamka1'] != ''):
            znamka = request.POST['znamka1']
        model = request.POST['model']        
        vrsta = request.POST['vrsta']
        velikost = request.POST['velikost']
        if(request.POST['velikost1'] != ''):
            velikost = request.POST['velikost1']
        input = request.POST['input']
        if(request.POST['input1'] != ''):
            input = request.POST['input1']    
        opis = request.POST['opis']
        kolicina = request.POST['kolicina']
        
        if znamka == 'Vsi' or pomnilnik == 'Vsi' or vrsta == 'Vsi' or velikost == 'Vsi' or input == 'Vsi':
             return redirect(dodajZaslon)
        
        nov_zaslon = Zaslon(znamka=znamka, model=model, vrsta=vrsta, velikost=velikost, input=input, opis=opis, kolicina=kolicina)

        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            nov_zaslon.image = form.cleaned_data['image']
            nov_zaslon.save()
            
    return render(request, 'kalkulator/dodajZaslon.html', context) 
 
@login_required
def dodajRazsiritveno(request):
    
    context = {}
        
    # S temi parametri napolnimo dropdown-e v htmlju, torej npr. seznam vseh znamk
    znamke = Razsiritvena.objects.values('znamka').distinct().order_by(Lower('znamka')).values_list('znamka', flat=True)
    #vrste = Razsiritvena.objects.values('vrsta').distinct().order_by(Lower('vrsta')).values_list('vrsta', flat=True)
    prikljucki = Razsiritvena.objects.values('prikljucek').distinct().order_by(Lower('prikljucek')).values_list('prikljucek', flat=True)
    context['znamke'] = znamke
    #context['vrste'] = vrste  
    context['prikljucki'] = prikljucki
    
    if request.method == 'POST'  and 'znamka' in request.POST:        
        znamka = request.POST['znamka']        
        if(request.POST['znamka1'] != ''):
            znamka = request.POST['znamka1']
        model = request.POST['model']      
        vrsta = request.POST['vrsta']          
        prikljucek = request.POST['prikljucek']
        if(request.POST['prikljucek1'] != ''):
            prikljucek = request.POST['prikljucek1']
        opis = request.POST['opis']   
        kolicina = request.POST['kolicina']         
        
        if znamka == 'Vsi' or prikljucek == 'Vsi':
             return redirect(dodajGraficno)
        
        nova_razsiritvena = Razsiritvena(znamka=znamka, model=model, vrsta=vrsta, prikljucek=prikljucek, opis=opis, kolicina=kolicina)
                
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():           
            nova_razsiritvena.image = form.cleaned_data['image']
             
        nova_razsiritvena.save()                          
   
    # napolnimo samo s tistimi podkategorijami, ki smo jih prej dodali
    vrste = Kategorija.objects.values('podkategorija').order_by(Lower('podkategorija')).values_list('podkategorija', flat=True)
    vrste = vrste.filter(kategorija='razsiritvena')
    context['vrste'] = vrste     
    
    return render(request, 'kalkulator/dodajRazsiritveno.html', context)    

@login_required
def dodajTiskalnik(request):
    
    context = {}
     
    # napolnimo samo s tistimi podkategorijami, ki smo jih prej dodali
    vrste = Kategorija.objects.values('podkategorija').order_by(Lower('podkategorija')).values_list('podkategorija', flat=True)
    vrste = vrste.filter(kategorija='tiskalnik')
    context['vrste'] = vrste 
     
    # S temi parametri napolnimo dropdown-e v htmlju, torej npr. seznam vseh znamk
    tipi = Tiskalnik.objects.values('tip').distinct().order_by(Lower('tip')).values_list('tip', flat=True)    
    priklopi = Tiskalnik.objects.values('priklop').distinct().order_by(Lower('priklop')).values_list('priklop', flat=True)
    context['tipi'] = tipi
    context['priklopi'] = priklopi
    
    if request.method == 'POST'  and 'vrsta' in request.POST:        
        vrsta = request.POST['vrsta']        
        tip = request.POST['tip'] 
        if(request.POST['tip1'] != ''):
            tip = request.POST['tip1']
        priklop = request.POST['priklop']        
        if(request.POST['priklop1'] != ''):
            priklop = request.POST['priklop1']
        opis = request.POST['opis']   
        kolicina = request.POST['kolicina']         
         
        if tip == 'Vsi' or priklop == 'Vsi':
             return redirect(dodajTiskalnik)
         
        nov_tiskalnik = Tiskalnik(vrsta=vrsta, tip=tip, priklop=priklop, opis=opis, kolicina=kolicina)
                
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():           
            nov_tiskalnik.image = form.cleaned_data['image']
             
        nov_tiskalnik.save()                         
               
    return render(request, 'kalkulator/dodajTiskalnik.html', context)        

@login_required
def dodajDrugo(request):
    
    context = {}
     
    # napolnimo samo s tistimi podkategorijami, ki smo jih prej dodali
    vrste = Kategorija.objects.values('podkategorija').order_by(Lower('podkategorija')).values_list('podkategorija', flat=True)
    vrste = vrste.filter(kategorija='drugo')
    context['vrste'] = vrste 
         
    
    if request.method == 'POST'  and 'vrsta' in request.POST:        
        vrsta = request.POST['vrsta'] 
        ime = request.POST['ime']
        opis = request.POST['opis']
        kolicina = request.POST['kolicina']                
         
        nov_drugo = Drugo(vrsta=vrsta, ime=ime, opis=opis, kolicina=kolicina)
                
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():           
            nov_drugo.image = form.cleaned_data['image']
             
        nov_drugo.save()                         
               
    return render(request, 'kalkulator/dodajDrugo.html', context)        

@login_required
def dodajPeriferijo(request):
    
    context = {}
     
    # napolnimo samo s tistimi podkategorijami, ki smo jih prej dodali
    vrste = Kategorija.objects.values('podkategorija').order_by(Lower('podkategorija')).values_list('podkategorija', flat=True)
    vrste = vrste.filter(kategorija='periferija')
    context['vrste'] = vrste 
         
    
    if request.method == 'POST'  and 'vrsta' in request.POST:        
        vrsta = request.POST['vrsta'] 
        ime = request.POST['ime']
        opis = request.POST['opis']
        kolicina = request.POST['kolicina']                
         
        nov_drugo = Periferija(vrsta=vrsta, ime=ime, opis=opis, kolicina=kolicina)
                
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():           
            nov_drugo.image = form.cleaned_data['image']
             
        nov_drugo.save()                         
               
    return render(request, 'kalkulator/dodajPeriferijo.html', context)        
 

    
def convertToInteger(list_of_strings):
    list = []
    for el in list_of_strings:
        list.append(int(el))
    return sorted(list)
 
 


 


 
 
 