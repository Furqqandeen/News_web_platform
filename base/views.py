from django.shortcuts import render,HttpResponse,redirect
from base.models import Categories,Articles
from base.form import RegisterationFrom
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    context={
        
        'articles':Articles.objects.all().filter(status='Published',is_treanding=True).order_by('-updated_at'),
        'articles_not_teanding':Articles.objects.all().filter(status='Published',is_treanding=False).order_by('-updated_at')
    }
    return render(request,'home.html',context)

def post_by_category(request,cname):
    category=Categories.objects.get(category=cname)
    context={
        
        'category':cname,
        'articles':Articles.objects.all().filter(category=category.id)
    }
    return render(request,'post_by_category.html',context)

@login_required(login_url='login')
def single_article(request,slug):
    context={
        'article':Articles.objects.get(slug=slug),

    }
    return render(request,'article.html',context) 


def register(request):
    if request.method=='POST':
        form=RegisterationFrom(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:   
        form=RegisterationFrom()

    context={
        'form':form
    }
    return render(request,'register.html',context)

def user_login(request):
    if request.method=='POST':
        form=AuthenticationForm(request,request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user=auth.authenticate(username=username,password=password)
            if user is not None:
                auth.login(request,user)
                return redirect('home')
    else:
        form=AuthenticationForm()

    context={
        'form':form
    }
    return render(request,'login.html',context)

def user_logout(request):
    auth.logout(request)
    return redirect('home')
