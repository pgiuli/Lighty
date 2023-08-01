#This file manages all requests sent to the API

import urequests

print('Loaded Request File!')

baseurl = 'http://10.1.1.47:8000/lighty-rgb/'

append = '?manual=true'

def get_color(manual=False):
    
    if manual:
        requesturl = baseurl + append   
        print('Sending request with hai!')
        print('Sending HTTP request to: {}'.format(requesturl))
    else:
        requesturl = baseurl
        print('Sending HTTP request to: {}'.format(requesturl))

    response = urequests.get(requesturl)
    data = response.json()

    response.close() #Garbage collection
    response = None #Garbage collection

    return (data['red'], data['green'], data['blue']), data['hai']



