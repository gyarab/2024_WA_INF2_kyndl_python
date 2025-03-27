from django.shortcuts import render
from django.http import HttpResponse
from .models import Bohemka, Category, Type

import requests
import json

def homepage(request):
    articles = Bohemka.objects.order_by('title')
    return render(request, 'content/homepage.html', {'articles': articles})

def article(request, id):
    article = Bohemka.objects.get(pk=id)

    return render(request, 'content/article.html', {'article': article})

def categories(request, id):
    category = Category.objects.get(pk=id)
    return render(request, 'content/category.html', {'category': category})

def types(request, id):
    type = Type.objects.get(pk=id)
    return render(request, 'content/type.html', {'type': type})