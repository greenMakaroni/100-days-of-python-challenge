import requests
from datetime import datetime

USERNAME = "greenmakaroni"
TOKEN = "nope"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"
create_graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

# preferred authentication method.
request_header = {
    "X-USER-TOKEN": TOKEN,
}

# automate getting today's date
today = datetime.now()

request_body = {
    # formatted as pixela api specified.
    "date": "20221230",
    "quantity": "30",
}

response = requests.post(url=create_graph_endpoint, json=request_body, headers=request_header)
print(response.text)
