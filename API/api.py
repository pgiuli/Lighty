from fastapi import FastAPI
import colors

app = FastAPI()

custom_color = 100, 100, 100

current_preset = 'happy'

force_update = True

def get_color(preset=None):
    #If the key in current_present does not have a value in colors.py the API defaults to the current custom color
    if preset != None and colors.emotions.get(preset) is not None:
        return colors.emotions.get(preset)
    else:
        return custom_color

@app.get("/lighty-rgb/")

async def get_rgb_values():
    
    red, green, blue = get_color(current_preset)
    response = {
        "red": red,
        "green": green,
        "blue": blue,
        "force_update" : force_update
    }
    return response