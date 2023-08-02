from fastapi import FastAPI, Query
import colors

import random

app = FastAPI()

custom_color = 100, 100, 100

current_preset = 'anticipating'

hai = False

def get_color(preset=None):
    #If the key in current_present does not have a value in colors.py the API defaults to the current custom color
    if preset != None and colors.emotions.get(preset) is not None:
        return colors.emotions.get(preset)
    else:
        return custom_color

def haiback():
    print('The button was pressed!')

@app.get("/lighty-rgb/")

async def get_rgb_values(manual: bool = Query(False)):
    global hai

    print('Sent values!')
    red, green, blue = random.randint(1, 255), random.randint(1, 255), random.randint(1, 255)
    red, green, blue = get_color(current_preset)
    response = {
        "red": red,
        "green": green,
        "blue": blue,
        "hai" : hai
    }
    if hai:
        hai = False
        print('Sent hai! Hai is now off.')
    
    if manual:
        haiback()

    return response
