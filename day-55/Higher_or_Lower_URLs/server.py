from flask import Flask
import random

#Constants 
GUESS_URL = "https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif"
FOUND_URL = "https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif"
LOW_URL = "https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif"
HIGH_URL = "https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif"

app = Flask(__name__)


class Number_random():
    def __init__(self) -> None:
        self.ran()    

    def comp(self, number):
        if number == self.number:
            self.ran() #generate another number random
            return "found"
        elif number > self.number:
            return "high"
        else:
            return "low"

    def ran(self):
        self.number = random.randint(0, 9)
    

@app.route("/")
def guess():
    return format_response("Guess a number between 0 and 9", GUESS_URL, "blue")

game_instance = Number_random() # create a instance

@app.route("/<int:number>")
def game(number):
    result = game_instance.comp(number)
    if result == "found":
        return format_response("You found me!", FOUND_URL, "green")
    elif result == "low":
            return format_response("Too low, try again! ", LOW_URL, "red")
    elif result == "high":
            return format_response("Too high, try again!", HIGH_URL, "red")
    
def format_response(text, url, color):
    return f'<b><p style="color:{color}">{text}</p></b> <img src={url}>'

if __name__ == "__main__":
    app.run(debug=True)