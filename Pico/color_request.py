#This file manages all requests sent to the API
import urequests

print('Loaded Request File!')

def get_credentials():
    credentials_file = open('secrets.txt', 'r')
    lines = credentials_file.readlines()
    #[:-1] Removes the breakline expression. (\n)
    api = lines[2][:-1]
    token = lines[3]
    credentials_file.close()
    return api, token


api, token = get_credentials()

url = "{}?token={}".format(api, token)
hai_append = "&hai=true"


def get_color(hai=False):
    
    if hai:
        requesturl = url + hai_append  
        print('Sending request with hai!')
        print('Sending HTTP request to: {}'.format(requesturl))
    else:
        requesturl = url
        print('Sending HTTP request to: {}'.format(requesturl))

    response = urequests.get(requesturl)
    data = response.json()

    response.close() #Garbage collection
    response = None #Garbage collection
    #print(data)
    return (data['red'], data['green'], data['blue']), data['hai']



