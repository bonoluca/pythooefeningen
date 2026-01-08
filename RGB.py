from gpiozero import RGBLED
from time import sleep

led = RGBLED(red=9, green=10, blue=11)

led.red = 1  # full red
sleep(1)
led.red = 0.5  # half red
sleep(1)

led.color = (0, 1, 0)  # full green
sleep(1)
led.color = (1, 0, 1)  # magenta
sleep(1)
led.color = (1, 1, 0)  # yellow
sleep(1)
led.color = (0, 1, 1)  # cyan
sleep(1)
led.color = (1, 1, 1)  # white
sleep(1)

led.color = (0, 0, 0)  # off
sleep(1)

# slowly increase intensity of blue
for n in range(100):
    led.blue = n/100
    sleep(0.1)


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
