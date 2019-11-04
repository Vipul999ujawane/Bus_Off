/****************************************************************************
CAN Read Demo for the SparkFun CAN Bus Shield. 

Written by Stephen McCoy. 
Original tutorial available here: http://www.instructables.com/id/CAN-Bus-Sniffing-and-Broadcasting-with-Arduino
Used with permission 2016. License CC By SA. 

Distributed as-is; no warranty is given.
*************************************************************************/

#include <Canbus.h>
#include <defaults.h>
#include <global.h>
#include <mcp2515.h>
#include <mcp2515_defs.h>

//********************************Setup Loop*********************************//

void setup() {
  Serial.begin(9600); // For debug use
  
  if(Canbus.init(CANSPEED_500))  //Initialise MCP2515 CAN controller at the specified speed
    Serial.println("<<START>>");
  else
    Serial.println("Can't init CAN");
    
  delay(1000);
}

//********************************Main Loop*********************************//

void loop(){
  tCAN message;
if (!mcp2515_check_message()) 
	{
    if (mcp2515_get_message(&message)) 
	{
        //if(message.id == 0x620 and message.data[2] == 0xFF)  //uncomment when you want to filter
             //{
               auto time = millis();
               Serial.print(message.id,HEX);
               Serial.print(", ");
               Serial.println(time);
             //}
           }}

}
