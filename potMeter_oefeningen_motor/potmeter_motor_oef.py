from gpiozero import Motor
from gpiozero import MCP3008
from time import sleep

pot = MCP3008(channel=0)
motor = Motor(forward=4, backward=14)

while True:
    motor.forward()
    sleep(5)
    motor.backward()
    sleep(5)
    print(pot.value)



rpi@raspberrypi:~/Documenten/pythooefeningen $ /bin/python /home/rpi/Documenten/pythooefeningen/potMeter_oefeningen_motor/potmeter_motor_oef.py
Traceback (most recent call last):
  File "/usr/lib/python3/dist-packages/gpiozero/pins/pi.py", line 411, in pin
    pin = self.pins[info]
          ~~~~~~~~~^^^^^^
KeyError: PinInfo(number=7, name='GPIO4', names=frozenset({'J8:7', 'BOARD7', 'WPI7', 4, 'BCM4', 'GPIO4', '4'}), pull='', row=4, col=1, interfaces=frozenset({'', 'dpi', 'gpio', 'uart', 'i2c', 'spi'}))

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/rpi/Documenten/pythooefeningen/potMeter_oefeningen_motor/potmeter_motor_oef.py", line 6, in <module>
    motor = Motor(forward=4, backward=14)
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3/dist-packages/gpiozero/devices.py", line 108, in __call__
    self = super().__call__(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3/dist-packages/gpiozero/output_devices.py", line 1197, in __init__
    ('forward_device', PinClass(forward, pin_factory=pin_factory)),
                       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3/dist-packages/gpiozero/devices.py", line 108, in __call__
    self = super().__call__(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3/dist-packages/gpiozero/output_devices.py", line 392, in __init__
    super().__init__(pin, active_high=active_high, initial_value=None,
  File "/usr/lib/python3/dist-packages/gpiozero/output_devices.py", line 74, in __init__
    super().__init__(pin, pin_factory=pin_factory)
  File "/usr/lib/python3/dist-packages/gpiozero/mixins.py", line 75, in __init__
    super().__init__(*args, **kwargs)
  File "/usr/lib/python3/dist-packages/gpiozero/devices.py", line 553, in __init__
    pin = self.pin_factory.pin(pin)
          ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3/dist-packages/gpiozero/pins/pi.py", line 413, in pin
    pin = self.pin_class(self, info)
          ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3/dist-packages/gpiozero/pins/lgpio.py", line 126, in __init__
    lgpio.gpio_claim_input(
  File "/usr/lib/python3/dist-packages/lgpio.py", line 755, in gpio_claim_input
    return _u2i(_lgpio._gpio_claim_input(handle&0xffff, lFlags, gpio))
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3/dist-packages/lgpio.py", line 458, in _u2i
    raise error(error_text(v))
lgpio.error: 'GPIO busy'