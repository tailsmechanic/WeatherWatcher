import requests, json

apikey = "7cb9becaea566cc27d69991c345fa129"
base = "http://api.openweathermap.org/data/2.5/weather?"
city = "Sanger"
compbase = base + "appid=" + apikey + "&q=" + city
resp = requests.get(compbase)
x = resp.json()
if x["cod"] != "404":
    y = x["main"]
    currtemp = y["temp"]
    currtemp = str(float(1.8)*(currtemp - 273) + 32)
    currpres = y["pressure"]
    currpres = str(currpres/3386)
    currhum = y["humidity"]
    z = x["weather"]
    weatherdes = str(z[0]["description"])
    print()
    print(f"It is currently {currtemp} degrees Fahrenheit outside.")
    print()
    print(f"The pressure is at {currpres} inhg.")
    print()
    print(f"The humidity is at %{currhum}.")
    print()
    print(f"OpenWeatherMap describes this weather as {weatherdes}.")
    print()
    print("This data was brought to you by WeatherWatcher.")
