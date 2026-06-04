import time
import serial


if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    ser.reset_input_buffer()
    while True:
        temp =40
        hum = 0
        ventialtor = 0
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').rstrip()
            print(line)
        else:
            ser.write(b"Hello from Raspberry Pi!\n")
            line = ser.readline().decode('utf-8').rstrip()
            print(line)
            time.sleep(1)
        if temp <= 30 and hum <= 100:
            ventialtor = 0
        elif temp <= 43 or temp >= 30 and hum  
            ventialtor = 33
        elif temp <= 51 and hum <= 80:
            ventialtor = 66
        elif temp <= 61 and hum >= 20 or hum <= 100:
            ventialtor = 100
        
        print(ventialtor)



