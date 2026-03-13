from django.shortcuts import render
from django.http import HttpResponse
from show_api_data.models import Pocasie
#import requests
#from sceduler.jobs import pocasie_data
from sceduler.jobs import pocet
 

def hello_world_view(request):
    return HttpResponse('Hello World')
def BaTable(request):
    posledne = Pocasie.objects.last()  # posledný záznam
    if not posledne:  # ak je stále prázdny
        return HttpResponse("Dáta ešte nie sú načítané")
    
    context = {
        "teplota": posledne.teplota,
        "vietor": posledne.vietor,
        "vlhkost": posledne.vlhkost,
        "tlak": posledne.tlak,
        "cas": posledne.cas,
        "o3": posledne.o3,
        "pocet_update":posledne.pocet
    }
    print(f"posledne: {posledne}")
    print(context)
   
    return render(request, 'show_api_data/Batable.html', context)
    

# Create your views here.
