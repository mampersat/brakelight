import machine
import neopixel
import time
import utime

# Configuration
lights = 10
neopixel_pin = 28
brake_pin = 27

# Initialize the pin and NeoPixel
pin = machine.Pin(brake_pin, machine.Pin.IN, machine.Pin.PULL_UP)
np = neopixel.NeoPixel(machine.Pin(neopixel_pin), lights)

def cruise():
    for i in range(lights):
        np[i] = (64, 0, 0)
    np.write()

def brake():
    for i in range(lights):
        np[i] = (255, 0, 0)
    np.write()

def off():
    for i in range(lights):
        np[i] = (0, 0, 0)
    np.write()

def brake_flash():
    blinks_per_second = 3
    blink_interval_ms = 1000 / blinks_per_second  # Calculate the interval in milliseconds
    time_mod = utime.ticks_ms() % blink_interval_ms
    print(f"{utime.ticks_ms()} : {time_mod}")
    if time_mod < (blink_interval_ms / 2):
        brake()
    else:
        off()
    
def handle_pin_change(pin):
    global mode
    if pin.value() == 1:
        print("Brake pressed")
        mode = brake_flash
    else:
        print("Brake released")
        mode = cruise

# Attach interrupt to the pin
pin.irq(trigger=machine.Pin.IRQ_RISING | machine.Pin.IRQ_FALLING, handler=handle_pin_change)

# Main loop
mode = cruise
while True:

    # time.sleep(0.1)  # Sleep to reduce CPU usage
    mode()