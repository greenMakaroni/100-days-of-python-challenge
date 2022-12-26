import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient
import requests

OWM_CALL = "https://api.openweathermap.org/data/2.5/weather"

# twilio sms api vars
account_sid = 'lel'
auth_token = 'my auth token :D' # I'm not pushing any of those on github, sorry scrapers.

# weather map vars
api_key = "haha nope"
lat = 52.520008
long = 13.404954

call_params = {
    "lat": lat,
    "lon": long,
    "excluded": "current,minutely,daily",
    "appid": api_key
}

# Call weathermap api
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
    # call twilio api
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}

    client = Client(account_sid, auth_token, http_client=proxy_client)

    message = client.messages.create(body="Take umbrella", from_="+987654321", to="+123456789")
