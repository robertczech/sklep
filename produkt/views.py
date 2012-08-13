# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
from produkt.models import *
from django.core.paginator import Paginator

def index(request):
    produkty = Produkt.objects.all()

    p = Paginator(produkty, 2)
    if request.GET :
	page = p.page(request.GET.get('page'))
    else :
	page = p.page(1)
    return render_to_response('index.html',
                             {'produkty': page })
