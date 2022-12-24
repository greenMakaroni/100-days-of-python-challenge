import requests

OWM_CALL = "https://api.openweathermap.org/data/2.5/weather"

api_key = "haha nope"
lat = 52.520008
long = 13.404954

call_params = {
    "lat": lat,
    "lon": long,
    "exclused": "current,minutely,daily",
    "appid": api_key
}

will_rain = False

response = requests.get(OWM_CALL, params=call_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

for hourly_data in weather_data:
    condition_code = hourly_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    print("Bring umbrella")

