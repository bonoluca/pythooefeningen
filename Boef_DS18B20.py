from w1thermsensor import W1ThermSensor, Sensor

sensor = W1ThermSensor(sensor_type=Sensor.DS18B20, sensor_id="00000588806a")
temperature_in_celsius = sensor.get_temperature()