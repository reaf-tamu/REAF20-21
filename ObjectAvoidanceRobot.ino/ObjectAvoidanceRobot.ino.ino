int greenLeft = 13;
int redLeft = 12;
int greenRight = 11;
int redRight = 10;

int in1=7;    // IN1 (yellow) --> Arduino D7
int in2=6;    // IN2 (orange) --> Arduino D6
int in3=5;    // IN3 (red)    --> Arduino D5 
int in4=4;    // IN4 (brown)  --> Arduino D4

int rx = 2;  // Define the ultrasound signal receiving a Pin
int tx = 3;  //Define the ultrasound signal emission Pin

int enA = 8;   //purple
int enB = 10;

int wheelspeed = 0;
int setpoint = 30;   //[cm]
float oldTime = 0;
float newTime = 0;
float timeInterval = 0;
float error = 0;
float derror =0;
float accerror= 0;
float olderror = 0;
int kp = 5;
int ki = 1;
int kd = 0;

void setup() {

  Serial.begin(9600);     // Initialize 
  pinMode(in1, OUTPUT);
  pinMode(in2, OUTPUT);
  pinMode(in3, OUTPUT);
  pinMode(in4, OUTPUT);
  pinMode(enA, OUTPUT);
  pinMode(enB, OUTPUT);
  
  pinMode(rx, INPUT);    // Define the ultrasound enter pin
  pinMode(tx, OUTPUT);  // Define the ultrasound output pin   

  pinMode(10, OUTPUT);  //LED
  pinMode(11, OUTPUT);
  pinMode(12, OUTPUT);
  pinMode(13, OUTPUT);
}

float getDistance(){
  digitalWrite(tx, LOW);   // For low voltage 2 us ultrasonic launch
  delayMicroseconds(2);
  digitalWrite(tx, HIGH);  // Let ultrasonic launch 10 us high voltage, there is at least 10 us
  delayMicroseconds(10);
  digitalWrite(tx, LOW);    // Maintaining low voltage ultrasonic launch
  float distance = pulseIn(rx, HIGH);  // Read the time difference
  distance= distance/5.8/10;     //Will be time to distance distance (unit: cm)
  //Serial.print("\n Distance:");   //The output distance (unit: cm)
  //Serial.print(distance);         //According to the distance
  return distance;
}

int pid(){
  newTime = millis()/1000;
  error = -setpoint + getDistance();
  timeInterval = newTime - oldTime;
  accerror+= error*timeInterval;
  derror = (error - olderror)/timeInterval;
  int out = error*kp  + (ki*accerror) + (kd*derror);
  Serial.print("\n out:");   //The output distance (unit: cm)
  Serial.print(error);         //According to the distance
  if(out > 300){
    out = 300;}
  wheelspeed = map(out,0,300,0,255);
  Serial.print("\n wheel speed:");   //The output distance (unit: cm)
  Serial.print(wheelspeed);         //According to the distance
  olderror = error;
  oldTime = newTime;
  return int(wheelspeed);
}


void speedControl(int sped) {
  analogWrite(enA,abs(sped));
  analogWrite(enB,abs(sped));
  if(sped<0){
    digitalWrite(in1, LOW);
    digitalWrite(in2, HIGH);
    digitalWrite(in3, LOW);
    digitalWrite(in4, HIGH);
    Serial.print("\n BACKWARDS");  
  }
  else{
    digitalWrite(in1, HIGH);
    digitalWrite(in2, LOW);
    digitalWrite(in3, HIGH);
    digitalWrite(in4, LOW);
    Serial.print("\n FORWARD");  
  }
}

void loop() {
  // put your main code here, to run repeatedly:
  speedControl(pid());
  delay(1000);
}
