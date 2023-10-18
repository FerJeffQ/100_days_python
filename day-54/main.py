import time

def decorator_function(function):
    def wrapper_function():
        print("Wait 2 seconds ..")
        time.sleep(2)
        function()
    return wrapper_function
    

@decorator_function
def say_hello():
    print("Hey ! hello bro !")

@decorator_function
def say_bye():
    print("bye !")

if __name__ == "__main__":
    say_hello()
    say_bye()