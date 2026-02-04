import RPi.GPIO as GPIO
from w1thermsensor import W1ThermSensor
import time
import board
import adafruit_dht
from gpiozero import LEDBoard
leds = LEDBoard(5,6,13,19,26,20,17,16)
dhtDevice = adafruit_dht.DHT11(board.D18)
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN,pull_up_down=GPIO.PUD_UP)
sensor = W1ThermSensor()
while True:
    try :
        temperature_c = dhtDevice.temperature
        humidity = dhtDevice.humidity
        temperatuur_in_celcius = sensor.get_temperature()
        temperatuur = temperatuur_in_celcius + temperature_c / 2
        print(temperature_c, humidity)
        print(temperatuur_in_celcius)
        if temperatuur >= 0:
            leds.value = (1, 0, 0, 0, 0, 0, 0, 0)
            print(temperature_c, humidity)
            print(temperatuur_in_celcius)
        elif temperatuur >= 10:
            leds.value = (1, 1, 1 ,0 , 0, 0, 0, 0)
            print(temperature_c, humidity)
            print(temperatuur_in_celcius)
        elif temperatuur >= 20:
            leds.value = (1, 1, 1 ,1 ,1 , 0, 0, 0)
            print(temperature_c, humidity)
            print(temperatuur_in_celcius)
        elif temperatuur >= 30:
            leds.value = (1, 1, 1 ,1 ,1 , 1 ,1 , 0)
            print(temperature_c, humidity)
            print(temperatuur_in_celcius)

        elif temperatuur >= 35:
            leds.value = (1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 )
            print(temperature_c, humidity)
            print(temperatuur_in_celcius)
    except RuntimeError as error:
        print(error.args[0])
    time.sleep(1.0)
            

