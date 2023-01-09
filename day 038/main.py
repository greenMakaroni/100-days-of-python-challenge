import requests
from datetime import datetime
import os

APP_ID = os.environ["APP_ID"]
API_KEY = os.environ["APP_KEY"]
SHEETY_AUTH_TOKEN = os.environ["SHEETY_AUTH_TOKEN"]

NUTRITIONIX_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_ENDPOINT = "https://api.sheety.co/ba33589af213578563ba3f8f51c48b34/pythonWorkouts/workouts"

print(APP_ID)

user_input = input("What exercises did you do today? \n")

request_header = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "x-remote-user-id": "0"
}

request_body = {
    "query": user_input,
    "gender": "male",
    "weight_kg": 70.5,
    "height_cm": 182,
    "age": 27
}

response = requests.post(url=NUTRITIONIX_ENDPOINT, json=request_body, headers=request_header)
data = response.json()
print(data)

today_date = datetime.now().strftime("%d/%m/%Y")
time_now = datetime.now().strftime("%X")

sheety_request_header = {
    "Authorization": f"Bearer {SHEETY_AUTH_TOKEN}"
}

for exercise in data["exercises"]:
    sheety_request_body = {
        "workout": {
            "date": today_date,
            "time": time_now,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    response = requests.post(url=SHEETY_ENDPOINT, json=sheety_request_body, headers=sheety_request_header)
    print(response.text)

