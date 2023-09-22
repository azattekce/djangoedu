from django.shortcuts import render,HttpResponse,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from datetime import date
from .models import Article
from .forms import ArticleForm

# Create your views here.
def index(request):
 return render(request,"index.html")

def about(request):
 return render(request,"about.html")

def detail(request,id):
    article=get_object_or_404(Article,id=id)# Article.objects.filter(id =id).first()
    context = {
        "article":article
    }
    return render(request,"detail.html",context)

def test(request):
 return HttpResponse("Merhaba Create sayfasına hoş geldiniz.")

@login_required(login_url = "users:login")
def dashboard(request):
    articles = Article.objects.filter(author = request.user)
    context = {
        "articles":articles
    }
    return render(request,"dashboard.html",context)


@login_required(login_url = "users:login")
def addarticle(request):
    form=ArticleForm(request.POST or None)
    context={
      'form':form
    }

    if(form.is_valid()):
        article=form.save(commit=False)
        article.author= request.user
        article.save()
        messages.success(request,"Makele başarılı yapıldı.")
        return render(request,"addarticle.html",context)

    
    return render(request,"addarticle.html",context)

