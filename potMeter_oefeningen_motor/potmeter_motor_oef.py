from gpiozero import Motor
from gpiozero import MCP3008
from time import sleep

pot = MCP3008(channel=0)
motor = Motor(forward=4, backward=14)

while True:
    motor.forward()
    sleep(5)
    motor.backward()
    sleep(5)
    print(pot.value)


