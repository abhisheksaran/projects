4. Code for servo motor-
//creating a wifi with ESP8266

ESP8266WebServer gayuserver;
Servo topServo;
Servo bottomServo;//oh BADLUCK!,2nd motor has gone mad!
const char username [] = "servo";
const char password [] = "subspace";
void setup()
{
Serial.begin(115200);
Serial.println("hey itz FIRST STEP ..GOING TO BEGIN THE WIFI!..SEE U
AT LATER STAGE!!");
WiFi.softAP(username, password);
IPAddress myip = WiFi.softAPIP();
gayuserver.begin();
gayuserver.on("/unlock", unlock);
Serial.print("AP IP Address: ");
Serial.println(myip);
topServo.attach(12);
//bottomServo.attach(14);//defining pin number to output
}
void loop()
{
gayuserver.handleClient();
Serial.println("hendling clients!!");
}
//server has started


//creating a webpage for controlling the door , LOCK and UNLOCK 

void unlock(){
//String myhtml = "<html><head><title> DOOR UNLOCK</title> <h1>
<center> KEY TO UNLOCK YOUR DOOR
</center></h1><form></form>><button type=\"submit\" name=\"key\"
value=\"0\" >openmydoor</button> </form> </head></html> ";
String myhtml = "<html><head><title>Door Lock-Unlock
System</title></head><body style=\"background-color:
red\"><h1><center><font size=\"108\">Key To
Room</font></center></h1><h1><center><font color=\"white\"
size=\"108\">\"Welcome\"</font></center></h1><h2><font color=\"white\"
size=\"96\"><marquee>\"IIT PKD Me Apka Swagat
Hai\"</marquee></h2></h2></font><form><br><center><button
type=\"submit\" name=\"state\" value=\"0\" style=\"font-size:35px\" color=
yellow> UNLOCK </button></center></form></body></html>";
gayuserver.send(200, "text/html", myhtml);

//our phone will connect to esp wifi using password which only known to room owner
//and then opening the webpage

if (gayuserver.arg("state") == "0")
{ Serial.print("starting motors...");
topServo.write(180);
// bottomServo.write(180);
delay(5000);
topServo.write(90);
//bottomServo.write(90);
delay(2000);
//topServo.write(180);
//delay(2000);
}
if(gayuserver.arg("state") == "1")
{Serial.println("warning :IF IT'S ALREADY LOCK,THEN U ARE GOING TO
UNLOCK");
topServo.write(0);
bottomServo.write(0);
delay(2000);
}
}

