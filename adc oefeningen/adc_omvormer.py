# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT
from gpiozero import PWMLED
import board
import busio
import digitalio
import time
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn

# create the spi bus
spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)

# create the cs (chip select)
cs = digitalio.DigitalInOut(board.D5)

# create the mcp object
mcp = MCP.MCP3008(spi, cs)

# create an analog input channel on pin 0
chan = AnalogIn(mcp, MCP.P0)
red = PWMLED(17)

while True:

    print("Raw ADC Value: ", chan.value)
    print("ADC Voltage: " + str(chan.voltage) + "V")
    #lees de potentiometerwaarden uit 
    raw_value = chan.value
    voltage = chan.voltage 
    #zet de ruwe ADC waarde om naar een genoralizeerde waarden tussen 0.0 en 1.0
    brightness = raw_value / 65535
    #stel de helderheid in 
    red.value = brightness

   

    time.sleep(1.0)
    
