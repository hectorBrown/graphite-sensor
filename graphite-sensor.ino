#include<cstdio>

const int adcPin = 34;
const int time_step = 5;

void setup() {
  Serial.begin(9600);
  analogSetAttenuation(ADC_11db);   
  analogSetWidth(12);
}

void loop() {

  Serial.print(analogRead(adcPin));
  Serial.print(",");
  Serial.println(millis());
  delay(time_step);
}
