print('Starting...')

import wifi_manage
import led_control
import color_request
import time
import uasyncio
import sensor_manage
import machine
import gc
from time import sleep

gc.enable()
print(gc.mem_free())

#Purposely run without threading to avoid two modules interacting with the LED ring
led_control.startup_anim()

sleep(2)

wifi_manage.disconnect()

sleep(2)

for i in range(5):
        try:
            wifi_manage.connect()
        except:
            print('Connection failed')
            sleep(2)
            wifi_manage.disconnect()
            for i in range(15):
                led_control.loading('white')
        else:
            break


time.sleep(2)


button_led = machine.Pin(14, machine.Pin.OUT)
button = machine.Pin(2, machine.Pin.IN, machine.Pin.PULL_UP)

switch = machine.Pin(16, machine.Pin.IN, machine.Pin.PULL_UP)



show_hai = False


try:
    current_rgb, _ = color_request.get_color()
except:
    current_rgb = (255, 0, 0)
    print('Failed initial request!')
    led_control.alert('error')
else:
    print('Current RGB is: {}'.format(current_rgb))
    #led_control.display(current_rgb)
   


def manual_run():
    global current_rgb
    global show_hai

    if show_hai:
        print('Hai dismissed') 
        button_led.low()
        show_hai = False

    led_control.loading('white')

    if button.value() == 0:
        print('Button was held!')
        led_control.rainbow()
        try:
            rgb, _ = color_request.get_color(hai=True)
        except:
            print('Error during request!')
            led_control.alert('error')
        else:
            current_rgb = rgb
            time.sleep(0.2)
            led_control.display(rgb)

    else:
        try:
            rgb, _ = color_request.get_color()
        except:
            print('Error during request!')
            led_control.alert('error')
        else:
            current_rgb = rgb

            time.sleep(0.2)
            led_control.display(rgb)



async def check_new(force=False):
    global current_rgb
    global show_hai

    while True:

        try:
            new_rgb, hai = color_request.get_color()
            print('Recieved RGB values: {}'.format(new_rgb))
        except:
             print('Error during request!')
             led_control.alert('error')
        else:
            if hai == True:
                show_hai = True
                button_led.high()
                print('Recieved hai!')
                led_control.rainbow()
                await uasyncio.sleep(.75)
            if new_rgb != current_rgb or force:
                    led_control.display(new_rgb)
                    current_rgb = new_rgb
            else:
                    print('No changes in RGB values')
        await uasyncio.sleep(30)


async def notify_hai():
    global show_hai
    while True:
        if show_hai:
            print('Showing rainbow (Notif not dissmised)')
            led_control.rainbow()
        await uasyncio.sleep(30)


async def check_button():
    prev = button.value()
    while(button.value() == 1) or (button.value() == prev):
        prev = button.value()
        await uasyncio.sleep(0.05)


async def main():

    uasyncio.create_task(check_new())
    uasyncio.create_task(notify_hai())

    while True:

        print('Idling...')
        await check_button()
        print('button pressed')
        if switch.value() == 0:
            manual_run()
        if switch.value() == 1:
            battery = sensor_manage.get_battery()
            led_control.display_battery(battery)
        

        #_thread.start_new_thread(manual_run, ())
        

while True:
    uasyncio.run(main())
