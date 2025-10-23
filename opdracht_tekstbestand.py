import time as time 
import board
import adafruit_dht
from time import gmtime , strftime

f = open("tijdbestand.txt", "w")
f.write("nr    tijd    temp(°C)  vochtigheid(%)\n")
f.close()
dhtDevice = adafruit_dht.DHT11(board.D18)



teller = 0 



while True:
    try:
        huidige_tijd = strftime (" %H:%M:%S ")
        temperature_c = dhtDevice.temperature
        humidity = dhtDevice.humidity
        print(temperature_c, humidity)
        print(huidige_tijd)
        
        f= open("tijdbestand.txt", "a")
        f.write(f"{teller}")
        f.write(f"{huidige_tijd}  ")
        f.write(f"{temperature_c}          ")
        f.write(f"{humidity}\n")
        f.close()
        teller = teller +1


      

      
    except RuntimeError as error:
        print(error.args[0])
    time.sleep(5)




   