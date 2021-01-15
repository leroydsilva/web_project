from django.contrib import admin
from django.urls import path,include
from . import views
app_name='home'
urlpatterns = [
    path('',views.home,name='home'),
    path('login/',views.postLogin,name='postLogin'),
    path('logout/',views.logout,name='logout'),
    path('register/',views.register,name='register'),
    
    path('course/',views.course ,name='course'),
    path('study/',views.study ,name='study'),
    path('contact/',views.contact ,name='contact')


    
]
