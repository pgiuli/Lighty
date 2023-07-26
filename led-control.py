#The only purpose of this file is to recieve RGB values to be set on the LEDs

import machine

print('Loaded LED File!')


R_PIN = 3
G_PIN = 4
B_PIN = 5

def set(red, green, blue):
    
    return