#This file will return the RGB values sent by the API

import urequests

print('Loaded Request File!')

url = 'http://10.1.1.47:8000/lighty-rgb/'

def get_color():

    print('Sending HTTP request to: {}'.format(url))
    response = urequests.get(url)
    data = response.json()
    response.close() #Garbage collection
    response = None #Garbage collection
    return data['red'], data['green'], data['blue'], #data['force_update']



