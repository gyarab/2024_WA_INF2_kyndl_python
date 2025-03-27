from django.db import models

class Category(models.Model):
    název = models.CharField(max_length=100)
    popis = models.TextField()

    def __str__(self):
        return self.název
    
class Type(models.Model):
    název = models.CharField(max_length=100)
    popis = models.TextField()

    def __str__(self):
        return self.název

class Bohemka(models.Model):
    název = models.CharField(max_length=100)
    cena = models.DecimalField(max_digits=10, decimal_places=2)
    obrázek = models.URLField()
    odkaz = models.URLField()
    category = models.ManyToManyField(Category)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)

    def __str__(self):
        return self.název
