from django.http import HttpResponse
from django.shortcuts import render, redirect
from myapp.models import *

def show_about_page(request):
    print("About page request")
    name = 'Contact for More Interested Images'
    link = 'https:/www.instagaram.com'

    data = {
        'name': name,
        'link': link
    }

    return render(request, "about.html", {data})


def show_home_page(request):
    cats = Category.objects.all()
    images = Image.objects.all()
    data = {'images': images, 'cats': cats}

    return render(request, "Home.html", data)


def show_category_page(request, cid):
    cats = Category.objects.all()
    category = Category.objects.get(pk=cid)
    images = Image.objects.filter(cat=category)
    data = {'images': images, 'cats': cats}

    return render(request, "Home.html", data)


def home(request):
    return redirect('/home')
