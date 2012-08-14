# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
from produkt.models import *
from django.core.paginator import Paginator

Kategorie = Kategoria.objects.all()
produkty = Produkt.objects.all()

def index(request):
    produkty = Produkt.objects.all()
    p = Paginator(produkty, 2)
    if request.GET :
	page = p.page(request.GET.get('page'))
    else :
	page = p.page(1)
    return render_to_response('produkt_list.html',
                             {'produkty': page, 'Kategorie': Kategorie})

def kategoria(request, kategoria):
    katrgoria_id = Kategoria.objects.get(nazwa = kategoria)
    produkty = Produkt.objects.filter(kategoria_id = katrgoria_id.id)
    p = Paginator(produkty, 2)
    if request.GET :
	page = p.page(request.GET.get('page'))
    else :
	page = p.page(1)
    return render_to_response('produkt_list.html',
                             {'produkty': page, 'Kategorie': Kategorie})
