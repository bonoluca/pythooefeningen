import time
import board
import adafruit_dht
from gpiozero import RGBLED

# =========================
# Hardware-configuratie
# =========================

# DHT11:
# Aanrader: gebruik board.D4 (BCM pin 4) en zet 1-Wire uit als die actief is.
# Als je per se op D18 wilt blijven: laat board.D18 staan en check conflicts.
DHT_PIN = board.D4  # wijzig naar board.D18 als je op GPIO18 zit
dhtDevice = adafruit_dht.DHT11(DHT_PIN)

# RGB LED (pas aan naar jouw bekabeling)
# Let op: active_high=False gebruiken als je common anode RGB LED hebt.
led = RGBLED(red=9, green=10, blue=11)  # voorbeeld: RGBLED(9, 10, 11, active_high=False)

# Algemene helderheid (0..1). Zet lager als de LED te fel is.
BRIGHTNESS = 1.0

# =========================
# Kleurenlijst (0 = rood bij 40°C, 20 = blauw bij 0°C)
# =========================
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

# =========================
# Hulpfuncties
# =========================

def clamp_temp(T):
    """Hou temperatuur binnen 0..40°C; None blijft None."""
    if T is None:
        return None
    try:
        return max(0.0, min(40.0, float(T)))
    except (TypeError, ValueError):
        return None

def temp_to_index_method_A(T):
    """
    Methode A: lineaire mapping 0..40°C -> index 20..0
    40°C -> 0 (rood), 0°C -> 20 (blauw)
    Discrete keuze met round naar dichtstbijzijnde kleur.
    """
    Tc = clamp_temp(T)
    if Tc is None:
        return None
    idx = round((40.0 - Tc) * 20.0 / 40.0)  # 0..20
    # extra veiligheid:
    if idx < 0: idx = 0
    if idx > 20: idx = 20
    return idx

def set_led_rgb255(rgb_list):
    """
    Zet [R,G,B] (0..255) om naar PWM floats (0..1) en stuur de LED.
    Houdt rekening met BRIGHTNESS factor.
    """
    if rgb_list is None:
        return
    try:
        r, g, b = rgb_list
        led.color = (
            (r / 255.0) * BRIGHTNESS,
            (g / 255.0) * BRIGHTNESS,
            (b / 255.0) * BRIGHTNESS
        )
    except Exception as e:
        print("LED set error:", e)

# =========================
# Hoofdlus
# =========================

try:
    while True:
        try:
            # 1) DHT uitlezen (kan RuntimeError geven)
            temperature_c = dhtDevice.temperature  # °C
            print(f"Temperatuur: {temperature_c} °C")

            # 2) Index berekenen (Methode A)
            idx = temp_to_index_method_A(temperature_c)
            if idx is None:
                print("Geen geldige temperatuurmeting; kleur blijft ongewijzigd.")
            else:
                # Veiligheid voor index en kleurenlijst
                try:
                    rgb = colors[idx]
                except IndexError:
                    print(f"Index buiten bereik ({idx}); fallback naar blauw.")
                    rgb = colors[-1]

                # 3) LED aansturen via PWM
                set_led_rgb255(rgb)

        except RuntimeError as e:
            # DHT11 geeft soms runtime errors; rustig opnieuw proberen
            print("DHT error:", e)

        except Exception as e:
            # Algemene fallback (GPIO/permissies/convert-errors)
            print("Onverwachte fout in de lus:", e)

        # DHT11 niet te snel lezen; ~1–2s is prima
        time.sleep(2.0)

except KeyboardInterrupt:
    print("Gestopt door gebruiker (Ctrl+C).")

finally:
    # Netjes afsluiten
    try:
        led.off()
    except Exception:
        pass
