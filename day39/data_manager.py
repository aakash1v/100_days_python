import requests

sheety_endpoint = 'https://api.sheety.co/c5289088422f4fef879e45a4f83edc2b/flightDeals/prices'


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        pass

    def get_destination_data(self):
        self.response = requests.get(url=sheety_endpoint)
        self.data = self.response.json()['prices']
        return self.data

    def post_data(self, data):
        self.response = requests.post(url=sheety_endpoint, json=data)
        return self.response.text

    def update_data(self, id, data):
        self.response = requests.put(url=f"{sheety_endpoint}/{id}", json=data)
        return self.response.text

    def delete_row(self, id):
        self.response = requests.delete(url=f"{sheety_endpoint}/{id}")
        return self.response.text
