// Pin Definitions
const int potPin = A0;   // Analog input pin connected to the potentiometer
const int ledPin = 9;    // PWM output pin connected to the LED (Use pins with ~ symbol)

int sensorValue = 0;     // Variable to store the raw value (0-1023)
int outputValue = 0;     // Variable to store the scaled PWM value (0-255)

void setup() {
  // PWM pins don't strictly require pinMode for analogWrite, 
  // but it's good practice.
  pinMode(ledPin, OUTPUT);
  Serial.begin(9600); // Optional: For debugging in the Serial Monitor
}

void loop() {
  // 1. Read the analog input (0 to 1023)
  sensorValue = analogRead(potPin);

  // 2. Map the value to the PWM range (0 to 255)
  // map(value, fromLow, fromHigh, toLow, toHigh)
  outputValue = map(sensorValue, 0, 1023, 0, 255);

  // 3. Output the PWM signal to the LED
  analogWrite(ledPin, outputValue);

  // Optional: Print values to Serial Monitor to help with your lab report
  Serial.print("Potentiometer: ");
  Serial.print(sensorValue);
  Serial.print(" -> PWM Output: ");
  Serial.println(outputValue);

  delay(10); // Small delay for stability
}
