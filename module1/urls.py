from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('Home/', intro,name='intro'),
    path('Welcome/', ruthik, name='welcome'),
    path('',NewHomepage,name='NewHomepage'),
    path('travelpackage/',travelpackage,name='travelpackage'),
    path('console/',console,name='console'),
    path('p/',print1,name='print1'),
    path('ran1/',random1,name='random1'),
    path('b/',Randomotp1,name='Randomotp1'),
    path('c/',get_date,name='get_date'),
    path('d/',getdate1,name='getdate1'),
    path('Pytz/',tzfunctioncall,name='tzfunctioncall'),
    path('ru/',functioncall1,name='functioncall1'),
    path('th/',registerloginfunction,name='registerloginfunction'),
     path('piecall/', piechartcall, name='piechartcall'),
    path('pie_chart/', pie_chart, name='pie_chart'),
    path('ps/', photoslide, name='photoslide'),
    path('wcall/', weathercall, name='weathercall'),
    path('wlogic/', weatherlogic, name='weatherlogic'),
    path('dh/',signup,name='signup'),
    path('tl/',login,name='login'),
    path('a/',signup1,name='signup1'),
    path('ca/',login1,name='login1'),
    path('dog/',logout,name='logout'),
    path('cat/',contactmail,name='contactmail'),
    path('robo/',contact,name='contact'),
]
