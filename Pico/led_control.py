#This file takes care of everything involving the RGB NeoPixel Ring. 

import machine
from neopixel import NeoPixel
from time import sleep
from random import randint
from colors import colors
from colors import gradient

import gc

gc.enable()

print('Loaded LED File!')


pin_number = 4
led_count = 16

ring_pin = machine.Pin(pin_number, machine.Pin.OUT)

ring = NeoPixel(ring_pin, led_count)

def startup_anim():
    print('Displaying startup animation!')
    for i in range(led_count):
        ring[i] = (randint(1,255), randint(1,255), randint(1,255))
        ring.write()
        sleep(.1)

    sleep(.35)

    for i in range(led_count):

        ring[i] = (0, 0, 0)
        ring.write()
        sleep(.05)


def display_battery(percentage):
    print('Displaying battery: {}%!'.format(percentage))

    try:
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
            clear(smooth=True, reverse=True)
        else:
            raise RuntimeError('Percentage is out of bounds!')
    except:
        print('Failed to display battery percentage!')
        alert('error')
    
def clear(smooth = False, reverse = False):
    print('Clearing LEDs!')
    if smooth:
        leds = list(range(led_count))
        if reverse:
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

def loading(color=None, repeat=1):
    print('Displaying loading animation!')
    #Spins x times a color
    for i in range(repeat):
        if color != None and colors.get(color) != None:
            ledcolor = colors.get(color)
        else:
            ledcolor = (255, 255, 255)

        for i in range(led_count):
            ring[i] = ledcolor
            ring.write()
            sleep((1/led_count)*2)
            ring[i] = (0, 0, 0)
            ring.write()

        ring.write()

def alert(color=None):
    print('Displaying alert!')
    #Flashes 3 times
    for i in range(3):
        if color != None:
            ledcolor = colors.get(color)
        else:
            ledcolor = (255, 255, 255)

        for i in range(led_count):
            ring[i] = ledcolor

        ring.write()
        sleep(0.15)
        clear()
        sleep(0.15)

def display(rgb):

    print('Displaying RGB color: {}'.format(rgb))

    for i in range(21):
        updated_color = tuple(round(value * (i / 20)) for value in rgb)
        ring.fill(updated_color)
        ring.write()
        sleep(0.05)
    
    sleep(5)

    steps = list(range(0, 21))
    steps.reverse()
    for i in steps:
        updated_color = tuple(round(value * (i / 20)) for value in rgb)
        ring.fill(updated_color)
        ring.write()
        sleep(0.05)
    
    clear()


def rainbow():
    print('Displaying rainbow!')
    for i in range(led_count):
        ring[i] = gradient[i]
        ring.write()
        sleep(0.05)
    
    sleep(1)

    clear(smooth=True, reverse=True)

    return