#include "application.h"
#include "HttpClient.h"
#include "TM1637.h"

/**
* Declaring the variables.
*/
unsigned int nextTime = 0;    // Next time to contact the server
#define CLK D2//pins definitions for TM1637 and can be changed to other ports
#define DIO D3
TM1637 tm1637(CLK,DIO);
HttpClient http;

// Headers currently need to be set at init, useful for API keys etc.
http_header_t headers[] = {
    //  { "Content-Type", "application/json" },
    //  { "Accept" , "application/json" },
    { "Accept" , "*/*"},
    { NULL, NULL } // NOTE: Always terminate headers will NULL
};

http_request_t request;
http_response_t response;
int tracker;

void setup() {
    Serial.begin(9600);
    tracker = 13;

    tm1637.init();
    tm1637.set(BRIGHT_TYPICAL);//BRIGHT_TYPICAL = 2,BRIGHT_DARKEST = 0,BRIGHTEST = 7;
}

void loop() {
  int8_t NumTab[] = {0,1,2,3,4,5,6,7,8,9};
  int8_t ListDisp[4];
    if (nextTime > millis()) {
        return;
    }

    Serial.println();
    Serial.println("Application>\tStart of Loop.");
    // Request path and body can be set at runtime or at setup.
    request.hostname = "secret-fjord-5332.herokuapp.com";
    request.port = 80;
    request.path = "/2011/ACRDBT.json";

    // The library also supports sending a body with your request:
    //request.body = "{\"key\":\"value\"}";

    // Get request
    http.get(request, response, headers);
    char buff[5];
    memcpy(buff, &response.body[tracker], 4);
    Serial.println(buff);

    tm1637.display(0,buff[0] - '0');
    tm1637.display(1,buff[1] - '0');
    tm1637.display(2,buff[2] - '0');
    tm1637.display(3,buff[3] - '0');

    nextTime = millis() + 5000;
    tracker += 66;
    if(tracker >= 400)
      tracker = 13;
}
