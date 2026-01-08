import time
import board
import adafruit_dht
from gpiozero import LED , Button 
from signal import pause 

dhtDevice = adafruit_dht.DHT11(board.D18)
led = LED(17)
button = Button(2)





while True:
    try:
        temperature_c = dhtDevice.temperature
        humidity = dhtDevice.humidity
        print(temperature_c, humidity)
        if temperature_c >= 40:
            button.when_pressed = led.on 
            button.when_released = led.off
            pause()
    except RuntimeError as error:
        print(error.args[0])
    time.sleep(1.0)

