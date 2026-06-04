import time
import serial


if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    ser.reset_input_buffer()
    while True:
        temp =40
        hum = 0
        ventilator = 0
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').rstrip()
            print(line)
        else:
            ser.write(b"Hello from Raspberry Pi!\n")
            line = ser.readline().decode('utf-8').rstrip()
            print(line)
            time.sleep(1)
       
        if temp <= 30:
            ventilator = 0
        

        elif temp <= 30 and hum < 70 or temp <= 27 and hum >= 70:
            ventilator = 100
        
        elif temp <= 35 and hum < 60 or temp <= 30 and hum >= 60:
            ventilator = 100
        
        elif temp > 35 or hum > 80:
            ventilator = 100
        
        print(ventilator)



