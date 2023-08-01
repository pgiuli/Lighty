#This file will return the RGB values sent by the API

import urequests

print('Loaded Request File!')

baseurl = 'http://10.1.1.47:8000/lighty-rgb/'

append = '?hai=true'

def get_color(haiback=False):
    
    if haiback:
        requesturl = baseurl + append   
        print('Sending request with hai!')
    else:
        requesturl = baseurl
        print('Sending HTTP request to: {}'.format(requesturl))

    response = urequests.get(requesturl)
    data = response.json()

    response.close() #Garbage collection
    response = None #Garbage collection

    return (data['red'], data['green'], data['blue']), data['hai']



