This is my first foray into using the Github DCVS for my project storage. I am an EE by trade, and as
a hobbyist on the side I toy with network control of sensors and motor control. The work I do is mainly
with the Sparkfun ESP8266 wifi shield, using the Arduino Uno or Mega.

This project is a simple one, just testing the latency of a socket connection from a client connecting
to a wifi server set up on the Arduino Uno, using the Sparkfun ESP8266 wifi shield.

There are two files contained in the project. The only difference is that one uses PyQt4, and the other PyQt5.

I have run both of these files successfully on;

Python 2.7
Python 3.5

and on;

Debian Buster
RPi

I have tried to run these on the latest Ubuntu, 20.10, and have been successful running wifi_latency_pyqt5.py
with Python 3. However, Ubuntu does not seem to support PyQt4 any longer, or support PyQt5 in Python 2.7. No big
deal, it was just an experiment on my part to see how backwards compatible I could make this code.

Running this code, I have found a mean latency of about 1.2 seconds, looks like maybe a one sigma distribution
of about 1.15 to 1.25s. This is OK for temp sensors and such, but not for motor control. I have other experiments
in mind using direct radio control for motors. I will post other projects if I am successful.

Note that I use the LiquidCrystal Arduino library, as I have an HD44780 16x2 LCD display mounted on an Arduino
prototyping board. There are potential conficts between the electrical connections need for the wifi shield and 
for the LCD display. This is reflected in the arguments that I have used in the;

LiquidCrystal lcd()

function in this code. You will need to wired your board to reflect this function call, or change the function 
call and your wiring per your own needs.

Although it's not noted in these files, I have set the ESP8266 wifi shield to software control and I am using 
pin 8 (tx) and pin 9 (rx) for the Software Serial control. You will need to edit your Software Serial library to
reflect this.

For my own security reason, I left the following arguments in the .ino code empty. You will need to add your own.

const char mySSID[] = "";
const char myPSK[] = "";

There is a lot of the ESP8266 example code left in the Arduino code. My apologies that I have not cleaned this up.

I'm happy to help, please contact me if you have interest in this, or run into issues making it run.

Steve

s.reine@comcast.net         
