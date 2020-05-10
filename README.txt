Smart_viv README

This code is designed to be used with a wifi enabled Rasberry pi,
AM2302 temperaturesensor(s) and Energenie pi-Mote remote control 
extension lead.

These files have been written using code and guide produced by Tom's 
Carnivores: 
https://www.carnivorousplants.co.uk/resources/raspberry-pi-terrarium-controller/

I have modified some of the code to allow for multiple probes to be 
monitored at once, and have multiple energinie sockets to be controlled.

Monitor_2.py is designed to send data from one sensor pin to Thingspeak, and display the temperature and humidity in the terminal.
This is for checking your probes are connected properly.

Monitor.py is for sending data from two or more sensors to thingspeak, and is to be used after you know that your probes are working,
and placed in an 'Auto files' folder for running via crontab. You will also need a copy of the AdafruitDHT.py in any folders you are running 
either of these scripts as this contains the instructions/ drivers for using the sensors.
