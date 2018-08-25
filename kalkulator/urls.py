""" i created this """

from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

#url(r'^$', auth_views.login, {'template_name': 'kalkulator/login.html'}, name='login'),
	#url(r'^login.html', auth_views.login, {'template_name': 'kalkulator/login.html'}, name='login'),

urlpatterns = [
	
	# login, logout
	url( r'^login/$',auth_views.LoginView.as_view(template_name="kalkulator/login.html"), name="login"),
    #url(r'^login/$', views.LoginView.as_view(template_name=template_name), name='login'),   
	
    #url(r'^logout/$', auth_views.logout, {'next_page': '/kalkulator'}, name='logout'),
	url( r'^logout/$',auth_views.LoginView.as_view(template_name="kalkulator/logout.html"), name="logout"),
	#	registracija
	url(r'^registracija', views.registracija, name='registracija'),
	url(r'^RegistracijaPodrobno', views.RegistracijaPodrobno, name='RegistracijaPodrobno'),		
		
	# stanje		
	url(r'^stanje', views.stanje, name='stanje'), 
	url(r'^StanjePodrobno', views.StanjePodrobno, name='StanjePodrobno'), 
	
    # graficne
    url(r'^graficne', views.graficne, name='graficne'),
    
     # tipkovnice
    url(r'^tipkovnice', views.tipkovnice, name='tipkovnice'),
    
	# vpisi prihodek
	url(r'^vpisiPrihodek', views.vpisiPrihodek, name='vpisiPrihodek'),
	url(r'^VpisiPrihodekPodrobno', views.vpisiPrihodekPodrobno, name='vpisiPrihodekPodrobno'), 
	
	# vpisi odhodek
	url(r'^vpisiOdhodek', views.vpisiOdhodek, name='vpisiOdhodek'),
	url(r'^VpisiOdhodekPodrobno', views.vpisiOdhodekPodrobno, name='vpisiOdhodekPodrobno'), 
	
	# porocila
	url(r'^porocila', views.porocila, name='porocila'),	
	url(r'^PorocilaPodrobno', views.PorocilaPodrobno, name='porocilaPodrobno'), 
	
	# dodaj racun
	url(r'^dodajRacun', views.dodajRacun, name='dodajRacun'),
	
	# odstrani racun
	url(r'^odstraniRacun', views.odstraniRacun, name='odstraniRacun'),
	
    # administracija
    url(r'^administracija', views.administracija, name='administracija'),
	url(r'^AdministracijaPodrobno', views.AdministracijaPodrobno, name='AdministracijaPodrobno')
	
]

