# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT
from gpiozero import LED
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
red = LED(17)
go = True
teller = 0
while go:

    print("Raw ADC Value: ", chan.value)
    print("ADC Voltage: " + str(chan.voltage) + "V")
    #lees de potentiometerwaarden uit 
    raw_value = chan.value
    voltage = chan.voltage 
    #zet de ruwe ADC waarde om naar een genoralizeerde waarden tussen 0.0 en 1.0
    brightness = raw_value / 65535
    #stel de helderheid in 
    LED.value = brightness

    red.on()
    teller = teller +1
    if teller == 20:
        go = False
    time.sleep(1.0)
    
