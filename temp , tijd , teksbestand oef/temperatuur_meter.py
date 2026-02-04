import RPi.GPIO as GPIO
from w1thermsensor import W1ThermSensor
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN,pull_up_down=GPIO.PUD_UP)
sensor = W1ThermSensor()
while True:
    temperatuur_in_celcius = sensor.get_temperature()
    print(temperatuur_in_celcius)
    sleep(1)

