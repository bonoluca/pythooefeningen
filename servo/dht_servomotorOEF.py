from gpiozero import AngularServo
from time import sleep
import board
import adafruit_dht

servo = AngularServo(17, min_angle = -90, max_angle = 90)

dhtDevice = adafruit_dht.DHT11(board.D18)

while True:
    try:
        temperature_c = dhtDevice.temperature
        humidity = dhtDevice.humidity
        print(temperature_c, humidity)
        if temperature_c < 15:
            servo.angle = 0
            sleep(2)
        elif temperature_c >= 15:
            servo.angle = 45
            sleep(2)
        elif temperature_c >= 20:
            servo.angle = 90
            sleep(2)
    except RuntimeError as error:
        print(error.args[0])
        sleep(1.0)