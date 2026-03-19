
# import the library
import RPi.GPIO as GPIO
from RpiMotorLib import RpiMotorLib 

GpioPins = [18, 23, 24, 25]  # zet de a,b,c,d pin op 18, 23, 24, 25

# Declare an named instance of class pass a name and motor type
mymotortest = RpiMotorLib.BYJMotor("MyMotorOne", "28BYJ")

vraag_voor_hvl_mm = int(input("hvl mm wil je draaien :")) #vraag hvl mm ze willen en zet het als een int 

mm_per_rotatie_nr = 2 #maak variabelen voor 2 aan
stappen_per_rotatie = 512 #maak voor een rotatie stappen een variabelen aan


stappen = (vraag_voor_hvl_mm / mm_per_rotatie_nr)* stappen_per_rotatie
#maak variabelen voor formule en deel de vraag voor hvl mm dor mijn klasnr en dat maal 512

print(f'aantal stappen : {stappen}' )  #print hvl stappen er zijn 
# call the function , pass the parameters
mymotortest.motor_run(GpioPins , .01, stappen, False, False, "half", .05)
#zet hvl seconden de rasberry pi wacht tussen elke stap op 01 
#zet de stappen op hvl stappen er worden berekent
#zet tegen de klok draaien op false en zet info printen tijden het draaien ook op false
#en zet de steptype op half step
#laat de motor 05 sec wachten voor dat die beweegt 
