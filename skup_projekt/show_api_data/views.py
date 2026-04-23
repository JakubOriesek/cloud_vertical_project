from django.shortcuts import render
from django.http import HttpResponse
from show_api_data.models import Pocasie
from mqtt_app.models import Esp32_data
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
#import requests
#from sceduler.jobs import pocasie_data
#from sceduler.jobs import pocet
 

def hello_world_view(request):
    return HttpResponse('Hello World')
def BaTable(request):
    # Získame posledných 10 záznamov pre úvodné vykreslenie tabuľky
    posledne_objekty = Pocasie.objects.all().order_by('-id')[:10]
    
    if not posledne_objekty:
        return HttpResponse("Dáta ešte nie sú načítané")
    
    # Do kontextu dáme celý zoznam pod názvom 'posledne_data'
    context = {
        "posledne_data": posledne_objekty,
        "cas_posledneho": posledne_objekty[0].cas  # Pre nadpis h2
    }
    return render(request, 'show_api_data/Batable.html', context)

# Create your views here.
def tab_update1(request):
    last = Pocasie.objects.last()
    return JsonResponse({
        "teplota": last.teplota,
        "vietor": last.vietor,
        "vlhkost": last.vlhkost,
        "tlak": last.tlak,
        "cas": last.cas,
        "o3": last.o3,
        "pocet_update":last.id
    })

def tab_update(request):
    posledne = Pocasie.objects.all().order_by('-id')[:10]
    data = []
    for item in posledne:
        data.append({
            "cas": item.cas.strftime('%Y-%m-%d %H:%M:%S') if item.cas else "",
            "teplota": item.teplota,
            "tlak": item.tlak,
            "vietor": item.vietor,
            "o3": item.o3,
            "vlhkost": item.vlhkost,
            "pocet_update": item.id  # Toto pošle ID záznamu ako "pocet_update" do JS
        })
    return JsonResponse(data, safe=False)

def my_post_view(request):
    if request.method == "POST":
        data = json.loads(request.body)
        print("Received:", data)

        return JsonResponse({"status": "ok"})
    
    return JsonResponse({"error": "Only POST allowed"}, status=405)




@csrf_exempt
def testpost(request):
    if request.method == 'POST':
        print(request.POST)
        # Spracuj dáta
        return JsonResponse({"status": "úspech"})
    
    
def to_front(request):
    posledne = Esp32_data.objects.all().order_by('-id')[:1]
    data = []
    for item in posledne:
        data.append({
            "cas": item.cas,
            "teplota": item.teplota,
            "svetlo": item.svetlo, 
        })
    return JsonResponse(data, safe=False)

