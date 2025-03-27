from django.contrib import admin

from .models import Bohemka, Category, Type

admin.site.register(Bohemka)
admin.site.register(Category)
admin.site.register(Type)