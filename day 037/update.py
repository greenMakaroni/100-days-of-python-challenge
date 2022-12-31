import requests

USERNAME = "greenmakaroni"
TOKEN = ""
GRAPH_ID = "graph1"
DATE = "20221231"

pixela_endpoint = "https://pixe.la/v1/users"
create_graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{DATE}"

# preferred authentication method.
request_header = {
    "X-USER-TOKEN": TOKEN,
}

request_body = {
    "quantity": "15",
}

response = requests.put(url=create_graph_endpoint, json=request_body, headers=request_header)
print(response.text)