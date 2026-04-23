from django.urls import path

from . import views

urlpatterns = [
    path('hello', views.hello_world_view, name= 'hello_world'),
    path('',views.BaTable, name = 'base'),
    
    path('api/data',views.tab_update, name = 'tab_update'),
    path('testpost',views.testpost,name = 'testpost',),
    path('to_front',views.to_front,name = 'to_front',),
]
