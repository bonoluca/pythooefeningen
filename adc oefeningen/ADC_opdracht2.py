import time
from gpiozero import MCP3008, LED
import adafruit_dht
import board
from time import  strftime

f = open("tijdbestand.txt", "w")
f.write("datum     tijd    dht11(°C)  TMP36(°C)   verschillwaarden(°C)\n")
f.close()

# --- Config ---
TMP36_CHANNEL = 0           # TMP36 Vout op CH0 van MCP3008
DHT_PIN = board.D18         # DHT11 op GPIO18 (BCM)
INTERVAL_SEC = 2.0

# --- Init hardware ---
adc = MCP3008(channel=TMP36_CHANNEL)   # standaard SPI0 CE0
dht = adafruit_dht.DHT11(DHT_PIN)

# LEDs (voorbeeld)
rood = LED(5)
geel = LED(6)
groen = LED(13)


while True:
    # TMP36 uitlezen -> spanning -> °C
    voltage = adc.value * 3.3               # 0.0..1.0 * 3.3V
    tmp36_c = (voltage - 0.500) * 100.0     # TMP36 formule

    # DHT11 uitlezen (kan soms RuntimeError geven)
    try:
        huidige_tijd = strftime (" %H:%M:%S ")
        dht_c = dht.temperature
        humidity = dht.humidity  # beschikbaar indien je later wil gebruiken
    except RuntimeError:
        dht_c = None

    # Verschil berekenen als DHT succesvol was
    verschil = (tmp36_c - dht_c) if dht_c is not None else None

    # LEDs en print
    if dht_c is not None:
        # Metingen ok -> groen aan
        groen.on()
        rood.off()

        # Print exact de drie waarden
        print(f"DHT11: {dht_c:.1f} °C | TMP36: {tmp36_c:.1f} °C | Δ: {verschil:+.1f} °C")
        f= open("tijdbestand.txt", "a")
        f.write(f"{huidige_tijd}  {dht_c:.1f} {tmp36_c:.1f} {verschil:+.1f} ")
        f.close()
        # Geel aan als verschil groter dan 2°C
        if abs(verschil) > 2.0:
            geel.on()
        else:
            geel.off()
    else:
        # DHT mislukt -> rood aan, geel/groen uit
        rood.on() 
        geel.off()
        groen.off()
        print(f"DHT11: NA     | TMP36: {tmp36_c:.1f} °C | Δ: NA")
        f= open("tijdbestand.txt", "a")
        f.write(f"DHT11: NA     | TMP36: {tmp36_c:.1f} °C | Δ: NA\n")
        f.close()


    time.sleep(INTERVAL_SEC)
