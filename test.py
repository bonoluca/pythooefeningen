#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import os
import atexit
from datetime import datetime
from gpiozero import MCP3008
import adafruit_dht
import board

# Config
CSV_BESTAND = "test_temp_log.csv"
VREF = 3.3
TMP36_CHANNEL = 0

# Init
adc = MCP3008(channel=TMP36_CHANNEL)
dht = adafruit_dht.DHT11(board.D17)   # <-- ANDERE GPIO (belangrijk!)

# GPIO netjes vrijgeven bij stoppen
atexit.register(lambda: dht.exit())

# Header alleen schrijven als bestand nog niet bestaat
if not os.path.exists(CSV_BESTAND):
    with open(CSV_BESTAND, "w", encoding="utf-8") as f:
        f.write("datum;tijd;dht11(°C);TMP36(°C);verschilwaarde(°C)\n")

while True:
    now = datetime.now()
    datum = now.strftime("%d/%m/%Y")
    tijd = now.strftime("%H:%M:%S")

    # TMP36 uitlezen
    voltage = adc.value * VREF
    tmp36_c = (voltage - 0.500) * 100

    # DHT11 uitlezen
    try:
        dht_c = dht.temperature
    except RuntimeError:
        dht_c = None

    verschil = tmp36_c - dht_c if dht_c is not None else None

    # Print
    if dht_c is not None:
        print(f"{datum};{tijd};{dht_c:.1f};{tmp36_c:.1f};{verschil:.1f}")
    else:
        print(f"{datum};{tijd};NA;{tmp36_c:.1f};NA")

    # CSV schrijven
    with open(CSV_BESTAND, "a", encoding="utf-8") as f:
        f.write(
            f"{datum};{tijd};"
            f"{dht_c if dht_c is not None else 'NA'};"
            f"{tmp36_c:.1f};"
            f"{verschil if verschil is not None else 'NA'}\n"
        )

    time.sleep(2)
