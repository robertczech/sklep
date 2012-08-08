# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
from produkt.models import *

def index(request):
    produkty = Produkt.objects.all()
    return render_to_response('index.html',
                             {'produkty': produkty})
