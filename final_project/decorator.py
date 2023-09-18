def announce(f):
    def wrapper():
        print('about to run a function....')
        f()
        print("done with function")
    return wrapper

@announce #the @ is use to call decorator function
def hello():
    print("hello,world")

hello()        