
from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('',views.index,name='index'),
    path('index',views.index,name='index'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('home',views.home,name='home'),
    path('create',views.create,name='create'),
    path('success',views.success,name='success'),
    path('log',views.log,name='log'),
    path('user',views.user,name='user'),
    path('company',views.company,name='company'),
    path('cadd',views.cadd,name='cadd'),
    path('uedits',views.uedits,name='uedits'),
    path('edit', views.edit, name='edit'),
    path('edited', views.edited, name='edited'),
    path('logins',views.logins,name='logins'),
    path('logi',views.logi,name='logi'),
    path('rentals', views.rentals, name='rents'),
    path('save',views.save,name='save'),
    path('bill',views.bill,name='bill'),
    path('take',views.take,name='take'),
    path('userid',views.userid,name='userid'),
    path('logerror',views.logerror,name='logerror'),
    path('logout',views.logout,name="logout"),


]