from dotenv import load_dotenv, dotenv_values
import os

load_dotenv()
print(os.getenv('MY_SECRET_KEY'))
print(os.getenv('SPORTIFY_CLIENT_ID'))
print(os.getenv('SPORTIFY_SECRET_KEY'))
