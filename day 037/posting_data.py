import requests

USERNAME = "greenmakaroni"
TOKEN = "hehe"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"
create_graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

# preferred authentication method.
request_header = {
    "X-USER-TOKEN": TOKEN,
}

request_body = {
    "date": "20221231",
    "quantity": "3",
}

response = requests.post(url=create_graph_endpoint, json=request_body, headers=request_header)
print(response.text)
