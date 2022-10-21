import paho.mqtt.client as mqtt
import serial
arduino = serial.Serial('/dev/ttyS0', 9600)
 
def on_connect(client, userdata, flags, rc):
     print("Connect with result code " + str(rc))
     client.subscribe("/edge_device/SOILdata")
     client.subscribe("/edge_device/DHTdata")
     client.subscribe("/edge_device/FLAMEdata")
     client.subscribe("/cloud/SMOKEdata")
     client.subscribe("/status/buzzer")
     client.subscribe("/status/buzzeroff")
    # The callback for when a PUBLISH message ts recetved from the server.
def on_message (client, userdata, msg) :
    print(msg.topic + " " + str(msg.payload))
    
    if(msg.topic == '/status/buzzer'):
        if(msg.payload == 1):
            ser.write(b'3')
            
    if(msg.topic == '/status/buzzeroff'):
        if(msg.payload == 0):
            ser.write(b'5')
    
   
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("192.168.241.96", 1883, 60)
client.connect("192.168.241.77", 1883, 60)
    # Blocking call that processes network trafftc, dtspatches callbacks and
    # handles reconnecting.
    #Other loop*() functtons are avatlable that give a threaded tnterface and a
    # manual interface.
client.loop_forever()
