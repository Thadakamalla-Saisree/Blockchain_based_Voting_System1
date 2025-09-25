"""WebC URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [ 
    path('', views.home, name="Welcome"), 
    path('alogin/', views.adminlogindef, name="adminlogindef"), 
    path('ulogin/', views.userlogindef, name="userlogindef"),    
    path('userreg/', views.signupdef, name="signupdef"),    
    path('usignupaction/', views.usignupactiondef, name="usignupactiondef"),
    path('userloginaction/', views.userloginactiondef, name="userloginactiondef"),
    path('userhome/', views.userhomedef, name="userhome"),
    path('userlogout/', views.userlogoutdef, name="userlogout"),
    path('adminloginaction/', views.adminloginactiondef, name="adminloginactiondef"),
    path('adminhome/', views.adminhomedef, name="adminhome"),
    path('adminlogout/', views.adminlogoutdef, name="adminlogout"),
    

    path('addelection/', views.addelection, name="addelection"),
    path('addcandidate/', views.addcandidate, name="addcandidate"),
    path('aviewcandidates/', views.aviewcandidates, name="aviewcandidates"),
    path('viewelections/', views.viewelections, name="viewelections"),
    path('addannouncement/', views.addannouncement, name="addannouncement"),
    path('addfeedback/', views.addfeedback, name="addfeedback"),
    path('viewfeedback/', views.viewfeedback, name="viewfeedback"),
    path('uannouncement/', views.uannouncement, name="uannouncement"),
    


    path('uviewelections/', views.uviewelections, name="uviewelections"),
    path('viewresults/', views.viewresults, name="viewresults"),
    path('vote/', views.vote, name="vote"),
    path('otpverify/', views.otpverify, name="otpverify"),
    
    
    

    
]
