from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h1 style="text-align: center"> Hello, World! </h1> <p> This is a paragraph. </p> <img src="https://64.media.tumblr.com/4ba3a4631d1b950f32516524c8f526a1/tumblr_mqtqftY3SG1s9mkjxo1_250.gifv" /> '

def make_bold(function):

    def wrapper():
        return f"<b> {function()} </b>"
    return wrapper

def make_emphasis(function):

    def wrapper():
        return f"<em> {function()} </em>"
    return wrapper

def make_underlined(function):

    def wrapper():
        return f"<u> {function()} </u>"
    return wrapper


@app.route('/bye')
@make_bold
@make_underlined
@make_emphasis
def bye():
    return 'Bye!'

@app.route('/username/<name>/<int:number>')
def greet(name, number):
    return f'Hello bro  {name}, Your are {number} years old!'




if __name__ == '__main__':
    app.run(debug=True)



# Advanced python Decorator Functions
class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False

def is_authenticated_decorator(function):
    def wrapper(*args, **kwargs):
        if args[0].is_logged_in is True:
            function(args[0])
    return wrapper

@is_authenticated_decorator
def create_blog_post(user):
    print(f"This is {user.name}'s new blog post.")


new_user = User('angela')
new_user.is_logged_in = True
create_blog_post(new_user)



