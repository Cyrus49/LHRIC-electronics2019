#define SOLENOID 5
#define switchPin 3

void setup() {
  // put your setup code here, to run once:

  Serial.begin(9600);
  pinMode(SOLENOID, OUTPUT);      // pin 5 is output
  //pinMode(switchPin, INPUT_PULLUP);

}

void loop() {
  // put your main code here, to run repeatedly:

  digitalWrite(SOLENOID, HIGH);      // ON
  delay(2000);                       // Wait 2 Seconds
  digitalWrite(SOLENOID, LOW);       // OFF
  delay(2000);                       // Wait 2 Seconds
    
}
