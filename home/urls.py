from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.login,name='login'),
    path('home',views.postLogin,name='postLogin'),
    path('logout',views.logout,name='logout'),
    path('register',views.register,name='register'),
    path('Signup',views.Signup,name='register'),
    path('career',views.career ,name='career'),
    path('homes',views.study ,name='study')


    
]
