from django.apps import AppConfig
import sys

class MqttAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mqtt_app'

    def ready(self):
        # This prevents the client from starting twice during development
        if 'runserver' in sys.argv:
            from . import mqtt_client
            mqtt_client.start_mqtt()