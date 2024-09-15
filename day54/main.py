import time


def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        # Do something before
        function()
        function()
        # Do something after

    return wrapper_function


@delay_decorator
def say_hello():
    print("Hello ")
    
def say_bye():
    print("Bye")

def say_gretting():
    print("How are YOU?")


decorated_function = delay_decorator(say_bye)

decorated_function()
