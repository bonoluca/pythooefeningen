from gpiozero import Motor
from gpiozero import MCP3008
from time import sleep

pot = MCP3008(channel=0)
motor = Motor(forward=17, backward=14, pwm = True)

while True:
    motor.forward(pot.value)
    print(pot.value)
    sleep(0.1)
    motor.backward(pot.value)
    print(pot.value)
    sleep(0.1)



