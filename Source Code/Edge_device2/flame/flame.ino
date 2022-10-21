// lowest and highest sensor readings:
const int sensorMin = 0;     // sensor minimum
const int sensorMax = 1024;  // sensor maximum
#include <LiquidCrystal.h>
LiquidCrystal lcd(7, 6, 5, 4, 3, 2);

void setup() {
  // initialize serial communication @ 9600 baud:
  Serial.begin(9600);
  lcd.begin(16, 2);
  lcd.print("Flame:");  
}
void loop() {
  lcd.setCursor(0, 1);
  if (!analogRead(A0)) {
    lcd.print("ERROR");
    return;
  }
  // read the sensor on analog A0:
  int sensorReading = analogRead(A0);
  // map the sensor range (four options):
  // ex: 'long int map(long int, long int, long int, long int, long int)'
  int range = map(sensorReading, sensorMin, sensorMax, 0, 3);

  

  //lcd.print(sensorReading);
  // range value:
  switch (range) {
  case 0:    // A fire closer than 1.5 feet away.
    lcd.print("** Close Fire **");
    break;
  case 1:    // A fire between 1-3 feet away.
    lcd.print("** Distant Fire **");
    break;
  case 2:    // No fire detected.
    lcd.print("No Fire");
    break;
  }
  
  Serial.println(analogRead(A0));
  delay(1000);  // delay between reads
}
