import requests

class DataManager:
    #This class is responsible for talking to the Google Sheet.

    def __init__(self):
        self.SHEETY_GET_URL = "nah"
        self.SHEETY_TOKEN = 'nope'

    def getData(self):

        header = {
            "Authorization": f"Bearer {self.SHEETY_TOKEN}"
        }

        response = requests.get(url=self.SHEETY_GET_URL, headers=header)
        print(response.text)
