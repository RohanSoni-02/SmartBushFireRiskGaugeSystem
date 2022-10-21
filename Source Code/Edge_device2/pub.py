import paho.mqtt.publish as publish
import serial
arduino = serial.Serial('/dev/ttyS0', 9600)
while True:
    data_read_1 = arduino.readline()
    if (int(data_read_1) < 80):
        arduino.write(b'3')
    if (int(data_read_1) > 80):
        arduino.write(b'5')
    publish.single("/edge_device/SMOKEdata", data_read_1, hostname="192.168.241.96")
   