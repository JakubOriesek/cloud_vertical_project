"""
URL configuration for skup_projekt project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def answer_from_api(request):
    return HttpResponse("OK mame pripojenie")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('show_api_data.urls')),
    path('mqtt/',include('mqtt_app.urls')),
    path('answer_from_api/',view=answer_from_api, name='answer_from_api'),
    #path('api/', include('meeting.urls')),  # API endpoint prefix
]
