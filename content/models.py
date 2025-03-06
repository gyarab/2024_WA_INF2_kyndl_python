from django.db import models

class Bohemka(models.Model):
    název = models.CharField(max_length=100)
    cena = models.DecimalField(max_digits=10, decimal_places=2)
    obrázek = models.URLField()
    odkaz = models.URLField()
    
