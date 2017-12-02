#! /home/graham/.PythonEnvs/mqtttts/bin/python

# Basic script for saying and displaying messaged received my MQTT

import paho.mqtt.client as mqtt
from espeakng import ESpeakNG

esng = ESpeakNG()
esng.voice = 'english-mb-en1'
esng.speed = 135

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("NAOS-PC/tts")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    if msg.topic == "NAOS-PC/tts":
        esng.say(msg.payload.decode("utf-8"))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("raspberrypi.local", 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()
