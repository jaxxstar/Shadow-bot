 #include <Arduino.h>

int motorfwd=8;
int motorbwd=9;
//int motorspeed=23;
int motora=11;
int motorb=12;
void setup()
{ Serial.begin(9600);
  Serial.println("hi");
  pinMode(motorfwd,OUTPUT);
 // pinMode(motorspeed,OUTPUT);
  pinMode(motorbwd,OUTPUT);
  pinMode(motora,INPUT);
  pinMode(motorb,INPUT);
 
}
void loop()
{
  //digitalWrite(motorspeed,HIGH);
  digitalWrite(motorfwd,HIGH);
  digitalWrite(motorbwd,LOW);
  Serial.print(digitalRead(motora));
  Serial.print("    ");
  Serial.println(digitalRead(motorb));
  
}
