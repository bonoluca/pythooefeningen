import time as time 
import board
import adafruit_dht
from time import gmtime , strftime


dhtDevice = adafruit_dht.DHT11(board.D18)

huidig_tijd = strftime()

teller = 0 





while True:
    try:
        temperature_c = dhtDevice.temperature
        humidity = dhtDevice.humidity
        print(temperature_c, humidity)
        print("nr tijd  Temp(°C)  Vochtigheid(%)") 
        print(teller ,huidige_tijd)
        teller = teller + 1

      

      
    except RuntimeError as error:
        print(error.args[0])
    time.sleep(5)




   