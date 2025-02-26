from django.urls import path
from content.views import homepage, article

urlpatterns = [
    path('', homepage, name='homepage'),
    path('article/<int:id>/', article, name='article'),
]
