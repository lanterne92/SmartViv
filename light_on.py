##Turns on lights using crontab
# MIT license.
# https://www.carnivorousplants.co.uk/resources/raspberry-pi-terrarium-controller/

# Imports
from gpiozero import Energenie
import Adafruit_DHT
import requests


syl = 4
fang = 3
toothless = 2


f = Energenie(syl, initial_value=True)
f = Energenie(fang, initial_value=True)
f = Energenie(toothless, initial_value=True)

