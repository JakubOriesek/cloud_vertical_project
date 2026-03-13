import requests
from show_api_data.models import Pocasie
from django.utils.dateparse import parse_datetime
pocet = [0]
pocasie_data = []
def job_get_api():
    global pocasie_data
    global pocet
    url ='https://api.waqi.info/feed/bratislava/?token=demo'
    response = requests.get(url)
    data = response.json()
    
    t = data["data"]["iaqi"]["t"]["v"]
    vietor =data["data"]["iaqi"]["w"]["v"]
    vlhkost = data["data"]["iaqi"]["h"]["v"]
    tlak = data["data"]["iaqi"]["p"]["v"]
    cas = data["data"]["time"]["s"]
    o3 = data["data"]["iaqi"]["o3"]["v"]
    
    pocasie_data[:] = [t, vietor, vlhkost, tlak, cas, o3]
    pocet[0] += 1
        # Uloženie do databázy
        
    cas = parse_datetime(cas)
    Pocasie.objects.create(
        cas=cas,
        teplota=t,
        vietor=vietor,
        vlhkost=vlhkost,
        tlak=tlak,
        o3=o3,
        pocet = pocet[0],
    )

    #print(f"Dáta uložené do DB, počet aktualizácií: {pocet[0]}")
    print(f"Dáta aktualizované cas: {cas}")
    
