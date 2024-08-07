import requests
import datetime

today = datetime.datetime.now()-datetime.timedelta(1)

USERNAME = 'aakash1z'
TOKEN = 'hekekfjkdfdjfkd'
GRAPH_ID = 'graph1'

pixela_endpoint = 'https://pixe.la/v1/users'

user_params = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    'id': GRAPH_ID,
    'name': 'Cycling Graph',
    'unit': 'Km',
    'type': 'float',
    'color': 'momiji'
}
headers = {
    'X-USER-TOKEN': TOKEN
}
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixela_creation_endpoint = f"{graph_endpoint}/{GRAPH_ID}"
pixela_data = {
    'date': today.strftime('%Y%m%d'),
    'quantity': '10'
}

response = requests.post(url=pixela_creation_endpoint, json=pixela_data, headers=headers)
print(response.text)

# update data
pixela_data_update = {
    'quantity': '4.5'
}

date = today.strftime('%Y%m%d')

#pixela_update_endpoint = f"{pixela_creation_endpoint}/{date}"
#response = requests.put(url=pixela_update_endpoint, json=pixela_data_update, headers=headers)
#print(response.text)

#delete_endpoint = f"{pixela_creation_endpoint}/{date}"
#response = requests.delete(url=delete_endpoint, headers=headers)
#print(response.text)



