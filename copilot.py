
import time
import board
import adafruit_dht
from gpiozero import RGBLED

# -------------------------------
# Hardware-configuratie
# -------------------------------

# DHT11 op BCM pin 4 (fysieke pin 7) via Blinka
# (Aanrader i.p.v. GPIO18 om conflicten te vermijden)
dht = adafruit_dht.DHT11(board.D4)

# RGB LED (pas pinnen aan naar jouw bekabeling)
# Zet active_high=False als je een common anode RGB LED gebruikt.
led = RGBLED(red=9, green=10, blue=11)  # bv.: RGBLED(9, 10, 11, active_high=False)

# Algemene helderheid (0..1). Zet lager als je LED te fel is.
BRIGHTNESS = 1.0

# -------------------------------
# Kleurenlijst: 0 = rood (40°C) ... 20 = blauw (0°C)
# -------------------------------
colors = [
    [255, 0, 0],     # 0  -> 40°C
    [205, 38, 38],   # 1
    [205, 55, 0],    # 2
    [250, 128, 114], # 3
    [238, 149, 114], # 4
    [255, 127, 0],   # 5
    [205, 133, 0],   # 6
    [238, 173, 14],  # 7
    [238, 221, 130], # 8
    [205, 205, 0],   # 9
    [255, 246, 143], # 10 -> ~20°C
    [124, 252, 0],   # 11
    [0, 255, 0],     # 12
    [78, 238, 148],  # 13
    [0, 245, 255],   # 14
    [151, 255, 255], # 15
    [0, 255, 255],   # 16
    [135, 206, 250], # 17
    [0, 191, 255],   # 18
    [30, 144, 255],  # 19
    [0, 0, 255]      # 20 -> 0°C
]

# -------------------------------
# Hulpfuncties
# -------------------------------

def pick_color_by_temp_if(temp_c):
    """
    Kies een kleur uit de lijst op basis van temperatuur,
    zonder berekeningen: enkel if-else met vaste zones.
    40°C en hoger => colors[0] (rood)
    0°C en lager  => colors[20] (blauw)
    Daartussen stappen van 2°C per kleur.
    """
    if temp_c is None:
        return None

    # Zones van 2°C, van hoog naar laag
    if temp_c >= 40:
        return colors[0]
    elif temp_c >= 38:
        return colors[1]
    elif temp_c >= 36:
        return colors[2]
    elif temp_c >= 34:
        return colors[3]
    elif temp_c >= 32:
        return colors[4]
    elif temp_c >= 30:
        return colors[5]
    elif temp_c >= 28:
        return colors[6]
    elif temp_c >= 26:
        return colors[7]
    elif temp_c >= 24:
        return colors[8]
    elif temp_c >= 22:
        return colors[9]
    elif temp_c >= 20:
        return colors[10]
    elif temp_c >= 18:
        return colors[11]
    elif temp_c >= 16:
        return colors[12]
    elif temp_c >= 14:
        return colors[13]
    elif temp_c >= 12:
        return colors[14]
    elif temp_c >= 10:
        return colors[15]
    elif temp_c >= 8:
        return colors[16]
    elif temp_c >= 6:
        return colors[17]
    elif temp_c >= 4:
        return colors[18]
    elif temp_c >= 2:
        return colors[19]
    else:  # temp_c < 2 (incl. <= 0)
        return colors[20]

def set_led_rgb255(rgb):
    """
    Zet een (R,G,B) in 0..255 om naar PWM 0..1 en stuur de LED.
    Houdt rekening met BRIGHTNESS factor.
    """
    if rgb is None:
        return
    r, g, b = rgb
    led.color = (
        (r / 255.0) * BRIGHTNESS,
        (g / 255.0) * BRIGHTNESS,
        (b / 255.0) * BRIGHTNESS
    )

# -------------------------------
# Hoofdlus
# -------------------------------

try:
    while True:
        try:
            T = dht.temperature  # °C
            print(f"Temperatuur: {T} °C")

            kleur = pick_color_by_temp_if(T)
            if kleur is not None:
                set_led_rgb255(kleur)
            # Bij None laten we de vorige kleur staan

        except RuntimeError as e:
            # DHT11 geeft soms RuntimeErrors; rustig opnieuw proberen
            print("DHT error:", e)

        # DHT11 niet te snel lezen; ~1–2s is prima
        time.sleep(2.0)

except KeyboardInterrupt:
    pass
finally:
    led.off()
