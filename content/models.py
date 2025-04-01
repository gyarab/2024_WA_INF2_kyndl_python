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
    cena = models.DecimalField(max_digits=10, decimal_places=2)
    obrazek = models.URLField()
    odkaz = models.URLField()
    category = models.ForeignKey(Category, related_name='articles', on_delete=models.CASCADE)
    type = models.ManyToManyField(Type, related_name='articles')

    def __str__(self):
        return self.nazev
