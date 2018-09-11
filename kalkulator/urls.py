""" i created this """

from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.staticfiles.urls import static
from django.conf import settings

urlpatterns = [
	
	# login, logout
	#url( r'^login/$',auth_views.LoginView.as_view(template_name="kalkulator/login.html"), name="login"),    	    
	#url( r'^logout/$',auth_views.LoginView.as_view(template_name="kalkulator/logout.html"), name="logout"),
        
	# registracija
	#url(r'^registracija', views.registracija, name='registracija'),     
	
    # delete		
	url(r'^delete/(?P<vrsta>\w+)/(?P<id>\d+)$', views.delete, name='delete'),
        
    # add		
	url(r'^add/(?P<vrsta>\w+)/(?P<id>\d+)$', views.add, name='add'),
    
	# main		
	url(r'^main', views.main, name='main'), 
	 	
    # graficne
    url(r'^graficne', views.graficne, name='graficne'),
    
    # inputi
    url(r'^inputi', views.inputi, name='inputi'),
    
    # procesorji
    url(r'^procesorji', views.procesorji, name='procesorji'),
    
    # maticne
    url(r'^maticne', views.maticne, name='maticne'),           
       
    # diski
    url(r'^diski', views.diski, name='diski'),
    
    # rami
    url(r'^rami', views.rami, name='rami'),
           
    # zasloni
    url(r'^zasloni', views.zasloni, name='zasloni'),
    
    # napajalniki
    url(r'^napajalniki', views.napajalniki, name='napajalniki'),
    
    # razsiritvene
    url(r'^razsiritvene/(?P<izbrani>\w+)', views.razsiritvene, name='razsiritvene'),
    
    # razsiritvene
    url(r'^razsiritvene', views.razsiritvene, name='razsiritvene'),
    
    
    # kabli
    url(r'^kabli', views.kabli,  name='kabli'),
    
    # adapterji
    url(r'^adapterji', views.adapterji,  name='adapterji'),
    
    # vrsteNapajalnikov
    url(r'^vrsteNapajalnikov', views.vrsteNapajalnikov, name='vrsteNapajalnikov'),
    
    # vrsteRazsiritvenih
    url(r'^vrsteRazsiritvenih', views.vrsteRazsiritvenih, name='vrsteRazsiritvenih'),
   
    # vrsteRama
    url(r'^vrsteRama', views.vrsteRama, name='vrsteRama'),
    
   
    # vrsteGraficnih
    url(r'^vrsteGraficnih', views.vrsteGraficnih, name='vrsteGraficnih'),
    
    # vrsteInputov
    url(r'^vrsteInputov', views.vrsteInputov, name='vrsteInputov'),
    
    # dodajInput
    url(r'^dodajInput', views.dodajInput, name='dodajInput'),
    
    # vrsteDiskov
    url(r'^vrsteDiskov', views.vrsteDiskov, name='vrsteDiskov'),
    
     # dodajGraficno
    url(r'^dodajGraficno', views.dodajGraficno, name='dodajGraficno'),
    
    # dodajProcesor
    url(r'^dodajProcesor', views.dodajProcesor, name='dodajProcesor'),
    
    # dodajMaticno
    url(r'^dodajMaticno', views.dodajMaticno, name='dodajMaticno'),      
    
    # dodajNapajalnik
    url(r'^dodajNapajalnik', views.dodajNapajalnik, name='dodajNapajalnik'),     
    
    # dodajDisk
    url(r'^dodajDisk', views.dodajDisk, name='dodajDisk'),
    
    # dodajRam
    url(r'^dodajRam', views.dodajRam, name='dodajRam'),
           
    # dodajZaslon
    url(r'^dodajZaslon', views.dodajZaslon, name='dodajZaslon'),
    
    # dodajRazsiritveno
    url(r'^dodajRazsiritveno', views.dodajRazsiritveno, name='dodajRazsiritveno'),
    
    # dodajKabel
    url(r'^dodajKabel', views.dodajKabel, name='dodajKabel'),  

    # dodajAdapter
    url(r'^dodajAdapter', views.dodajAdapter, name='dodajAdapter'),      
    
]


