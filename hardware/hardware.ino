#include <Adafruit_ILI9341.h>

//##################################################################################################################
//##                                      SMART FARMING SOLUTIONS                                                 ##
//##                                                                                                              ##
//##################################################################################################################

 

// IMPORT ALL REQUIRED LIBRARIES
#include "Arduino.h"
#include <rom/rtc.h>
#include <ArduinoJson.h>
#include <math.h>  // https://www.tutorialspoint.com/c_standard_library/math_h.htm
#include <FastLED.h>

#include <SPI.h>
#include <Wire.h>
#include "Adafruit_GFX.h"
#include "Adafruit_ILI9341.h"
// #include <Adafruit_BMP280.h>
#include "DHT.h"

#ifndef _WIFI_H 
#include <WiFi.h>
#include <HTTPClient.h>
#endif

#ifndef STDLIB_H
#include <stdlib.h>
#endif

#ifndef STDIO_H
#include <stdio.h>
#endif

#ifndef ARDUINO_H
#include <Arduino.h>
#endif 

#define NUM_LEDS 7
#define DATA_PIN 26
 
// DEFINE VARIABLES
#define ARDUINOJSON_USE_DOUBLE      1 

// DEFINE THE CONTROL PINS FOR THE DHT22 
#define DHTPIN 4 //datapin of sensor
#define DHTPIN2 22 //datapin of sensor

#define DHTTYPE DHT22 // define the type of sensor



#define trig1Pin  2
#define echo1Pin  36
#define trig2Pin  25
#define echo2Pin  39


#define TFT_DC    17
#define TFT_CS    5
#define TFT_RST   16
#define TFT_CLK   18
#define TFT_MOSI  23
#define TFT_MISO  19

//----------------------------------------Defines colors
// Assign human-readable names to some common 16-bit color values:
#define BLACK       0x0000
#define BLUE        0x001F
#define RED         0xF800
#define GREEN       0x07E0
#define CYAN        0x07FF
#define MAGENTA     0xF81F
#define YELLOW      0xFFE0
#define WHITE       0xFFFF
#define AQUA        0x04FF
#define ORANGE      0xFD20
#define DARKORANGE  0xFB60
#define MAROON      0x7800
#define BLACKM      0x18E3
#include <Fonts/FreeSansBold18pt7b.h>
#include <Fonts/FreeSansBold9pt7b.h> 

#define RED2RED 0
#define GREEN2GREEN 1
#define BLUE2BLUE 2
#define BLUE2RED 3
#define GREEN2RED 4
#define RED2GREEN 5


double h=0;
double t=0;
double hi;

double h2=0;
double t2=0;
double hi2;

double f=0;
double pa;

int AirValue = 3999;  //you need to replace this value with Value_1
int WaterValue = 1999;  //you need to replace this value with Value_2
int soilMoistureValue = 0;
int soilmoisturepercent=0;

int soilMoistureValue2 = 0;
int soilmoisturepercent2 =0;

uint32_t runTime = -99999;       // time for next update
int reading1 = 0; // Value to be displayed
int d = 0; // Variable used for the sinewave test waveform
boolean alert = 0;
int8_t ramp = 1;
int tesmod =0;
long duration, radarValue, radarValue2;
double waterheight, fertilizerheight;

char TempCelciusFahrenheit[6];

float tempF = 0;



// MQTT CLIENT CONFIG  
static const char* pubtopic      = "620154701";                    // Add your ID number here
static const char* subtopic[]    = {"620154701_sub","/elet2415"};  // Array of Topics(Strings) to subscribe to
// static const char* mqtt_server   = "dbs.msjrealtms.com";         // Broker IP address or Domain name as a String 
static const char* mqtt_server   = "www.yanacreations.com";         // Broker IP address or Domain name as a String 
static uint16_t mqtt_port        = 1883;

// WIFI CREDENTIALS
const char* ssid       = "ARRIS-34A2" ; // Add your Wi-Fi ssid
const char* password   = "BPM7EW600194"; // Add your Wi-Fi password 



// TASK HANDLES 
TaskHandle_t xMQTT_Connect          = NULL; 
TaskHandle_t xNTPHandle             = NULL;  
TaskHandle_t xLOOPHandle            = NULL;  
TaskHandle_t xUpdateHandle          = NULL;
TaskHandle_t xButtonCheckeHandle    = NULL; 



// FUNCTION DECLARATION   
void checkHEAP(const char* Name);   // RETURN REMAINING HEAP SIZE FOR A TASK
void initMQTT(void);                // CONFIG AND INITIALIZE MQTT PROTOCOL
unsigned long getTimeStamp(void);   // GET 10 DIGIT TIMESTAMP FOR CURRENT TIME
void callback(char* topic, byte* payload, unsigned int length);
void initialize(void);
bool publish(const char *topic, const char *payload); // PUBLISH MQTT MESSAGE(PAYLOAD) TO A TOPIC
void vButtonCheck( void * pvParameters );
void vUpdate( void * pvParameters ); 


/* Init class Instances for the DHT22 etcc */
 DHT dht(DHTPIN,DHTTYPE);
 DHT dht2(DHTPIN2,DHTTYPE);

 CRGB leds[NUM_LEDS];

//############### IMPORT HEADER FILES ##################
#ifndef NTP_H
#include "NTP.h"
#endif

#ifndef MQTT_H
#include "mqtt.h"
#endif

#ifndef FORECAST_H
#include "foreCast.h"
#endif

#define analogPin A4
#define analogPin2 A5



/* Initialize class objects*/
Adafruit_ILI9341 tft = Adafruit_ILI9341(TFT_CS, TFT_DC, TFT_MOSI, TFT_CLK, TFT_RST, TFT_MISO);
// Adafruit_BMP280 bmp; // use I2C interface
// Adafruit_Sensor *bmp_temp = bmp.getTemperatureSensor();
// Adafruit_Sensor *bmp_pressure = bmp.getPressureSensor();


void setup() {
  Serial.begin(115200);  // INIT SERIAL  

  /* TFT DISPLAY SET UP */
  dht.begin();
  dht2.begin();
  tft.begin();
  pinMode(trig1Pin, OUTPUT);
  pinMode(echo1Pin, INPUT);
  pinMode(trig2Pin, OUTPUT);
  pinMode(echo2Pin, INPUT);
  tft.setRotation(1);

  LEDS.addLeds<WS2812, DATA_PIN, GRB>(leds, NUM_LEDS);



  tft.fillScreen(RED); 

  // bmp.setSampling(Adafruit_BMP280::MODE_NORMAL,     /* Operating Mode. */
  //                 Adafruit_BMP280::SAMPLING_X2,     /* Temp. oversampling */
  //                 Adafruit_BMP280::SAMPLING_X16,    /* Pressure oversampling */
  //                 Adafruit_BMP280::FILTER_X16,      /* Filtering. */
  //                 Adafruit_BMP280::STANDBY_MS_500); /* Standby time. */

  // bmp_temp->printSensorDetails();

  initialize();           // INIT WIFI, MQTT & NTP 

  //vButtonCheckFunction(); // UNCOMMENT IF USING BUTTONS THEN ADD LOGIC FOR INTERFACING WITH BUTTONS IN THE vButtonCheck FUNCTION

}

void loop() {
  // put your main code here, to run repeatedly:


            digitalWrite(trig1Pin, LOW);
            delayMicroseconds(5);
            digitalWrite(trig1Pin, HIGH);
            delayMicroseconds(10);
            digitalWrite(trig1Pin, LOW);

            duration = pulseIn(echo1Pin, HIGH);


            radarValue = (duration/2) / 74;   // Divide by 74 or multiply by 0.0135

           
            waterheight = 94.5 - radarValue;

            digitalWrite(trig2Pin, LOW);
            delayMicroseconds(5);
            digitalWrite(trig2Pin, HIGH);
            delayMicroseconds(10);
            digitalWrite(trig2Pin, LOW);

            duration = pulseIn(echo1Pin, HIGH);


            radarValue2 = (duration/2) / 74;   // Divide by 74 or multiply by 0.0135

           
            fertilizerheight = 94.5 - radarValue;
  vTaskDelay(1000 / portTICK_PERIOD_MS);  
  
}

  
//####################################################################
//#                          UTIL FUNCTIONS                          #       
//####################################################################
void vButtonCheck( void * pvParameters )  {
    configASSERT( ( ( uint32_t ) pvParameters ) == 1 );     
      
    for( ;; ) {
        // Add code here to check if a button(S) is pressed
        // then execute appropriate function if a button is pressed  

     
        vTaskDelay(200 / portTICK_PERIOD_MS);  
        }
}

void vUpdate( void * pvParameters )  {
    configASSERT( ( ( uint32_t ) pvParameters ) == 1 );    
 
    for( ;; ) {

            

        soilMoistureValue = analogRead(analogPin);  //put Sensor insert into soil
        soilmoisturepercent = map(soilMoistureValue, AirValue, WaterValue, 0, 100);

        soilMoistureValue2 = analogRead(analogPin2);  //put Sensor insert into soil
        soilmoisturepercent2 = map(soilMoistureValue2, AirValue, WaterValue, 0, 100);

        // sensors_event_t temp_event, pressure_event;
        // bmp_pressure->getEvent(&pressure_event);

        h = dht.readHumidity();
        t = dht.readTemperature();
        hi = dht.computeHeatIndex(t, h);

        h2 = dht2.readHumidity();
        t2 = dht2.readTemperature();
        hi2 = dht2.computeHeatIndex(t2, h2);
        // pa = pressure_event.pressure;

        // Serial.print(F("Approx air pressure = "));
        // Serial.print(pa);
        // Serial.println(" hPa");

        // Serial.print(F("Approx altitude = "));
        // Serial.print(bmp.readAltitude(1014)); /* Adjusted to local forecast! */
        // Serial.println(" m");

        //   Serial.println(soilmoisturepercent);

        if(soilmoisturepercent >= 100)
        {
          soilmoisturepercent=100;
        }
        else if(soilmoisturepercent <=0)
        {
          soilmoisturepercent=0;
        }

        if(soilmoisturepercent2 >= 100)
        {
          soilmoisturepercent2=100;
        }
        else if(soilmoisturepercent2 <=0)
        {
          soilmoisturepercent2=0;
        }
        // Serial.print(F("Approx soil moisture = "));
        // Serial.print(soilmoisturepercent);
        // Serial.println("%");

        // Serial.print(F("Approx humidity = "));
        // Serial.print(h);
        // Serial.println("%");

        // Serial.print(F("Approx temperature = "));
        // Serial.print(t);
        // Serial.println(" C");

        // Serial.print(F("Approx heat index = "));
        // Serial.print(hi);
        // Serial.println("C");


        //----------------------------------------
      int xpos = 0, ypos = 5, gap = 4, radius = 52;
          // Draw a large meter
          xpos = 320/2 - 150, ypos = 15, gap = 100, radius = 50;
          
          ringMeter( t,0,90, 0,0,radius,"TEMPERATURE",4 ); // Draw analogue meter

          ringMeter( hi,0,90, 108,0,radius,"HEAT INDEX",4 ); // Draw analogue meter

          ringMeter(h,0,100, 215,0,radius,"HUMIDITY",4 ); // Draw analogue meter
          
          ringMeter(soilmoisturepercent,0,99, 0,120,radius,"SOIL MOISTURE",4 ); // Draw analogue meter
          
          ringMeter(waterheight ,0,99, 108,120,radius,"WATER LEVEL",4 ); // Draw analogue meter

          ringMeter(fertilizerheight ,0,99, 215,120,radius,"FERTILIZER",4 ); // Draw analogue meter

        

        tft.setCursor (247, 90); // Print the Humidity
        tft.setTextSize (1);
        tft.setTextColor (GREEN, RED);
        tft.print (h, 1);
        tft.setTextSize (1);
        tft.setTextColor (GREEN, RED);
        tft.print (" % ");
        tesmod = 1;

        tft.setCursor (138, 210); // Print the Humidity
        tft.setTextSize (1);
        tft.setTextColor (GREEN, RED);
        tft.print (waterheight, 1);
        tft.setTextSize (1);
        tft.setTextColor (GREEN, RED);
        tft.print (" % ");

        tft.setCursor (133, 90); // Print the Humidity
        tft.setTextSize (1);
        tft.setTextColor (GREEN, RED);
        tft.print ("( Feels Like )");
        tft.setTextSize (1);
        tft.setTextColor (GREEN, RED);
      
        tft.setCursor (33, 90); // Print the Humidity
        tft.setTextSize (1);
        tft.setTextColor (GREEN, RED);
        tft.print (t, 1);
        tft.setTextSize (1);
        tft.setTextColor (GREEN, RED);
        tft.print (" *C ");

        tft.setCursor (33, 210); // Print the Humidity
        tft.setTextSize (1);
        tft.setTextColor (GREEN, RED);
        tft.print (soilmoisturepercent, 1);
        tft.setTextSize (1);
        tft.setTextColor (GREEN, RED);
        tft.print (" %   ");

        tft.setCursor (247, 210); // Print the Humidity
        tft.setTextSize (1);
        tft.setTextColor (GREEN, RED);
        tft.print (fertilizerheight, 1);
        tft.setTextSize (1);
        tft.setTextColor (GREEN, RED);
        tft.print (" %  ");

   
      if(isNumber(t)){
              

              // 1. Create JSon object
              StaticJsonDocument<1500> doc;
              
              // 2. Create message buffer/array to store serialized JSON object
              char message[1600]={0};
              
              // 3. Add key:value pairs to JSon object based on above schema
              doc["timestamp"] = getTimeStamp();
              doc["temperature"] =  round( average(t, t2) * 100) / 100.0;
              doc["humidity"] =  round( average(h, h2) * 100) / 100.0;
              doc["heatindex"] =  round( average(hi, hi2) * 100) / 100.0;
              doc["water"] = percentage(waterheight);
              doc["ferterlizer"] = percentage(waterheight);
              doc["soilmoisture"] = round(((soilmoisturepercent + soilmoisturepercent2)/2) * 100) / 100.0;
             
    


              // 4. Seralize / Covert JSon object to JSon string and store in message array

              serializeJson(doc,message);
              Serial.println(message);
               
              // 5. Publish message to a topic sobscribed to by both backend and frontend
              if(mqtt.connected()){
                publish(pubtopic,message);
              }               

          }

        vTaskDelay(1000 / portTICK_PERIOD_MS);  
    }
}

unsigned long getTimeStamp(void) {
          // RETURNS 10 DIGIT TIMESTAMP REPRESENTING CURRENT TIME
          time_t now;         
          time(&now); // Retrieve time[Timestamp] from system and save to &now variable
          return now;
}

void callback(char* topic, byte* payload, unsigned int length) {
 // ############## MQTT CALLBACK  ######################################
  // RUNS WHENEVER A MESSAGE IS RECEIVED ON A TOPIC SUBSCRIBED TO

  Serial.printf("\nMessage received : ( topic: %s ) \n", topic);
  char* received = new char[length + 1]{ 0 };

  for (int i = 0; i < length; i++) {
    received[i] = (char)payload[i];
  }

  // PRINT RECEIVED MESSAGE
  Serial.printf("Payload : %s \n", received);


  // CONVERT MESSAGE TO JSON
  StaticJsonDocument<1000> doc;
  DeserializationError error = deserializeJson(doc, received);

  if (error) {
    Serial.print("deserializeJson() failed: ");
    Serial.println(error.c_str());
    return;
  }


  // PROCESS MESSAGE
  const char* type = doc["type"];

  if (strcmp(type, "controls") == 0) {
    // 1. EXTRACT ALL PARAMETERS: NODES, RED,GREEN, BLUE, AND BRIGHTNESS FROM JSON OBJECT
    int nodes = doc["leds"];
    int brightness = doc["brightness"];
    int red = doc["color"]["r"];
    int green = doc["color"]["g"];
    int blue = doc["color"]["b"];


    // 2. ITERATIVELY, TURN ON LED(s) BASED ON THE VALUE OF NODES. Ex IF NODES = 2, TURN ON 2 LED(s)

    for (unsigned char i = 0; i < nodes; i++) {
      leds[i] = CRGB(red, green, blue);
      FastLED.setBrightness(brightness);
      FastLED.show();
      delay(50);
    }

    // 3. ITERATIVELY, TURN OFF ALL REMAINING LED(s).

    for (unsigned char x = nodes; x < NUM_LEDS; x++) {
      leds[x] = CRGB::Black;
      FastLED.setBrightness(brightness);
      FastLED.show();
      delay(50);
    }
  }
}

bool publish(const char *topic, const char *payload){   
     bool res = false;
     try{
        res = mqtt.publish(topic,payload);
        // Serial.printf("\nres : %d\n",res);
        if(!res){
          res = false;
          throw false;
        }
     }
     catch(...){
      Serial.printf("\nError (%d) >> Unable to publish message\n", res);
     }
  return res;
}

//========================================================================

//========================================================================

void ringMeter(int value, int vmin, int vmax, int x, int y, int r, char *units, byte scheme)
{
  // Minimum value of r is about 52 before value text intrudes on ring
  // drawing the text first is an option
  
  x += r; y += r;   // Calculate coords of centre of ring
  int w = r / 3;    // Width of outer ring is 1/4 of radius 
  int angle = 150;  // Half the sweep angle of meter (300 degrees)
  int v = map(value, vmin, vmax, -angle, angle); // Map the value to an angle v
  byte seg = 3; // Segments are 3 degrees wide = 100 segments for 300 degrees
  byte inc = 6; // Draw segments every 3 degrees, increase to 6 for segmented ring
  // Variable to save "value" text colour from scheme and set default
  int colour = GREEN;
 
  // Draw colour blocks every inc degrees
  for (int i = -angle+inc/2; i < angle-inc/2; i += inc) {
    // Calculate pair of coordinates for segment start
    float sx = cos((i - 90) * 0.0174532925);
    float sy = sin((i - 90) * 0.0174532925);
    uint16_t x0 = sx * (r - w) + x;
    uint16_t y0 = sy * (r - w) + y;
    uint16_t x1 = sx * r + x;
    uint16_t y1 = sy * r + y;

    // Calculate pair of coordinates for segment end
    float sx2 = cos((i + seg - 90) * 0.0174532925);
    float sy2 = sin((i + seg - 90) * 0.0174532925);
    int x2 = sx2 * (r - w) + x;
    int y2 = sy2 * (r - w) + y;
    int x3 = sx2 * r + x;
    int y3 = sy2 * r + y;

    if (i < v) { // Fill in coloured segments with 2 triangles
      switch (scheme) {
        case 0: colour = GREEN; break; // Fixed colour
        case 1: colour = RED; break; // Fixed colour
        case 2: colour = BLUE; break; // Fixed colour
        case 3: colour = rainbow(map(i, -angle, angle, 0, 127)); break; // Full spectrum blue to red
        case 4: colour = rainbow(map(i, -angle, angle, 70, 127)); break; // Green to red (high temperature etc)
        case 5: colour = rainbow(map(i, -angle, angle, 127, 63)); break; // Red to green (low battery etc)
        default: colour = GREEN; break; // Fixed colour
      }
      tft.fillTriangle(x0, y0, x1, y1, x2, y2, colour);
      tft.fillTriangle(x1, y1, x2, y2, x3, y3, colour);
      //text_colour = colour; // Save the last colour drawn
    }
    else // Fill in blank segments
    {
      tft.fillTriangle(x0, y0, x1, y1, x2, y2, RED);
      tft.fillTriangle(x1, y1, x2, y2, x3, y3, RED);
    }
  }
  // Convert value to a string
  char buf[10];
  byte len = 2; if (value > 99) len = 3;if (value > 999) len = 4;
  dtostrf(value, len, 0, buf);
  buf[len] = ' '; buf[len] = 0; // Add blanking space and terminator, helps to centre text too!
  // Set the text colour to default
  tft.setTextSize(1);

  if(value>9){
  tft.setTextColor(CYAN,RED);
  tft.setCursor(x-25,y-10);tft.setTextSize(3);
  tft.print(buf);}
  if(value==100){
  dtostrf(value, 3, 0, buf);
  buf[3] = ' '; buf[3] = 0; // Add blanking space and terminator, helps to centre text too!
  // Set the text colour to default
  tft.setTextColor(ORANGE,RED);
  tft.setCursor(x-25,y-10);tft.setTextSize(3);
  tft.print(buf);
  delay(1000);
  tft.setTextColor(RED,RED);
  tft.setCursor(x-25,y-10);tft.setTextSize(3);
  tft.print(buf);
  }
  else if(value<10){
  tft.setTextColor(colour,RED);
  tft.setCursor(x-25,y-10);tft.setTextSize(3);
  tft.print(buf);}

  
  tft.setTextColor(CYAN,RED);
  
  tft.setCursor(x-20,y+55);tft.setTextSize(1);
  tft.print(units); // Units display
  
  // Calculate and return right hand side x coordinate
  // return x + r;
}
//========================================================================

bool isNumber(double number){       
        char item[20];
        snprintf(item, sizeof(item), "%f\n", number);
        if( isdigit(item[0]) )
          return true;
        return false; 
} 



unsigned int rainbow(byte value)
{
  // Value is expected to be in range 0-127
  // The value is converted to a spectrum colour from 0 = blue through to 127 = red

  byte red = 0; // Red is the top 5 bits of a 16 bit colour value
  byte green = 0;// Green is the middle 6 bits
  byte blue = 0; // Blue is the bottom 5 bits
  byte quadrant = value / 32;

  if (quadrant == 0) {
    blue = 31;
    green = 2 * (value % 32);
    red = 0;
  }
  if (quadrant == 1) {
    blue = 31 - (value % 32);
    green = 63;
    red = 0;
  }
  if (quadrant == 2) {
    blue = 0;
    green = 63;
    red = value % 32;
  }
  if (quadrant == 3) {
    blue = 0;
    green = 63 - 2 * (value % 32);
    red = 31;
  }
  return (red << 11) + (green << 5) + blue;
}

double reserve(int height){
  const double tankDiameter = 61.5; // Diameter of the tank in inches
  const double gallonsAt100Percent = 1000.0; // Volume of water at 100% capacity in gallons

  // Calculate the radius from the diameter
  const double tankRadius = tankDiameter / 2.0;

  // Convert height to gallons using the volume formula for a cylinder
  double volume = 3.14159265359 * tankRadius * tankRadius * height / 231.0; // 231 cubic inches in a gallon

  return volume;

}

int percentage(int radarValue){

    return (radarValue / 77.763) * 100;
  }


int average(double a, double b){
  return (a + b) / 2;
}