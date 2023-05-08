#define BUTTON_PIN 33
int lastState = HIGH;
int currentState;
int bVal;

void setup() {
  Serial.begin(9600);
  pinMode(BUTTON_PIN, INPUT_PULLUP);
}

void loop() {
  int xVal = analogRead(26);
  int yVal = analogRead(27);
  currentState = digitalRead(BUTTON_PIN);

  if (lastState == LOW && currentState == HIGH){
    Serial.println("0");
  }

  if (xVal == 0){
    Serial.println("1");
  }

  lastState = currentState;

  delay(100);
}