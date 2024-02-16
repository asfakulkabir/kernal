from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.conf import settings
from django.http import HttpResponse
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth import authenticate,login,logout
from .models import Product
from tkinter import E

def home(request):
    products = Product.objects.all()[::-1]
    return render(request, 'home.html', {'products':products})

def about(request):
    return render(request, 'about.html', {})

def contact(request):
    if request.method == 'POST':
        name= request.POST['name']
        email= request.POST['email']
        message= request.POST['message']

        send_mail(
        name,
        message,
        "fawadpentagon@gmail.com",
        ["Khan.ishtiak2008@gmail.com","asfakulthoha@gmail.com"],
        fail_silently=False,)
        return render(request, 'contact.html')
    else:
        return render(request, 'contact.html')


def product(request, slug):
        products = Product.objects.filter(slug =slug)
        if products:
            return render(request  , 'product.html' , {'product' : products.first(), 'products':Product.objects.all()[:4][::-1]})
        else:
            return redirect('home.html')


def cart(request):
    return render(request, 'cart.html', {})