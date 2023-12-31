from django.db import models
from django import forms


# Create your models here.


class Article(models.Model):
    author = models.ForeignKey("auth.User",on_delete = models.CASCADE,verbose_name = "Yazar ")
    title = models.CharField(max_length = 50,verbose_name = "Başlık")
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True,verbose_name="Tarih")
    article_image = models.FileField(blank = True,null = True,verbose_name="Makaleye Fotoğraf Ekleyin")
    def __str__(self):
        return self.title
    
 