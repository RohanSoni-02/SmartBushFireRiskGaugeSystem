int buzzer = 10;
int smokeA0 = A5;
// Your threshold value
int sensorThres = 100;

void setup() {

  pinMode(smokeA0, INPUT);
  Serial.begin(9600);
}

void loop() {
  int analogSensor = analogRead(smokeA0);

  //Serial.print("Pin A0: ");
  Serial.println(analogSensor);
  // Checks if it has reached the threshold value
  /*if (analogSensor > sensorThres)
  {
    tone(buzzer, 1000, 200);
  }
  else
  {
    noTone(buzzer);
  }*/

  
  if (Serial.read() == '3')
  {
    tone(buzzer, 1000, 200);
  }
  if(Serial.read() == '5')
  {
    noTone(buzzer);
  }
  delay(1000);
}
