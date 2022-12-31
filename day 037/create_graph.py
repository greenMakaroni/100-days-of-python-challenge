import requests

# view the graph in the browser https://pixe.la/v1/users/greenmakaroni/graphs/graph1.html

USERNAME = "greenmakaroni"
TOKEN = "hehe"

pixela_endpoint = "https://pixe.la/v1/users"
create_graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Learning German on Duolingo",
    "unit": "Exercise",
    "type": "int",
    "color": "sora"
}

# preferred authentication method.
request_header = {
    "X-USER-TOKEN": TOKEN,
}

# headers param takes in **kwargs
response = requests.post(url=create_graph_endpoint, json=graph_config, headers=request_header)
print(response.text)