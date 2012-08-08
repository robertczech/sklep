from django.db import models

# Create your models here.

class Produkt(models.Model):
    nazwa = models.CharField(max_length=60)
    cena = models.IntegerField()
    def __unicode__(self):
	return self.nazwa
