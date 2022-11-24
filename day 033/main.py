import requests

# response codes revision
# 1xx - please wait
# 2xx - success
# 3xx - no permission
# 4xx- you screwed up
# 5xx - server screwed up

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# # print(response)
# data = response.json()
# # print(data)
#
# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]
#
# iss_position = {longitude, latitude}
# print(iss_position)

# APIs with parameters

MY_LAT = 50.500352
MY_LONG = -0.125577

params = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=params)
response.raise_for_status()
print(response)

data = response.json()
# print(data)

sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]
print(sunset, sunrise)
