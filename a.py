import requests
import time
import Adafruit_DHT
import serial
import time 
import string
import pynmea2  
import requests
sensor = Adafruit_DHT.DHT11
pin = 24
while True:
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

    url = "https://api885.herokuapp.com/"
    myobj = {
      "temp":int(temperature),
      "curr_time":str(time.time())
  
    }
    x = requests.post(url, json = myobj)
    print("succesfully data goes in database........")
    print("Temperature is---",temperature)