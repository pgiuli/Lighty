#This file manages all requests sent to the API
import urequests

print('Loaded Request File!')


apiurl = ""

append = "hai=true"

def get_color(hai=False):
    
    if hai:
        requesturl = apiurl + append   
        print('Sending request with hai!')
        #print('Sending HTTP request to: {}'.format(requesturl))
    else:
        requesturl = apiurl
        #print('Sending HTTP request to: {}'.format(requesturl))

    response = urequests.get(requesturl)
    data = response.json()

    response.close() #Garbage collection
    response = None #Garbage collection
    #print(data)
    return (data['red'], data['green'], data['blue']), data['hai']



