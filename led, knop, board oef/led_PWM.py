#importeer alles 
import time
import board
import adafruit_dht
from gpiozero import RGBLED
#dht een pin geven 
dhtDevice = adafruit_dht.DHT11(board.D18)
led = RGBLED(red=9, green=10, blue=11)  # voorbeeld: RGBLED(9, 10, 11, active_high=False)
helderheid = 1.0 #variabelen voor helderheid 

colors = [
    [255, 0, 0],     # index = 0  -> 40°C
    [205, 38, 38],   # index = 1
    [205, 55, 0],    # index = 2
    [250, 128, 114], # index = 3
    [238, 149, 114], # index = 4
    [255, 127, 0],   # index = 5
    [205, 133, 0],   # index = 6
    [238, 173, 14],  # index = 7
    [238, 221, 130], # index = 8
    [205, 205, 0],   # index = 9
    [255, 246, 143], # index = 10 -> ~20°C
    [124, 252, 0],   # index = 11
    [0, 255, 0],     # index = 12
    [78, 238, 148],  # index = 13
    [0, 245, 255],   # index = 14
    [151, 255, 255], # index = 15
    [0, 255, 255],   # index = 16
    [135, 206, 250], # index = 17
    [0, 191, 255],   # index = 18
    [30, 144, 255],  # index = 19
    [0, 0, 255]      # index = 20 -> 0°C
]

def clamp_temp(temperatuur_in_celsius):
    """Hou temperatuur binnen 0..40°C; None blijft None."""
    if temperatuur_in_celsius is None:
        return None
    try:
        return max(0.0, min(40.0, float(temperatuur_in_celsius)))
    except (TypeError, ValueError):
        return None

def temp_to_index_method_A(temperatuur_in_celsius):
    """
    Methode A: lineaire mapping 0..40°C -> index 20..0
    40°C -> 0 (rood), 0°C -> 20 (blauw)
    Discrete keuze met round naar dichtstbijzijnde kleur.
    """
    normaale_temp = clamp_temp(temperatuur_in_celsius)
    if normaale_temp is None:
        return None
    index = round((40.0 - normaale_temp) * 20.0 / 40.0)  # 0..20
    # extra veiligheid:
    if index < 0: index = 0
    if index > 20: index = 20
    return index

def set_led_rgb255(rgb_list):
    """
    Zet [R,G,B] (0..255) om naar PWM floats (0..1) en stuur de LED.
    Houdt rekening met helderheid factor.
    """
    if rgb_list is None:
        return
    try:
        r, g, b = rgb_list
        led.color = (
            (r / 255.0) * helderheid,
            (g / 255.0) * helderheid,
            (b / 255.0) * helderheid
        )
    except Exception as error:
        print("LED set error:", error)

try:
    while True:
        try:
            # DHT uitlezen 
            temperature_c = dhtDevice.temperature  
            print(f"Temperatuur: {temperature_c} °C")

            # Index berekenen 
            index = temp_to_index_method_A(temperature_c)
            if index is None:
                print("Geen geldige temperatuurmeting; kleur blijft ongewijzigd.")
            else:
                # een try voor de Veiligheid voor index en kleurenlijst
                try:
                    rgb = colors[index]
                except IndexError:
                    print(f"Index buiten bereik ({index}); fallback naar blauw.")
                    rgb = colors[-1]

                # ik stuur de LED via PWM
                set_led_rgb255(rgb)
        except RuntimeError as error:
        
            print("DHT error:", error)

        except Exception as error:
            # Algemene fallback 
            print("Onverwachte fout in de lus:", error)

        # DHT11 niet te snel lezen; ~1–2s is prima
        time.sleep(2.0)
except KeyboardInterrupt:
    print("Gestopt door gebruiker (Ctrl+C).")
finally:
    try:
        led.off()
    except Exception:
        pass