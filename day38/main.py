import requests
import datetime

now = datetime.datetime.now()
date = now.strftime('%d/%m/%Y')
time = now.strftime('%H:%M:%S')

APP_ID = '2b0087ab'
API_KEY = '20a4262c3940e931a16810cab30e252b'

headers = {
    'Content-Type': 'application/json',
    'x-app-id': APP_ID,
    'x-app-key': API_KEY,
}

endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'

data = {
    'query': input("Enter your text: ")
}

response = requests.post(url=endpoint, json=data, headers=headers)
data = response.json()['exercises'][0]

workout_data = {
    'workout': {
        'date': date,
        'time': time,
        'exercise': data['user_input'],
        'duration': data['duration_min'],
        'calories': data['nf_calories'],
        'id': 4
    }
}

headers = {
    'Authorization': 'Basic YWFrYXNoMXo6ZGVtb25raW5n'
}
sheety_endpoint = 'https://api.sheety.co/c5289088422f4fef879e45a4f83edc2b/myWorkouts/workouts'

response = requests.post(url=sheety_endpoint, json=workout_data ,headers=headers)
print(response.text)



