from gpiozero import MCP3008
from gpiozero import Motor
from time import sleep

pot = MCP3008(channel=0)

motor = Motor(forward=4, backward=14)

while True:
    print(pot.value)
    sleep(2)


while True:
    motor.forward()
    sleep(5)
    motor.backward()
    sleep(5)