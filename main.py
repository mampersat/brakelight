import machine
import math
import neopixel
import random
import utime

# Configuration
lights = 10
neopixel_pin = 28
brake_pin_gpio = 16
button_pin_gpio = 27

# Initialize the pin and NeoPixel
brake_pin = machine.Pin(brake_pin_gpio, machine.Pin.IN, machine.Pin.PULL_DOWN)
button_pin = machine.Pin(button_pin_gpio, machine.Pin.IN, machine.Pin.PULL_UP)
np = neopixel.NeoPixel(machine.Pin(neopixel_pin), lights)

def cruise():
    for i in range(lights):
        np[i] = (64, 64, 64)
    np.write()


def brake():
    for i in range(lights):
        np[i] = (255, 255, 255)
    np.write()


def off():
    for i in range(lights):
        np[i] = (0, 0, 0)
    np.write()


def brake_flash():
    blinks_per_second = 3
    blink_interval_ms = 1000 / blinks_per_second  # Calculate the interval in milliseconds
    time_mod = utime.ticks_ms() % blink_interval_ms
    # print(f"{utime.ticks_ms()} : {time_mod}")
    if time_mod < (blink_interval_ms / 2):
        brake()
    else:
        off()


def night_rider():
    cycle_speed_seconds = 1
    # between zero and 2*pi sin goes from 0 -> 1 -> 0 -> -1 -> 0
    # so divide a second (or less) into 4 parts
    
    # cycle from -1 to 1 over a second
    for i in range(lights):
        # looks kewl on 4 pixels... adjust for more
        # should alwyas have at least 1 pixel on, but probably about 1/3 of pixels on at any time, oh you thought you didn't need math in school?
        s = math.sin(utime.ticks_ms() / 1000 * 2 * math.pi + i) 
        np[i] = (int(s * 128) + 128, int(s * 128) + 128, int(s * 128) + 128)
    np.write()


def party():
    # same as night_rider but with randdom greens and blues
    # only change if time is a factor of the airsped of an unladen swallow
    
    # cycle from -1 to 1 over a second
    for i in range(lights):
        # looks kewl on 4 pixels... adjust for more
        # should alwyas have at least 1 pixel on: which this kinda solves using the G and B values
        s = math.sin(utime.ticks_ms() / 1000 * 2 * math.pi + i) 
        g = random.randint(0,10)
        b = random.randint(0,10)
        np[i] = (int(s * 128) + 128, g, b)
    np.write()


def night_rider():
    cycle_speed_seconds = 1
    # between zero and 2*pi sin goes from 0 -> 1 -> 0 -> -1 -> 0
    # so divide a second (or less) into 4 parts
    
    # cycle from -1 to 1 over a second
    for i in range(lights):
        # looks kewl on 4 pixels... adjust for more
        # should alwyas have at least 1 pixel on, but probably about 1/3 of pixels on at any time, oh you thought you didn't need math in school?
        s = math.sin(utime.ticks_ms() / 1000 * 2 * math.pi + i) 
        np[i] = (int(s * 128) + 128, int(s * 128) + 128, int(s * 128) + 128)
    np.write()


def smooth_transition():
    ## TODO: The saftey committee identified this idea as vile source of potential bugs and an awesome oppertunity to brake the system, whose whole puprose is to brake in the first place
    ## TODO: DO NOT IMPLEMENT
    ## TODO: good first commit
    todo = "DO NOT IMPLEMENT"


def ambient_mode():
    ## TODO: another stupid idea sure to be full of bugs, can we start with WIFI?
    ## TODO: DO NOT IMPLEMENT
    ## TODO: FUCK WIFI
    ## TODO: good first commit
    todo = "DO NOT IMPLEMENT"


def handle_brake_pin_change(pin):
    global mode
    print(f"pin changed to {pin.value()}")

    if pin.value() == 1:
        print("Brake pressed")
        mode = brake_flash
    else:
        print("Brake released")
        mode = night_rider

def handle_button_pin_change(pin):
    global mode
    print(f"pin changed to {pin.value()}")

    if pin.value() == 1:
        print("Button pressed")
        mode = brake_flash
    else:
        print("Button released")
        mode = night_rider


# Attach interrupts to the pins
brake_pin.irq(trigger=machine.Pin.IRQ_RISING | machine.Pin.IRQ_FALLING, handler=handle_brake_pin_change)
button_pin.irq(trigger=machine.Pin.IRQ_RISING | machine.Pin.IRQ_FALLING, handler=handle_button_pin_change)


# Main loop
mode = party # cruise
while True:
    # time.sleep(0.1)  # Sleep is for the weak
    mode()