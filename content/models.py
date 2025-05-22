from django.db import models

class Category(models.Model):
    nazev = models.CharField(max_length=100)
    popis = models.TextField()

    def __str__(self):
        return self.nazev
    
class Type(models.Model):
    nazev = models.CharField(max_length=100)
    popis = models.TextField()

    def __str__(self):
        return self.nazev

class Bohemka(models.Model):
    nazev = models.CharField(max_length=100)
    obrazek = models.URLField(max_length=500)
    category = models.ForeignKey(Category, related_name='articles', on_delete=models.CASCADE)
    type = models.ManyToManyField(Type, related_name='articles')

    def __str__(self):
        return self.nazev
