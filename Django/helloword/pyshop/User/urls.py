from django.contrib import admin
from django.urls import path
from User import views

app_name="users"

urlpatterns = [
     path('register/',views.register,name="register"),
     path('login/',views.loginUser,name="login"),
     path('logout/',views.logoutUser,name="logout"),
]