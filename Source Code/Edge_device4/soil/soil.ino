#include <Servo.h>
Servo myservo; 
int pos = 0; 
void setup(){
  
  Serial.begin(9600);
  pinMode(2, OUTPUT);
  myservo.attach(9);
}

void loop(){

  //Serial.print("Moisture Sensor Value:");
  Serial.println(analogRead(A0));

  if (Serial.read() == '2')
  {
    digitalWrite(2, HIGH);
    for (pos = 0; pos <= 180; pos++){ // goes from 0 degrees to 180 degrees
    // in steps of 1 degree
      myservo.write(pos);              // tell servo to go to position in variable 'pos'                      // waits 15ms for the servo to reach the position
        delay(15);
    }
    for (pos = 180; pos >= 0; pos--) { // goes from 180 degrees to 0 degrees
      myservo.write(pos);              // tell servo to go to position in variable 'pos'                      // waits 15ms for the servo to reach the position
      delay(15);
    }
    
  }
  else
  {
    digitalWrite(2, LOW);
    myservo.write(0);
  }
  delay(1000);

}
