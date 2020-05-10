#!/usr/bin/python3

# monitor.py - For Terrarium Controllers using Adafruit
# DHT sensors, Energenie Pimote sockets, and ThingSpeak.
# MIT license.
# https://www.carnivorousplants.co.uk/resources/raspberry-pi-terrarium-controller/

# Imports
from gpiozero import Energenie
import Adafruit_DHT
import requests

#Energenie extension socket numbers
fang_light= 2
toothless_light= 3
syl_light= 4
fansocket= 1

##first vivarium temperature reading- gpio pin 5

# Attempt to get a sensor reading. The read_retry method will
# retry up to 15 times, waiting 2 seconds between attempts
#Sensorpin 5 is Fang
sensormodel = Adafruit_DHT.AM2302
sensorpin = 5
humidity, temperature = Adafruit_DHT.read_retry(sensormodel, sensorpin)

# If either reading has failed after repeated retries,
# abort and log message to ThingSpeak
thingspeak_key = 'your key here'
if humidity is None or temperature is None:
	f = requests.post('https://api.thingspeak.com/update.json', data = {'api_key':thingspeak_key, 'status':'failed to get reading'})

# Otherwise, check if temperature is above threshold,
# and if so, activate Energenie socket for cooling fan
else:
	
	tempthreshold = 30

	if temperature > tempthreshold:
		# Activate cooling fans
		f = Energenie(fansocket, initial_value=True)
		f = Energenie(fang_light, initial_value=False)

	else:
		# Deactivate cooling fans
		f = Energenie(fansocket, initial_value=False)

	# Send the data to Thingspeak
##	r = requests.post('https://api.thingspeak.com/update.json', data = {'api_key':thingspeak_key, 'field1':temperature, 'field2':humidity})
	
if humidity is not None and temperature is not None:
    print('Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, humidity))
else:
    print('Failed to get reading. Try again!')
    sys.exit(1)

## Second vivairum reading and publish to Thingspeak
	
# Attempt to get a sensor reading. The read_retry method will
# retry up to 15 times, waiting 2 seconds between attempts
#Sensorpin 6 is Toothless
sensormodel = Adafruit_DHT.AM2302
sensorpin = 6
humidity1, temperature1 = Adafruit_DHT.read_retry(sensormodel, sensorpin)

# If either reading has failed after repeated retries,
# abort and log message to ThingSpeak
thingspeak_key = 'TFNNRVXKARXUD9QV'
if humidity1 is None or temperature1 is None:
	f = requests.post('https://api.thingspeak.com/update.json', data = {'api_key':thingspeak_key, 'status':'failed to get reading'})

# Otherwise, check if temperature is above threshold,
# and if so, activate Energenie socket for cooling fan
else:
	
	tempthreshold1 = 35

	if temperature1 > tempthreshold1:
		# Activate cooling fans
		f = Energenie(fansocket, initial_value=True)
		f = Energenie(toothless_light, initial_value=False)

	else:
		# Deactivate cooling fans
		f = Energenie(fansocket, initial_value=False)

	# Send the data to Thingspeak
	r = requests.post('https://api.thingspeak.com/update.json', data = {'api_key':thingspeak_key, 'field3':temperature, 'field4':humidity, 'field5':temperature1, 'field6':humidity1})
	
if humidity is not None and temperature is not None:
    print('Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature1, humidity1))
else:
    print('Failed to get reading. Try again!')
    sys.exit(1)