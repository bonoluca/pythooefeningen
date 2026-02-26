from gpiozero import AngularServo #importeer gpiozero library
from time import sleep #importeer sleep
import board #importeer board
import adafruit_dht #importeer adafruit_dht
servo = AngularServo(17, min_angle = -90, max_angle = 90)  #zet de max en min anghle op 90 en -90 en de pin op 17
dhtDevice = adafruit_dht.DHT11(board.D18)  #maak een sensor object aaan die je kan gebruiken om de tem of humidety te meten 
servo_waarde = 0 #maak een teller voor servo waare gelijk aan null
rest_servowaarde = 0 #maak een teller voor de servo waarde te restten naar null
while True: # zolang het op true is zal het herhalen 
    try: #probeer
        temperature_c = dhtDevice.temperature #maak een variabelen temperatuur_c aan voor de temp  van dht 
        print(temperature_c, servo_waarde) # print de 2 waardes uit 
        if temperature_c < 15:  # als de temp kleiner is dan 15 maak servo waarde gelijk aan reset servowaarde om het dan terug op nul te zetten 
            servo_waarde = rest_servowaarde
            servo_waarde = servo_waarde + 0
            sleep(2) # wacht 2 sec
        if temperature_c > 15: # als temp boven 15 graden is dan maak servo waarde gelijk aan reset servowaarde om het dan op 45 te zetten
            servo_waarde = rest_servowaarde
            servo_waarde = servo_waarde + 45
            sleep(2) #wacht 2 sec
        if temperature_c >= 20:# als temp boven 20 graden is dan maak servo waarde gelijk aan reset servowaarde om het dan op 90 te zetten
            servo_waarde = rest_servowaarde
            servo_waarde = servo_waarde + 90
            sleep(2) # wacht 2 sec        
        servo.angle = servo_waarde #lees servo uit en zet die op de waarde waarop servowaarde staat
    except RuntimeError as error: #als try niet werkt gaat die over naar dit  en print die dat er een fout is 
        print(error.args[0])
        sleep(1.0)#wacht 2sec