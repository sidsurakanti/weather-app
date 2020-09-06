import weather as ws

city = input("City: ")

temperature, humidity = ws.get(city)
print(f"\nWeather in {city.title()}:")
print(f"Temperature: {temperature}")
print(f"Humidity: {humidity}")


