import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import pymysql

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe("/edge_device/DHTdata")
    client.subscribe("/edge_device/SOILdata")
    client.subscribe("/edge_device/SMOKEdata")
    client.subscribe("/edge_device/FLAMEdata")

def on_message(client, userdata, msg):
   
    
    if (msg.topic == "/edge_device/DHTdata"):
        publish.single("/cloud/DHTdata", str(msg.payload), hostname="192.168.241.96")
        hum = str(msg.payload)
        temp = str(msg.payload)
    
    if (msg.topic == "/edge_device/SOILdata"):
        publish.single("/cloud/SOILdata", str(msg.payload), hostname="192.168.241.96")
        soilMoist = str(msg.payload)
        
    if (msg.topic == "/edge_device/SMOKEdata"):
        publish.single("/cloud/SMOKEdata", str(msg.payload), hostname="192.168.241.96")
        gasLevel = str(msg.payload)
        
    if (msg.topic == "/edge_device/FLAMEdata"):
        publish.single("/cloud/FLAMEdata", str(msg.payload), hostname="192.168.241.96")
        fireThreshold = str(msg.payload)
    
    dbConn = pymysql.connect("localhost", "pi", "", "iot_db" or die("Could not load the database"))
    
    print(msg.topic + " " + str(msg.payload))
    
    #fireThreshold = 0;
    #gasLevel = 0;
    #soilMoist = 0;
    #temp = 0;
    #hum = 0;

    #if((fireThreshold!= 0) and (gasLevel != 0) and (soilMoist != 0)):
    #if((fireThreshold != 0) and (gasLevel != 0) ):
    with dbConn:
        cursor = dbConn.cursor()
        cursor.execute("INSERT INTO sensorLog(smokeLevel, fireThreshold, moistLevel, humidLevel, soilmoistLevel) VALUES (%s, %s, %s, %s, %s)" %(gasLevel, fireThreshold, hum, temp, soilMoist))
        dbConn.commit()
        cursor.close()


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("192.168.241.96", 1883, 60)

client.loop_forever()