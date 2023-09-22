from django.contrib import admin
from django.urls import path
from Article import views

app_name="articles"

urlpatterns = [
     path('calltest/',views.test,name="test"),
     path('index/',views.index,name="index"),
     path('dashboard/',views.dashboard,name="dashboard"),
     path('addarticle/',views.addarticle,name="addarticle"),     
     path('detail/<int:id>',views.detail,name="detail")
     
]