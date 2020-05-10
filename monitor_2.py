#!/usr/bin/python3

# monitor.py - For Terrarium Controllers using Adafruit
# DHT sensors, Energenie Pimote sockets, and ThingSpeak.
# MIT license.
# https://www.carnivorousplants.co.uk/resources/raspberry-pi-terrarium-controller/

# Imports
from gpiozero import Energenie
import Adafruit_DHT
import requests

# Attempt to get a sensor reading. The read_retry method will
# retry up to 15 times, waiting 2 seconds between attempts
# active pins are 4 and 5
sensormodel = Adafruit_DHT.AM2302
sensorpin = 4
humidity, temperature = Adafruit_DHT.read_retry(sensormodel, sensorpin)

# If either reading has failed after repeated retries,
# abort and log message to ThingSpeak
thingspeak_key = 'your key here'
if humidity is None or temperature is None:
	f = requests.post('https://api.thingspeak.com/update.json', data = {'api_key':thingspeak_key, 'status':'failed to get reading'})

# Otherwise, check if temperature is above threshold,
# and if so, activate Energenie socket for cooling fan
else:
	fansocket = 1
	tempthreshold = 30

	if temperature > tempthreshold:
		# Activate cooling fans
		f = Energenie(fansocket, initial_value=True)

	else:
		# Deactivate cooling fans
		f = Energenie(fansocket, initial_value=False)

	# Send the data to Thingspeak
	r = requests.post('https://api.thingspeak.com/update.json', data = {'api_key':thingspeak_key, 'field1':temperature, 'field2':humidity})
	
if humidity is not None and temperature is not None:
    print('Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, humidity))
else:
    print('Failed to get reading. Try again!')
    sys.exit(1)
