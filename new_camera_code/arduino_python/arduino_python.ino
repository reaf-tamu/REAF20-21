

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  pinMode(2, OUTPUT);
  pinMode(3, OUTPUT);
  pinMode(4, OUTPUT);
  pinMode(5, OUTPUT);
  pinMode(6, OUTPUT);
  pinMode(7, OUTPUT);
  pinMode(8, OUTPUT);
  pinMode(9, OUTPUT);
  
}

void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available()>0){
    String msg = Serial.readString();
    if(msg =="2"){
      Serial.print("2");
      digitalWrite(2, HIGH);
      delay(1000);
      digitalWrite(2,LOW);
    }
    else if (msg == "3"){
      Serial.print("3");
      digitalWrite(3, HIGH);
      delay(1000);
      digitalWrite(3,LOW);
    }
    else if (msg == "4"){
      Serial.print("4");
      digitalWrite(4, HIGH);
      delay(1000);
      digitalWrite(4,LOW);
    }
    else if (msg == "4"){
      Serial.print("4");
      digitalWrite(4, HIGH);
      delay(1000);
      digitalWrite(4,LOW);
    }
    else if (msg == "5"){
      Serial.print("5");
      digitalWrite(5, HIGH);
      delay(1000);
      digitalWrite(5,LOW);
    }
    else if (msg == "6"){
      Serial.print("6");
      digitalWrite(6, HIGH);
      delay(1000);
      digitalWrite(6,LOW);
    }
    else if (msg == "7"){
      Serial.print("7");
      digitalWrite(7, HIGH);
      delay(1000);
      digitalWrite(7,LOW);
    }
    else if (msg == "8"){
      Serial.print("8");
      digitalWrite(8, HIGH);
      delay(1000);
      digitalWrite(8,LOW);
    }
    else if (msg == "9"){
      Serial.print("9");
      digitalWrite(9, HIGH);
      delay(1000);
      digitalWrite(9,LOW);
    }
    else if (msg == "ALL"){
      digitalWrite(2, HIGH);
      digitalWrite(3, HIGH);
      digitalWrite(4, HIGH);
      digitalWrite(5, HIGH);
      digitalWrite(6, HIGH);
      digitalWrite(7, HIGH);
      digitalWrite(8, HIGH);
      digitalWrite(9, HIGH);       
    }
    else{
      digitalWrite(2,LOW);
      digitalWrite(3,LOW);
      digitalWrite(4,LOW);
      digitalWrite(5,LOW);
      digitalWrite(6,LOW);
      digitalWrite(7,LOW);
      digitalWrite(8,LOW);
      digitalWrite(9,LOW);
      Serial.print("ERROR");
    }
  }
}
