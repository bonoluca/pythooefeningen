import time
import serial

if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    time.sleep(2)

    while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').rstrip()
            print("Ontvangen:", line)

            try:
                temp, hum = map(int, line.split(","))
            except:
                continue

            # Logica
            if temp <= 25:
                ventilator = 0

            elif temp <= 35:
                ventilator = 33

            elif temp <= 45:
                ventilator = 66

            elif temp <= 55:
                # hier zit jouw probleemzone!
                if hum <= 40:
                    ventilator = 66   # oranje
                else:
                    ventilator = 100  # rood

            else:
                ventilator = 100

            print("Ventilator:", ventilator)

            # terugsturen naar Arduino
            ser.write(f"{ventilator}\n".encode())

        time.sleep(1)
