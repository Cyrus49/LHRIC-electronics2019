#define SOLENOID1 5
#define SOLENOID2 6

#define button1 3
#define button2 4

int pressed1 = 0;
int pressed2 = 0;
int currentGear = 0;
int delays[] = {100, 100, 100, 100, 100, 100, 100};

void setup() {
  // put your setup code here, to run once:

  Serial.begin(9600);
  pinMode(SOLENOID1, OUTPUT);      // pin 5 is output
  pinMode(SOLENOID2, OUTPUT);      // pin 5 is output
  //pinMode(switchPin, INPUT_PULLUP);
  pinMode(button1, INPUT_PULLUP);
  pinMode(button2, INPUT_PULLUP);
  

}

void loop() {
  // put your main code here, to run repeatedly:

  // if up button --> set one solenoid high and other low
  // if down button --> set one solenoid high, other low

  // need to measure distance 
  //int buttonState1 = digitalRead(button1);
  //int buttonState2 = digitalRead(button2);

  //Serial.println(pressed1);
  //Serial.println(pressed2 + " button2 " );
  
  if(digitalRead(button1) == LOW && !pressed1 && currentGear < 6) {   // upshifting
    //pressed1 = 1;
    currentGear = min(6, currentGear + 1);
    digitalWrite(SOLENOID1, HIGH);      // ON
    delay(delays[currentGear]);
    pressed2 = 1;
    pressed1 = 1;
    digitalWrite(SOLENOID1, LOW);
    Serial.println("UPSHIFT");
    Serial.println(currentGear);
  }

  else if(digitalRead(button2) == LOW && !pressed2 && currentGear > 0) {  // downshifting
    //pressed2 = 1;
    currentGear = max(0, currentGear - 1);
    digitalWrite(SOLENOID2, HIGH); 
    delay(delays[currentGear]);
    pressed2 = 1;
    pressed1 = 1;
    digitalWrite(SOLENOID2, LOW);
    Serial.println("DOWNSHIFT");
    Serial.println(currentGear);
  }

  if (digitalRead(button1) == HIGH) {
    pressed1 = 0;
  }
  if (digitalRead(button2) == HIGH) {
    pressed2 = 0;
  }

  // for N
  if (currentGear == 1) {
    
  }
  // if below certain RPM && hold downshift for 1 sec, then go into N
  
  
    
}
