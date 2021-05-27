import paho.mqtt.client as mqtt
import time
# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

def on_publish(client, userdata, rc):
    print("Connected with result code " + str(rc))


client = mqtt.Client()
#client.on_connect = on_connect
# client.on_message = on_message
#client.on_publish = on_publish

#client.connect("mqtt.eclipse.org", 1883, 60)
client.connect('broker.emqx.io')
print("Publishing message to topic","house/bulbs/bulb1")
while True:

    client.publish("house/bulbs/bulb1","OFF")
    print("Publishing message to topic", "house/bulbs/bulb1 to OFF")
    time.sleep(3)
    client.publish("house/bulbs/bulb1","ON")
    print("Publishing message to topic", "house/bulbs/bulb1 to ON")
    time.sleep(1)


# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
#client.loop_stop()
client.loop_start()
