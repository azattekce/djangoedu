
from django.contrib import admin
from django.urls import path,include
from Article import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,name="index"),
    path('about',views.about,name="about"),
    path('articles/',include("Article.urls")),
    path('users/',include("User.urls")),
]
