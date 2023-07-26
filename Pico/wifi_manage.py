#This file manages the wifi connection and its corresponding routines

import time
import network

print('Loaded WiFi File!')


#Change the country value to your country's code to prevent any errors when connect. ISO 3166-1 Alpha-2
import rp2
rp2.country('ES')
wlan = network.WLAN(network.STA_IF)
wlan.active(True)


#Get credentials from file (just so that the password is not stored in the .py file because github :'D)
def get_credentials():
    credentials_file = open('wifi.txt', 'r')
    lines = credentials_file.readlines()
    #[:-1] Removes the breakline expression. (\n)
    ssid = lines[0][:-1]
    password = lines[1]

    return ssid, password


#Im sorry for this
def disconnect():
    wlan.disconnect()
    if wlan.status() == 0:
        print('Disconnected from network!')
    else:
        raise RuntimeWarning('Something happened when disconnecting. WLAN status is: {}'.format(wlan.status))


#Main Connection Rutine
def connect():
    
    ssid, password = get_credentials()
    wlan.connect(ssid, password)
    print('Attempting to connect, please wait.')

    max_wait = 25
    while max_wait > 0:
        #Lower than 0 means an error. 3 is connection with IP.  More on: https://datasheets.raspberrypi.com/picow/connecting-to-the-internet-with-pico-w.pdf
        if wlan.status() < 0 or wlan.status() == 3:
            break
        max_wait -= 1
        
        time.sleep(1)

    #Throw error if connction is not successful after the specified time.
    if wlan.status() != 3:
        raise RuntimeError('Connection Failed! Error: {}'.format(wlan.status))
    else:
        print('Connected!')
        #print(wlan.ifconfig())
        ip = wlan.ifconfig()[0]
        print("Pi's IP is: {}".format(ip))
        

#connect(get_credentials()) doesn't work for some reason i'm to lazy to figure out QwQ



