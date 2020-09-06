from convert import converter as con
import requests

def get(city):
    city = city.title()
    key = "67f58722a81d7a2143da94ffe198c2d9"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}"
    response = requests.get(url) # gets data from openweather api

    try:
        # get the data from the response
        data = response.json()['main']

        temp = data['temp_max'] # gets temperature from data
        temp = con(temp) # convert temp from kelvin to fahrenheit
        humidity = data['humidity'] # gets humidity from data
        ret = (temp, humidity) # packs temp and humidity into a tuple
        
        return ret

    except Exception as exp:
        return exp