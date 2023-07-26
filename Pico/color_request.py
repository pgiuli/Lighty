#This file will return the RGB values sent by the API

import urequests

print('Loaded Request File!')

url = 'https://api.giuli.cat/lighty'

def get_color():

    response = urequests.get(url)
    data = response.json()
 
    return data['red'], data['green'], data['blue']