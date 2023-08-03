from fastapi import FastAPI, Query
import colors
import dotenv
import os
import requests

app = FastAPI()
dotenv.load_dotenv(dotenv.find_dotenv())

custom_color = 100, 100, 100
current_preset = 'happy'
send_hai = False

admin_token = os.getenv('API_TOKEN')
telegram_token = os.getenv('TELEGRAM_TOKEN')
admin_id = os.getenv('ADMIN_ID')

def get_color(preset=None):
    #If the key in current_present does not have a value in colors.py the API defaults to the current custom color
    if preset != None and colors.emotions.get(preset) is not None:
        return colors.emotions.get(preset)
    else:
        return custom_color

def recieved_hai():
    print('Recieved hai!')
    try:
        boturl= 'https://api.telegram.org/bot{}/sendMessage'.format(telegram_token)
        requests.post(boturl, json={'chat_id': admin_id, 'text': "Hai!!! Someone's thinking about you! <3"})
    
    except:
        print('An error occured sending hai to Telegram!')
    else:
        print('Successfully sent hai to Telegram!')

@app.get("/lighty/rgb-values")

async def get_rgb_values(hai: bool = Query(False)):
    global send_hai

    print('Sent values!')
    red, green, blue = get_color(current_preset)

    response = {
        "red": red,
        "green": green,
        "blue": blue,
        "hai" : send_hai
    }
    if send_hai:
        send_hai = False
        print('Sent hai! Hai is now off.')
    
    if hai:
        recieved_hai()

    return response

@app.get("/lighty/set-values/")
async def set_values(hai: bool = Query(None), preset: str = Query(None), token: str = Query(None)):
    global send_hai, current_preset

    if token == admin_token:

        if hai is not None:
            print('Set send_hai to {}'.format(hai))
            send_hai = hai

        if preset is not None and colors.emotions.get(preset) is not None:
            print('Set preset to {}'.format(preset))
            current_preset = preset

        return {"hai": send_hai, "preset": current_preset}

    else:
        return {'Invalid token!'}
    

def start_api():
    import uvicorn
    uvicorn.run("color_api:app", host="0.0.0.0", port=8000, reload=True)