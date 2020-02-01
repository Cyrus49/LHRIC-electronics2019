// CAR GEARS GO LIKE THIS: 1, N, 2, 3, 4, 5, 6

#define SOLENOID1 5
#define SOLENOID2 6

#define button1 3
#define button2 4
#define button3 8

int pressed1 = 0;
int pressed2 = 0;
int pressed3 = 0;
int currentGear = 1;
int delays[] = {100, 100, 100, 100, 100, 100, 100};

void setup() {
  // put your setup code here, to run once:

  Serial.begin(9600);
  pinMode(SOLENOID1, OUTPUT);      // pin 5 is output
  pinMode(SOLENOID2, OUTPUT);      // pin 5 is output
  //pinMode(switchPin, INPUT_PULLUP);
  pinMode(button1, INPUT_PULLUP);
  pinMode(button2, INPUT_PULLUP);
  pinMode(button3, INPUT_PULLUP);
  
}

void upShift() { // default code to upshift one time
    currentGear = min(6, currentGear + 1);
    digitalWrite(SOLENOID1, HIGH);      // ON
    delay(delays[currentGear]);
    pressed1 = 1;
    digitalWrite(SOLENOID1, LOW);
    Serial.println("UPSHIFT");
    Serial.println(currentGear);
}

void downShift() { // default code to downshift one time
    currentGear = max(0, currentGear - 1);
    digitalWrite(SOLENOID2, HIGH); 
    delay(delays[currentGear]);
    pressed2 = 1;
    digitalWrite(SOLENOID2, LOW);
    Serial.println("DOWNSHIFT");
    Serial.println(currentGear);
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
  
  if(digitalRead(button1) == LOW && !pressed1 && currentGear < 7) {   // Will upshift when button is pressed, ignoring neutral gear
    if (currentGear == 0) {
      upShift();
      upShift();
    }
    else {
      upShift();
    }
  }
  

  else if(digitalRead(button2) == LOW && !pressed2 && currentGear > 0) {  // Will down when button is pressed, ignoring neutral gear
    if (currentGear == 2) {
      downShift();
      downShift();
    }
    else {
      downShift();
    }
  }

  else if(digitalRead(button3) == LOW && !pressed3) { // puts car in neutral gear
   if (currentGear == 0) {
    upShift();
   }
   else {
    while (currentGear != 1) {
      downShift();
    }
   }
  }

  if (digitalRead(button1) == HIGH) {
    pressed1 = 0;
  }
  if (digitalRead(button2) == HIGH) {
    pressed2 = 0;
  }

  // for Neutral
  if (digitalRead(button3) == HIGH) {
    pressed3 = 0;
  }
  // When pressing Netral Button shift into Neutral from whatever the current gear is
  
    
}
