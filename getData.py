import requests, json

apikey = "7cb9becaea566cc27d69991c345fa129"
base = "http://api.openweathermap.org/data/2.5/weather?"
city = "Austin"
compbase = f"{base}appid={apikey}&q={city}"
resp = requests.get(compbase)
x = resp.json()
clear()
if x["cod"] != "404":
    y = x["main"]
    w = x["wind"]
    z = x["weather"]
    currtemp = y["temp"]
    currtemp = str(round(float(1.8)*(currtemp - 273) + 32, 1))
    currpres = y["pressure"]
    currpres = str(round(currpres/3386, 1))
    currhum = y["humidity"]
    feelslike = y["feels_like"]
    feelslike = str(round(float(1.8)*(feelslike - 273) + 32, 1))
    winds = str(round(float(w["speed"]), 1))
    weatherdes = str(z[0]["description"])
    print()
    print(f"It is currently {currtemp} degrees Fahrenheit outside.")
    print()
    print(f"It feels like {feelslike} degrees Fahrenheit outside.")
    print()
    print(f"The wind is blowing at {winds} MPH.")
    print()
    print(f"The pressure is at {currpres} inhg.")
    print()
    print(f"The humidity is at %{currhum}.")
    print()
    print(f"OpenWeatherMap describes this weather as {weatherdes}.")
    print()
    print("This data was brought to you by WeatherWatcher.")
elif x["cod"] == "401":
    print("Error in database link! Please notify developer.")
else:
    print("Error, does not work.")
