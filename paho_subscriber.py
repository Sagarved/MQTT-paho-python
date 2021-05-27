import paho.mqtt.client as mqtt

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

client = mqtt.Client()
#client.on_connect = on_connect
client.on_message = on_message

#client.connect("mqtt.eclipse.org", 1883, 60)
client.connect('broker.emqx.io')
client.subscribe("house/bulbs/bulb1")

#client.loop_stop()
client.loop_forever()
