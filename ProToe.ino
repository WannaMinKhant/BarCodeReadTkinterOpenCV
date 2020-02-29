#include<LiquidCrystal_I2C_Hangul.h>
#include<Wire.h>

LiquidCrystal_I2C_Hangul lcd(0x27,20,4); //LCD 클래스 초기화

int buzzerPin = 7;
int relay = 8;
int pass = 5;
int block = 6;
String recieveData;
char c;

void setup ()
{
  Serial.begin(9600);
  lcd.init();
  lcd.backlight();
  lcd.print("test");
  pinMode (buzzerPin, OUTPUT);
  pinMode(relay, OUTPUT);
  pinMode(pass, OUTPUT);
  pinMode(block, OUTPUT);
  digitalWrite (relay, LOW);
  digitalWrite (pass, LOW);
  digitalWrite (block, LOW);
  digitalWrite (buzzerPin, LOW);
  
}

void loop ()
{
  if (Serial.available()) {
    c = Serial.read();
    lcd.setCursor(1,1);
    lcd.print(c);
    if (c == '1') {
      digitalWrite (buzzerPin, LOW);
      digitalWrite (relay, LOW);
      digitalWrite (pass, HIGH);

    } else if (c == '0') {
      digitalWrite (block, HIGH);
      digitalWrite (buzzerPin, LOW);
      delay(200);
      digitalWrite (buzzerPin, HIGH);
      delay(200);
      digitalWrite (buzzerPin, LOW);
      delay(200);
      digitalWrite (buzzerPin, HIGH);
      delay(200);
      digitalWrite (buzzerPin, LOW);
      delay(200);
      digitalWrite (buzzerPin, HIGH);
      delay(200);
      digitalWrite (buzzerPin, LOW);
    }
  }
  delay(500);
  digitalWrite (buzzerPin, HIGH);
  delay (2000);
  digitalWrite (relay, HIGH);
  digitalWrite (pass, LOW);
  digitalWrite (block, LOW);
  digitalWrite (buzzerPin, HIGH);
  delay (500);
}
