from django.apps import AppConfig


class ShowApiDataConfig(AppConfig):
    name = 'show_api_data'
    def ready(self):
        #pass
       from sceduler import  sceduler
       #sceduler.start()
