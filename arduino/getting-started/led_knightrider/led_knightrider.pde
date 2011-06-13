#define LED_1 5
#define LED_2 6
#define LED_3 7
#define LED_4 8
#define LED_5 9
#define LED_6 10
#define LED_7 11
#define LED_8 12
#define LED_9 13

#define wait 50

void setup() {
  pinMode(LED_1, OUTPUT);
  pinMode(LED_2, OUTPUT);
  pinMode(LED_3, OUTPUT);
  pinMode(LED_4, OUTPUT);
  pinMode(LED_5, OUTPUT);
  pinMode(LED_6, OUTPUT);
  pinMode(LED_7, OUTPUT);
  pinMode(LED_8, OUTPUT);
  pinMode(LED_9, OUTPUT);

  digitalWrite(LED_1, LOW);
  digitalWrite(LED_2, LOW);
  digitalWrite(LED_3, LOW);
  digitalWrite(LED_4, LOW);
  digitalWrite(LED_5, LOW);
  digitalWrite(LED_6, LOW);
  digitalWrite(LED_7, LOW);
  digitalWrite(LED_8, LOW);
  digitalWrite(LED_9, LOW);
}

void loop() {
  digitalWrite(LED_9, LOW);
  digitalWrite(LED_1, HIGH);
  delay(wait);
  digitalWrite(LED_1, LOW);
  digitalWrite(LED_2, HIGH);
  delay(wait);
  digitalWrite(LED_2, LOW);
  digitalWrite(LED_3, HIGH);
  delay(wait);
  digitalWrite(LED_3, LOW);
  digitalWrite(LED_4, HIGH);
  delay(wait);
  digitalWrite(LED_4, LOW);
  digitalWrite(LED_5, HIGH);
  delay(wait);
  digitalWrite(LED_5, LOW);
  digitalWrite(LED_6, HIGH);
  delay(wait);
  digitalWrite(LED_6, LOW);
  digitalWrite(LED_7, HIGH);
  delay(wait);
  digitalWrite(LED_7, LOW);
  digitalWrite(LED_8, HIGH);
  delay(wait);
  digitalWrite(LED_8, LOW);
  digitalWrite(LED_9, HIGH);
  delay(wait);
  
  digitalWrite(LED_9, LOW);
  digitalWrite(LED_8, HIGH);
  delay(wait);
  digitalWrite(LED_8, LOW);
  digitalWrite(LED_7, HIGH);
  delay(wait);
  digitalWrite(LED_7, LOW);
  digitalWrite(LED_6, HIGH);
  delay(wait);
  digitalWrite(LED_6, LOW);
  digitalWrite(LED_5, HIGH);
  delay(wait);
  digitalWrite(LED_5, LOW);
  digitalWrite(LED_4, HIGH);
  delay(wait);
  digitalWrite(LED_4, LOW);
  digitalWrite(LED_3, HIGH);
  delay(wait);
  digitalWrite(LED_3, LOW);
  digitalWrite(LED_2, HIGH);
  delay(wait);
  digitalWrite(LED_2, LOW);
  digitalWrite(LED_1, HIGH);
}
