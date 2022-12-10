api_url = "https://opentdb.com/api.php?amount=10&type=boolean"

import requests

parameters = {
    "amount": 10,
    "type": "boolean"
}

response = requests.get(api_url, params=parameters)
response.raise_for_status()
data = response.json()
question_data = data['results']