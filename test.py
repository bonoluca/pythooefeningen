#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
from datetime import datetime
from gpiozero import MCP3008
import adafruit_dht
import board

# Config
CSV_BESTAND = "test_temp_log.csv"
VREF = 3.3
TMP36_CHANNEL = 0
dht = adafruit_dht.DHT11(board.D4)

# Init
adc = MCP3008(channel=TMP36_CHANNEL)

# Header (eenmalig)
with open(CSV_BESTAND, "w", encoding="utf-8") as f:
    f.write("datum;tijd;dht11(°C);TMP36(°C);verschilwaarde(°C)\n")

while True:
    now = datetime.now()
    datum = f"{now.day}/{now.month}/{now.year}"
    tijd = now.strftime("%H:%M:%S")

    # TMP36 uitlezen
    voltage = adc.value * VREF
    tmp36_c = (voltage - 0.500) * 100

    # DHT11 uitlezen
    try:
        dht_c = dht.temperature
        humidity = dht.humidity
    except RuntimeError:
        dht_c = None
        humidity = None

    verschil = tmp36_c - dht_c if dht_c is not None else None

    # Print exact wat in CSV komt
    if dht_c is not None:
        print(f"{datum};{tijd};{dht_c:.1f};{tmp36_c:.1f};{verschil:.1f}")
    else:
        print(f"{datum};{tijd};NA;{tmp36_c:.1f};NA")

    # Schrijf naar CSV
    with open(CSV_BESTAND, "a", encoding="utf-8") as f:
        f.write(f"{datum};{tijd};{dht_c if dht_c else 'NA'};{tmp36_c:.1f};{verschil if verschil else 'NA'}\n")

    time.sleep(2)
    #de code hier onder voorkomt gpio locks bij stoppen met ctrl + c 
    import atexit 
    atexit.register(lambda: dht.exit())