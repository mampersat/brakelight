import machine
import neopixel
import time

# Configuration
lights = 10
neopixel_pin = 28
brake_pin = 27

# Initialize the pin and NeoPixel
pin = machine.Pin(brake_pin, machine.Pin.IN, machine.Pin.PULL_UP)
np = neopixel.NeoPixel(machine.Pin(neopixel_pin), lights)

def brake():
    for i in range(lights):
        np[i] = (255, 0, 0)
    np.write()

def cruise():
    for i in range(lights):
        np[i] = (64, 0, 0)
    np.write()

def handle_pin_change(pin):
    if pin.value() == 1:
        brake()
    else:
        cruise()

# Attach interrupt to the pin
pin.irq(trigger=machine.Pin.IRQ_RISING | machine.Pin.IRQ_FALLING, handler=handle_pin_change)

# Main loop
while True:
    handle_pin_change(pin)
    time.sleep(1)  # Sleep to reduce CPU usage