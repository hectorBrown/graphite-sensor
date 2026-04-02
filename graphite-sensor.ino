#include<cstdio>

const int adcPin = 34;
const int time_step = 5;
int ms_time = 0;

void setup() {
  Serial.begin(9600);
  analogSetAttenuation(ADC_11db);   
  analogSetWidth(12);
}

void loop() {

  float rawValue = analogRead(adcPin);
  Serial.print(rawValue);
  Serial.print(",");
  Serial.println(ms_time);
  delay(time_step);
  ms_time += time_step;
}
