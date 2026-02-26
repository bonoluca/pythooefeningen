from gpiozero import Servo
from time import sleep

Servo = Servo(17)

while True:
    Servo.min()
    sleep(2)
    Servo.mid()
    sleep(2)
    Servo.max()
    sleep(2)

