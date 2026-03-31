import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(4, GPIO.IN, GPIO.PUD_UP)

GPIO.wait_for_edge(4, GPIO.FALLING):
print("button was pressed")

from gpiozero import Button

btn = Button(4)

btn.wait_for_press()
print("button was pressed")