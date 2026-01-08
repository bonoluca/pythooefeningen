import time
import board
import adafruit_dht
from gpiozero import LED , Button 
from gpiozero import RGBLED
from signal import pause 

dhtDevice = adafruit_dht.DHT11(board.D18)

colors = [
    (255, 0, 0),
    (205, 38, 38),
    (205, 55, 0),
    (250, 128, 114),
    (238, 149, 114),
    (255, 127, 0),
    (205, 133, 0),
    (238, 173, 14),
    (238, 221, 130),
    (205, 205, 0),
    (255, 246, 143),
    (124, 252, 0),
    (0, 255, 0),
    (78, 238, 148),
    (0, 245, 255),
    (151, 255, 255),
    (0, 255, 255),
    (135, 206, 250),
    (0, 191, 255),
    (30, 144, 255),
    (0, 0, 255)
]

eerste_waarde = colors[0]
tweede_waarde = colors[1]
derde_waarde = colors[2]

while True:
    try:
        temperature_c = dhtDevice.temperature
        print(temperature_c)
    except RuntimeError as error:
        print(error.args[0])
    time.sleep(1.0)