""" i created this """

from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
	
	# login, logout
	url( r'^login/$',auth_views.LoginView.as_view(template_name="kalkulator/login.html"), name="login"),    	    
	url( r'^logout/$',auth_views.LoginView.as_view(template_name="kalkulator/logout.html"), name="logout"),
    
    
	# registracija
	url(r'^registracija', views.registracija, name='registracija'),			
		
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
    url(r'^razsiritvene', views.razsiritvene, name='razsiritvene'),
    
    # kabli
    url(r'^kabli', views.kabli, name='kabli'),
    
    # dodajInput
    url(r'^dodajInput', views.dodajInput, name='dodajInput'),
    
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
]

