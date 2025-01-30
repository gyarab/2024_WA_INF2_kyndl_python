from django.shortcuts import render
from django.http import HttpResponse

import requests

data = [
    {
        'title': 'Python Django Tutorial',
        'url': 'https://www.youtube.com/watch?v=F5mRW0jo-U4',
    },
    {
        'title': 'Bohemians 1905',
        'url': 'https://www.bohemians.cz/',

    }
]

def homepage(request):
    ret = '''
    <!DOCTYPE html>
    <html>
    <head></head>
    <body>
    <ul>
    '''

    for i in data:
        ret += f"""
        <li>
            <a href="{i['url']}">{i['title']}</a>
        </li>"""

    ret += "</ul></body></html>"
    return HttpResponse(ret)
