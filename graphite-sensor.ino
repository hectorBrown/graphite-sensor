const int adcPin = 34;


void setup() {
  Serial.begin(9600);
  analogSetAttenuation(ADC_11db);   
  analogSetWidth(12);

}

void loop() {
  float rawValue = analogRead(adcPin);
  float voltage = 3.3f * (rawValue / 4095);
  Serial.println(voltage);
  delay(10);
}
