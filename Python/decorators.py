def mydecorator(function):

    def wrapper():
        print("I am decorating your function")
        function()
    return wrapper

def hello_world():
    print("Hello World!")

mydecorator(hello_world)

# @mydecorator
# def hello_world():
#     pri nt("Hello World!")

# hello_world