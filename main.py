import machine
import neopixel
import time

# It's useful to test a longer strip periodically, so just init to 100
# lights = max(airport_pixel.values()) +1
lights = 10

neopixel_pin = 28
np = neopixel.NeoPixel(machine.Pin(neopixel_pin), lights)

def brake():
    # write to all pixels at once
    for i in range(0, lights):
        np[i] = (255,0,0)
    np.write()

def cruise():
    for i in range(0, lights):
        np[i] = (64,0,0)
    np.write()

while True:
    brake()
    time.sleep(1)
    cruise()
    time.sleep(1)