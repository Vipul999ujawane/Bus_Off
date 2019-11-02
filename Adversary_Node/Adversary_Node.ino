
#include <Canbus.h>
#include <defaults.h>
#include <global.h>
#include <mcp2515.h>
#include <mcp2515_defs.h>

//********************************Setup Loop*********************************//

void setup() {
  Serial.begin(9600);
  Serial.println("CAN Write - Testing transmission of CAN Bus messages");
  delay(1000);
  
  if(Canbus.init(CANSPEED_500))  //Initialise MCP2515 CAN controller at the specified speed
    Serial.println("CAN Init ok");
  else
    Serial.println("Can't init CAN");
    
  delay(1000);
}
  int targetPeriod;
  unsigned int count=0;
  unsigned long start, targetID= 0x631, maxJitter = 35; // jitter in microseconds
  unsigned long sum=0, attackId=1;
  unsigned char attackMsg[8] = {7, 193, 240 , 124, 7, 7, 7, 7};// avoiding bit stuff error  
  

void loop() {
  tCAN message;

  auto error_tec = mcp2515_read_register(TEC);
  Serial.print("TEC Count : ");
  Serial.println(error_tec);
  if(!mcp2515_check_message()){
    if(mcp2515_get_message(&message)){
      if(message.id == 0x631){
        Serial.print("ID: ");
        Serial.print(message.id,HEX);
        Serial.print(", ");
        Serial.print("Data: ");
        Serial.print(message.header.length,DEC);
        for(int i=0;i<message.header.length;i++) 
         {  
           Serial.print(message.data[i],HEX);
           Serial.print(" ");
         }
        Serial.println("");
      }
    }
  }
}
