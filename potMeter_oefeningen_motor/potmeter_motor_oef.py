from gpiozero import Motor #importeer de gpiozero library
from gpiozero import MCP3008 #importeer de mcp3008 library
from time import sleep #importeer sleep

pot = MCP3008(channel=0) #de pot meter op channel 0 zetten
motor = Motor(forward=17, backward=14, pwm = True)  #zet de forward op pin 17 en backwards op 14 en zet de pwm op true
 
while True: #zolang true is blijf door gaan
    motor.forward(pot.value)  # laat de motor naar voor draaiden gelijk aan pot meter waarde
    print(pot.value)  #print de potentiometer value
    sleep(0.07)  #een sleep voor 0.1 sec
    motor.backward(pot.value)
    print(pot.value)  #print de potentiometer value
    sleep(0.07)  #een sleep voor 0.1 sec





