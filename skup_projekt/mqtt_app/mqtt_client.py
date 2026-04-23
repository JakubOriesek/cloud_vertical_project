import json
import paho.mqtt.client as mqtt
import os
from dotenv import load_dotenv
from mqtt_app.models import Esp32_data

load_dotenv()
MQTT_BROKER = "172.26.48.1"
MQTT_PORT = int(os.getenv('MQTT_PORT'))
MQTT_USERNAME = os.getenv('MQTT_USERNAME')
MQTT_PASSWORD = os.getenv('MQTT_PASSWORD')
MQTT_TOPIC = os.getenv('MQTT_TOPIC')

# Add 'properties' as the 5th argument
def on_connect(client, userdata, flags, rc, properties=None):
    if rc == 0:
        print("Connected to MQTT Broker")
        client.subscribe('test_topic')
    else: 
        print(f"Connection failed with code {rc}")

def on_message(client, userdata, msg):
    try:
        message = json.loads(msg.payload.decode("utf-8"))
        print(f"received message: {message}")
        Esp32_data.objects.create(
            teplota = message.get("temp"),
            svetlo = message.get("light")
        )
        
    except json.JSONDecodeError:
        print("Error decoding MQTT message")
    except Exception as e:
        print(f"Error processing message: {e}")
        
def on_disconnect(client, userdata, rc):
    print("Disconected from MQTT Broker")
    
#create and configure MQTT client
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_connect = on_connect
client.on_message = on_message
client.on_disconnect = on_disconnect

# This part in your mqtt_client.py handles the security:
if MQTT_USERNAME and MQTT_PASSWORD:
    client.username_pw_set(MQTT_USERNAME, MQTT_PASSWORD)

def start_mqtt():
    try:
        print(f"Connecting to Broker at {MQTT_BROKER}...")
        client.connect(MQTT_BROKER, MQTT_PORT, 60)
        client.loop_start()
    except Exception as e:
        print(f"MQTT Connection Error: {e}")