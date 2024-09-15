import random
from flask import Flask
app = Flask(__name__)

secret_number = random.randint(0,9)

@app.route('/')
def start():
    return "<h1> Guess a number between 0-9 </h1> <img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif' /> "

@app.route('/<int:num>')
def check(num):
    if num > secret_number:
        return "<h1 style='color:red;'>Too high, try again! </h1> <img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif' >"
    elif num < secret_number:
        return "<h1 style='color:purple;'>Too low, try again! </h1> <img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif' >"
    else:
        return "<h1 style='color:green;' >You Found me! </h1> <img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif' >"
if __name__ == "__main__":
    app.run()
