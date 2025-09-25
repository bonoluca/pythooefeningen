from gpiozero import LEDBoard  #import ledboard
from time import sleep   #import sleep

delay = 1  #variabelen voor 1 is delay

leds = LEDBoard(5,6,13,19,26,20,17,16)  #zet alle pins in een voor er een colectie van te maken 


while True:    #zolang het true is zal die doorgaan
    for led in leds:  #voor led in leds die zet de 1e waarde van leds in led 
        led.on()  #die zet die waarde aan
        sleep(delay)  #een delay 
        led.off()  # die zet die waarden uit
    for led in leds[::-1]:  #doet hetzelfde lijk regel 10 maar dan van achter naar voor
        led.on() #die zet die waarde aan
        sleep(delay) #een delay 
        led.off()  # die zet die waarden uit
    





