from flask import Flask,request,render_template, Markup
import paho.mqtt.publish as publish
import time
import pymysql



dbConn = pymysql.connect("localhost","pi","", "iot_db") or die("could not load database")
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/changeLCD")
def form():
    publish.single("/status/buzzer", 1, hostname="192.168.241.77")
    return render_template('index.html', template = "Active")

@app.route("/changeLCD0")
def formoff():
    publish.single("/status/buzzeroff", 0, hostname="192.168.241.77")
    return render_template('index.html', template = "Deactive")
@app.route('/mean_temperature')
def tempmean():
    with dbConn:
        cur = dbConn.cursor()
        cur.execute("SELECT ROUND(AVG(moistLevel),2) from sensorLog")
        data1 = cur.fetchone()
        cur.execute("SELECT MIN(moistLevel) from sensorLog")
        data2 = cur.fetchone()
        cur.execute("SELECT MAX(moistLevel) from sensorLog")
        data3 = cur.fetchone()
        dbConn.commit()
        cur.close()
    return render_template('index.html',averageTemp = data1[0],minTemp = data2[0], maxTemp = data3[0])
  

@app.route('/mean_humidity')
def temphumd():
    with dbConn:
        cur = dbConn.cursor()
        cur.execute("SELECT ROUND(AVG(humidLevel),2) from sensorLog")
        data1 = cur.fetchone()
        cur.execute("SELECT MIN(humidLevel) from sensorLog")
        data2 = cur.fetchone()
        cur.execute("SELECT MAX(humidLevel) from sensorLog")
        data3 = cur.fetchone()
        dbConn.commit()
        cur.close()
    return render_template('index.html',avgHumd = data1[0], minHumd = data2[0], maxHumd = data3[0])

@app.route('/mean_moisture')
def tempmoist():
    with dbConn:
        cur = dbConn.cursor()
        cur.execute("SELECT ROUND(AVG(soilmoistLevel),2) from sensorLog")
        data1 = cur.fetchone()
        cur.execute("SELECT MIN(soilmoistLevel) from sensorLog")
        data2 = cur.fetchone()
        cur.execute("SELECT MAX(soilmoistLevel) from sensorLog")
        data3 = cur.fetchone()
        dbConn.commit()
        cur.close()
    return render_template('index.html',avgMoist = data1[0], minMoist = data2[0], maxMoist = data3[0])
@app.route('/line')
def line():
    moisture = []
    humidity = []
    with dbConn:
        cursor = dbConn.cursor()
        cursor.execute("SELECT soilmoistLevel from sensorLog LIMIT 10")
        data = cursor.fetchall()
        
        for row in data:
            moisture.append(row[0])
        print(moisture)
            
        cursor.execute("SELECT humidLevel from sensorLog LIMIT 10")
        data = cursor.fetchall()
        
        for row in data:
            humidity.append(row[0])
        print(humidity)
        cursor.close()
    line_labels = humidity
    line_values = moisture
    return render_template('index.html', title = 'Analytics', max = 100, labels = line_labels, values=line_values)

if __name__=='__main__':
    app.run(host='0.0.0.0', port = 8080, debug = True)
    