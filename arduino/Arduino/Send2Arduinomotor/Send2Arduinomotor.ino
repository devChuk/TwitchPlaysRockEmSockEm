//This code will enable the user to turn an LED attached to an Arduino on and off with 1 and 0 respectively.
/*
int ledPin = 6;

void setup() {
  //Create Serial Object
  Serial.begin(9600);
  //Set pin of led to output
  pinMode(ledPin, OUTPUT);
}

void loop() {
  //Have the arduino wait to receive input
  while (Serial.available() == 0);
  
  //Read the Input
  int val = Serial.read() - '0';
  
  if (val == 1) 
  {
    Serial.println("Led is On"); 
    analogWrite(ledPin, 200);
  }
  else if (val == 0)
  {
    Serial.println("Led is Off");
    analog
    Write(ledPin, 0);
  }
  else
  {
    Serial.println("Invalid!");
  }
  Serial.flush(); 
}
*/

//2-Way motor control

int motorPin1 =  5;    // One motor wire connected to digital pin 5
int motorPin2 =  6;    // One motor wire connected to digital pin 6

// The setup() method runs once, when the sketch starts

void setup()   {                
  // initialize the digital pins as an output:
  pinMode(motorPin1, OUTPUT); 
  pinMode(motorPin2, OUTPUT);  
}

// the loop() method runs over and over again,
// as long as the Arduino has power
void loop()                     
{
  rotateLeft(150, 500);
  rotateRight(50, 1000);
  rotateRight(150, 1000);
  rotateRight(200, 1000);
  rotateLeft(255, 500);
  rotateRight(10, 1500);
}

void rotateLeft(int speedOfRotate, int length){
  analogWrite(motorPin1, speedOfRotate); //rotates motor
  digitalWrite(motorPin2, LOW);    // set the Pin motorPin2 LOW
  delay(length); //waits
  digitalWrite(motorPin1, LOW);    // set the Pin motorPin1 LOW
}

void rotateRight(int speedOfRotate, int length){
  analogWrite(motorPin2, speedOfRotate); //rotates motor
  digitalWrite(motorPin1, LOW);    // set the Pin motorPin1 LOW
  delay(length); //waits
  digitalWrite(motorPin2, LOW);    // set the Pin motorPin2 LOW
}

void rotateLeftFull(int length){
  digitalWrite(motorPin1, HIGH); //rotates motor
  digitalWrite(motorPin2, LOW);    // set the Pin motorPin2 LOW
  delay(length); //waits
  digitalWrite(motorPin1, LOW);    // set the Pin motorPin1 LOW
}

void rotateRightFull(int length){
  digitalWrite(motorPin2, HIGH); //rotates motor
  digitalWrite(motorPin1, LOW);    // set the Pin motorPin1 LOW
  delay(length); //waits
  digitalWrite(motorPin2, LOW);    // set the Pin motorPin2 LOW
}

