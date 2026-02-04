# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT
from gpiozero import PWMLED #importeer pwmled van gpiozere
import board #imopteer board
import busio #importeer busio
import digitalio #imoprteer digitalio
import time #imopteer time 
import adafruit_mcp3xxx.mcp3008 as MCP #importeer de library adafruit_mcp3xxx.mcp3008
from adafruit_mcp3xxx.analog_in import AnalogIn #importeer de library  adafruit_mcp3xxx.analog_in

# create the spi bus
spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)

# create the cs (chip select)
cs = digitalio.DigitalInOut(board.D5)

# create the mcp object
mcp = MCP.MCP3008(spi, cs)

# create an analog input channel on pin p0 pin p1 en p2
pot_rood = AnalogIn(mcp, MCP.P0)
pot_groen = AnalogIn(mcp, MCP.P1)
pot_blauw = AnalogIn(mcp, MCP.P2)

rood = PWMLED(17) #geef red variabelen 17 pin numer
groen = PWMLED(27) #geef groen variabelen 27 pin numer
blauw = PWMLED(22) #geef blauw variabelen 22 pin numer

while True: # zolang het true is gaat het door 

    print("Raw ADC Value: ", pot_rood.value)  #print Raw ADC Value: ", pot_rood.value
    print("ADC Voltage: " + str(pot_rood.voltage) + "V") #print  "ADC Voltage: " + str(pot_rood.voltage) + "V

    # deel de waarde van pot rood en groen en blauw door 65535 en zet die waardes in de variabelen val r , val g , val b

    val_r = pot_rood.value / 65535
    val_g = pot_groen.value / 65535
    val_b = pot_blauw.value / 65535
    
    rood.value = val_r #geef rood value de waarde van val r
    groen.value = val_g#geef groen value de waarde van val g
    blauw.value = val_b#geef blauw value de waarde van val b
   

    time.sleep(1.0) # wacht 1s voordat je opnieuw begint 
    
