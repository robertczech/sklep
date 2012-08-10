from django.db import models
from stdimage import StdImageField

# Create your models here.

class Kategoria(models.Model):
    nazwa = models.CharField(max_length=60)
    def __unicode__(self):
	return self.nazwa

class Produkt(models.Model):
    kategoria = models.ForeignKey(Kategoria)
    nazwa = models.CharField(max_length=60)
    cena = models.IntegerField()
    image = StdImageField(upload_to='photos', size=(400, 400), thumbnail_size=(100, 100, True))
    def __unicode__(self):
	return self.nazwa
