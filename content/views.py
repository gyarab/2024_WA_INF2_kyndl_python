from django.shortcuts import render
from django.http import HttpResponse

import requests
import json

# data = [
#     {
#         'title': 'web Gymnazia Arabska',
#         'link': 'https://gyarab.cz',
#     },
#     {
#         'title': 'web jutub',
#         'link': 'https://youtube.com',
#     },
# ]

def homepage(request):
    with open('articles.json') as file:
        data = json.load(file)

    article_html = ''
    i = 0
    for article in data:
        title = article['title']
        picture = article['picture']
        article_html += f'<a href="/article{i}<h2>{title}</h2></a>'
        article_html += f'<img src="{picture}" alt="{title}">'
        i += 1

    return HttpResponse(article_html)

def hello(request, name):
    return HttpResponse(f'Ahoj {name}')

def vynasob(request, a, b):
    return HttpResponse(f'{a} * {b} = {a * b}')