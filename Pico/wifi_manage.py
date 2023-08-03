#This file manages the wifi connection and its corresponding routines

from time import sleep
import network

import gc

gc.enable()

import led_control

print('Loaded WiFi File!')


#Change the country value to your country's code to prevent any errors when connect. ISO 3166-1 Alpha-2
import rp2
rp2.country('ES')
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.config(pm = 0xa11140)

#Prints an overview of the WiFi connection status (IP, DNS, SSID, RSSI...)
def get_status():
    status = wlan.ifconfig()
    print("IP Address: {}\nGateway: {}\nDNS: {}".format(status[0],status[2],status[3]))


#Get credentials from file (just so that the password is not stored in the .py file because github :'D)
def get_credentials():
    credentials_file = open('secrets.txt', 'r')
    lines = credentials_file.readlines()
    #[:-1] Removes the breakline expression. (\n)
    ssid = lines[0][:-1]
    password = lines[1][:-1]
    credentials_file.close()
    return ssid, password


#Im sorry for this
def disconnect():
    if wlan.status() < 1:
        print('Board already disconnected')
    else:
        wlan.disconnect()
        sleep(1)
        if wlan.status() == 0:
            print('Disconnected from network!')
            led_control.alert('white')
        else:
            print('wtf how did it mess up disconnecting')


#Main Connection Rutine
def connect():
    
    ssid, password = get_credentials()
    wlan.connect(ssid, password)
    print('Attempting to connect, please wait.')

    max_wait = 30
    while max_wait > 0:
        #Lower than 0 means an error. 3 is connection with IP.  More on: https://datasheets.raspberrypi.com/picow/connecting-to-the-internet-with-pico-w.pdf
        if wlan.status() < 0 or wlan.status() == 3:
            break
        print('sending load wifi')
        led_control.loading('wifi')

        max_wait -= 1
        
        

    #Throw error if connction is not successful after the specified time.
    if wlan.status() != 3:
        led_control.alert('red')
        raise RuntimeError('Connection Failed! Error: {}'.format(wlan.status()))
    else:
        print('Connected!')
        led_control.alert('success')

        get_status()
        

#connect(get_credentials()) doesn't work for some reason i'm to lazy to figure out QwQ

