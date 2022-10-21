import paho.mqtt.client as mqtt
 
def on_connect(client, userdata, flags, rc):
     print("Connect with result code " + str(rc))
     client.subscribe("/edge_device/DHTdata")
     client.subscribe("/edge_device/SOILdata")
     client.subscribe("/edge_device/SMOKEdata")
     client.subscribe("/edge_device/FLAMEdata")
     
def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))
    
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("192.168.241.96", 1883, 60)
    # Blocking call that processes network trafftc, dtspatches callbacks and
    # handles reconnecting.
    #Other loop*() functtons are avatlable that give a threaded tnterface and a
    # manual interface.
client.loop_forever()
