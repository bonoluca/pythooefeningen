from gpiozero import MCP3008
import board
import busio
import digitalio
import time
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn
from time import  strftime
import adafruit_dht
import board

dhtDevice = adafruit_dht.DHT11(board.D18)

while True:
    try:
        temperature_c = dhtDevice.temperature
        humidity = dhtDevice.humidity
        print(temperature_c, humidity)
    except RuntimeError as error:
        print(error.args[0])
    time.sleep(1.0)