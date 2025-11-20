#alles importeren tot en met regel 6
import RPi.GPIO as GPIO
from w1thermsensor import W1ThermSensor
import time
import board
import adafruit_dht

dhtDevice = adafruit_dht.DHT11(board.D18) #maak dhtdevice gelijk aan adafruit .... /variabelen maken

GPIO.setmode(GPIO.BCM)  #zecht hoe ik de pinnen noem
GPIO.setup(4, GPIO.IN,pull_up_down=GPIO.PUD_UP) #ik zet pin 4 als input
  #sensor = W1ThermSensor()
    
f = open("info_dht11.txt","w")  #open info dht11 tekstbestand

while True:
    try :
        f = open("info_dht11.txt","a")  # ik open het en voeg toe 
        temperature_c = dhtDevice.temperature  #ik maak 2 variabelen aan elkaar gelijk
    
        temperatuur_in_celcius =20 #sensor.get_temperature()    #ik maak deze varuabelen gelijk aan 20
        temperatuur =25# (temperatuur_in_celcius + temperature_c) / 2    #ik maak deze varuabelen gelijk aan 25
        print(temperature_c)  # print temperatuur_c zijn waarde
        huidige_tijd = time.ctime()  #ik maak variabelen huidige tijd aan door time.ctime te gebruiken 
        f.write("datum      ")  #schrijf datum
        f.write("tijd            ") #schrijf tijd
        f.write("DHT11  ") #schrijf dht11
        f.write("DS18B20 ")# schrijf ds18B20
        f.write("gemiddelde temperatuur\n",) #schrijf gem temp en daarna nieuwe regel
        f.write(f"{huidige_tijd} , {temperature_c} ,  {temperatuur_in_celcius}  , {temperatuur}\n") #schrijf de waardes van deze variabelen 
        f.close()  #close de tekstbestand 
  

    except RuntimeError as error: #vervangt de error door te printen dht not found
        print(error.args[0])
    time.sleep(5.0)  #timer 5sec

    




  





            

