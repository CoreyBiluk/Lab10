/*EETG 3024 Advanced Embedded Systems
  Instructor: Ricardo Bautista Quintero
  Corey Biluk | W0425561
  Lab 10 | Part 4
  March 8, 2021*/

// Variables for analog values
int analogVal1 = 0;
int analogVal2 = 0;

void setup() {
  Serial.begin(9600);           // Initialize Serial comms @ 9600 baudrate
}
void loop() {
  
  analogVal1 = analogRead(A0);  // Read input A0 and save value
  analogVal2 = analogRead(A1);  // Read input A1 and save value
  Serial.print(analogVal1);     // Print analog value 1 to Serial
  Serial.print(" , ");          // Print "," to serial.  This is used to split the transmitted data
  Serial.println(analogVal2);   // Print analog value 2 to Serial followed by carriage return/new line
  delay(1000);                  // 1 sec delay
}
