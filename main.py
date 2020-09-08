import weather as ws
import sys

city = input("City: ")
try:
    key = sys.argv[1]
except IndexError:
    key = input("enter your API key: ")

temperature, temperature_celcius, humidity = ws.get(city, key)
print(f"\nWeather in {city.title()}:")
print(f"Temperature (in farenheight): {temperature}")
print(f"Temperature (in celcius): {temperature_celcius}")
print(f"Humidity: {humidity}")


