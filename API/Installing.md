# How to install and run the Lighty API

## This API installation guide is not final and will get modified. 

This API will allow a Lighty device to request RGB values on demand to be set on the device's LEDs.

## Install the Python requirements

`$ pip install -r requirements.txt`

## Configure API

Set your default custom color and initial preset on the api.py file.
Feel free to add more color presets on colors.py (Pull requests are welcome!)

Create a .env file in the API folder following the skeleton provided

## Running the services 

`$ python3 main.py` (On the API Folder)
