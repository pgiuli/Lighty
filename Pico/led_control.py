#This file takes care of everything involving the RGB NeoPixel Ring. 

import machine
import neopixel
from time import sleep
from random import randint

print('Loaded LED File!')

np_pin = 4
led_count = 16

ring = neopixel.NeoPixel(machine.Pin(np_pin), led_count)

def startup_anim():
    for i in range(led_count):
        ring[i] = (randint(1,255), randint(1,255), randint(1,255))
        ring.write()
        sleep(.05)

    sleep(.35)

    for i in range(led_count):
        ring[i] = (0, 0, 0)
        ring.write()
        sleep(.05)


def display_battery(percentage):
    if percentage >= 0 or percentage <= 100:
        active_leds = round(led_count/100*percentage)
    
        for i in range(active_leds):
            if i < 4:
                ring[i] = (255, 0, 0)
            else:
                ring[i] = (0, 255, 0)
            ring.write()
            sleep(0.05)
        
        sleep(4)
        clear(True)

    else:
        raise RuntimeError('Percentage is out of bounds!')
    
def clear(smooth = False):
    
    if smooth:
        leds = list(range(led_count))
        leds.reverse()
        for i in leds:
            ring[i] = (0, 0, 0)
            ring.write()
            sleep(0.05)
    else:
        #ring.fill(0, 0, 0)
        for i in range(led_count):
            ring[i] = (0, 0, 0)
            ring.write()

    ring.write()

