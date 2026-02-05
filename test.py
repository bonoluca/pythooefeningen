#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import time
from datetime import datetime

import adafruit_dht
import board

# ========================
# CONFIG
# ========================
CSV_BESTAND = "test_temp_log.csv"

# Kies je GPIO hier (LET OP: 'board' mapping, niet BCM integer):
#  - board.D18  => GPIO18 (fysieke pin 12)
#  - board.D4   => GPIO4  (fysieke pin 7)
DHT_PIN = board.D18  # <-- PAS AAN NAAR JOUW AANSLUITING

# Sensor type (laat op DHT11 tenzij je echt DHT22/AM2302 hebt)
SENSOR_CLS = adafruit_dht.DHT11

# DHT11 mag ongeveer 1x per seconde; we nemen marge
MEET_INTERVAL_SECONDEN = 2

# Aantal herhaalpogingen per meting (bijv. checksum/buffer errors)
MAX_RETRIES = 5
RETRY_WACHTTIJD = 0.8  # sec tussen retries

# Eventueel een korte "opwarm" fase (sommige sensoren geven de eerste 1-2 metingen fout)
OPWARM_SKIPS = 1  # aantal metingen overslaan in het begin (0 = uit)
# ========================


def zorg_voor_csv_header(pad: str) -> None:
    """Schrijf CSV-header als bestand nog niet bestaat."""
    if not os.path.exists(pad):
        with open(pad, "w", encoding="utf-8") as f:
            f.write("datum;tijd;dht11_temp(°C);dht11_rh(%)\n")


def lees_dht_met_retries(dht, max_retries: int = 5, retry_s: float = 0.8):
    """
    Lees temperatuur en luchtvochtigheid met retries.
    Retourneert tuple (temp_c, rh_pct) of (None, None) na uitputting retries.
    """
    poging = 0
    while poging < max_retries:
        try:
            # Adafruit DHT kan RuntimeError gooien bij checksum/buffer issues.
            temp_c = dht.temperature
            rh_pct = dht.humidity

            # Validatie: soms geeft hij None terug
            if temp_c is not None and rh_pct is not None:
                return temp_c, rh_pct

        except RuntimeError as e:
            # Veelvoorkomende, onschuldige errors: "A full buffer was not returned", "Checksum failure"
            print(f"[WAARSCHUWING] Leespoging {poging+1}/{max_retries} mislukte: {e}")

        except Exception as e:
            # Andere fouten (zeldzaam) — wel loggen
            print(f"[FOUT] Onverwachte fout bij DHT read: {e}")

        poging += 1
        time.sleep(retry_s)

    # Alles geprobeerd, geen geldige meting
    return None, None


def main():
    print("DHT11 logger starten…")
    print(f"CSV-bestand: {os.path.abspath(CSV_BESTAND)}")
    print(f"GPIO-pin: {DHT_PIN}\n")

    zorg_voor_csv_header(CSV_BESTAND)

    # Sensor initialiseren
    dht = SENSOR_CLS(DHT_PIN)

    # Optionele opwarmfase: eerste metingen overslaan
    skips = OPWARM_SKIPS
    if skips > 0:
        print(f"Opwarmfase: sla de eerste {skips} meting(en) over…")
        for i in range(skips):
            _ = lees_dht_met_retries(dht, MAX_RETRIES, RETRY_WACHTTIJD)
            time.sleep(MEET_INTERVAL_SECONDEN)

    print("Logger actief. Druk op Ctrl+C om te stoppen.\n")

    try:
        while True:
            now = datetime.now()
            datum = now.strftime("%d/%m/%Y")
            tijd = now.strftime("%H:%M:%S")

            temp_c, rh_pct = lees_dht_met_retries(dht, MAX_RETRIES, RETRY_WACHTTIJD)

            # Console output
            if temp_c is None or rh_pct is None:
                print(f"{datum};{tijd};NA;NA")
            else:
                print(f"{datum};{tijd};{temp_c:.1f};{rh_pct:.0f}")

            # CSV append
            with open(CSV_BESTAND, "a", encoding="utf-8") as f:
                f.write(
                    f"{datum};{tijd};"
                    f"{temp_c if temp_c is not None else 'NA'};"
                    f"{rh_pct if rh_pct is not None else 'NA'}\n"
                )
                f.flush()  # direct naar schijf (handig bij power-off)

            time.sleep(MEET_INTERVAL_SECONDEN)

    except KeyboardInterrupt:
        print("\nAfsluiten op verzoek…")

    finally:
        # Sommige versies van adafruit_dht ondersteunen deinit/exit; als aanwezig, gebruik het.
        try:
            if hasattr(dht, "deinit"):
                dht.deinit()
            elif hasattr(dht, "exit"):
                dht.exit()  # alias in sommige Blinka-versies
        except Exception:
            pass

        print("DHT11 logger gestopt.")


if __name__ == "__main__":
    main()