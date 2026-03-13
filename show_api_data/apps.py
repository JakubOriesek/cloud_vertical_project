from django.apps import AppConfig


class ShowApiDataConfig(AppConfig):
    name = 'show_api_data'
    def ready(self):

        from sceduler import  sceduler
        sceduler.start()
