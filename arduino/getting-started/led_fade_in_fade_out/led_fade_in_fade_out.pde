#define LED 9
int level = 0;
int min_level = 5;
int max_level = 255;

void setup() {
  pinMode(LED, OUTPUT);
}

void loop() {
  for (level = min_level; level <= max_level; level++) {
    analogWrite(LED, level);
    delay(10);
  }
  
  for (level = max_level; level >= min_level; level--) {
    analogWrite(LED, level);
    delay(10);
  }
}
