# How to install and run the Lighty API

## This API is extremely barebones and pretty user-unfriendly. 

This API will allow a Lighty device to request RGB values on demand to be set on the device's LEDs.

## Install the Python requirements

`$ pip install -r requirements.txt`

## Configure API

Set your default custom color and initial preset on the api.py file.
Feel free to add more color presets on colors.py (Pull requests are welcome!) 

## Running the API (Temporary)

`$ uvicorn api:app --reload`
