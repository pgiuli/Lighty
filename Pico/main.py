print('Starting...')

import wifi_manage
import led_control
import color_request
import time
import uasyncio
import _thread
import machine
import gc

gc.enable()
print(gc.mem_free())

#Purposely run without threading to avoid two modules interacting with the LED ring
led_control.startup_anim()
wifi_manage.connect()

time.sleep(2)


button = machine.Pin(15, machine.Pin.IN, machine.Pin.PULL_UP)
switch = machine.Pin(16, machine.Pin.IN, machine.Pin.PULL_UP)


#gc.collect()
#print(gc.mem_free())
current_rgb = color_request.get_color()
#gc.collect()
#print(gc.mem_free())
print('Current RGB is: {}'.format(current_rgb))
led_control.display(current_rgb)


def manual_run():
    global current_rgb
    #gc.collect()
    rgb = color_request.get_color()
    current_rgb = rgb
    led_control.display(rgb)
    #print(gc.mem_free())


async def check_new(force=False):
    global current_rgb

    while True:
        #gc.collect()
        new_rgb = color_request.get_color()
        #gc.collect()
        print('Recieved RGB values: {}'.format(new_rgb))

        if new_rgb != current_rgb or force:
            led_control.display(new_rgb)
            current_rgb = new_rgb
        else:
            print('No changes in RGB values')
        await uasyncio.sleep(300)


async def beep():
    while True:
        print('boop')
        await uasyncio.sleep(1)


async def check_button():
    prev = button.value()
    while(button.value() == 1) or (button.value() == prev):
        prev = button.value()
        await uasyncio.sleep(0.05)


async def main():

    uasyncio.create_task(check_new())

    #uasyncio.create_task(beep())

    while True:
        await check_button()
        print('button pressed')
        manual_run()

        #_thread.start_new_thread(manual_run, ())
        

while True:
    uasyncio.run(main())
        

