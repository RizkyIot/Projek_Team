#define BLYNK_TEMPLATE_ID "TMPLexPZRD8R"
#define BLYNK_DEVICE_NAME "Smart Home"


#define BLYNK_PRINT Serial
#include <ESP8266WiFi.h>
#include <BlynkSimpleEsp8266.h>

class Opp {
public:
  int sensorValue; //
 
};

char auth[] = "cOEICK6QRjwzcBR_YULDL_H0BjTjZHqx";
char ssid[] = "Android";
char pass[] = "nasi goreng.";

void setup() {
  Serial.begin(9600);
  Blynk.begin(auth, ssid, pass);

  Opp oppObject;


  oppObject.sensorValue = 0;
  Serial.println(oppObject.sensorValue);
}

void loop() {
  Blynk.run();

  
}
