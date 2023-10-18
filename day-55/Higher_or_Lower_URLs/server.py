import random
from flask import Flask


# Constants
GUESS_URL = "https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif"
FOUND_URL = "https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif"
LOW_URL = "https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif"
HIGH_URL = "https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif"

app = Flask(__name__)

class GameState:
    def __init__(self):
        self._generate_new_number()
        
    def guess(self, number):
        if self.number == number:
            self._generate_new_number()
            return "found"
        elif self.number < number:
            return "low"
        else:
            return "high"
    
    def _generate_new_number(self):
        self.number = random.randint(0, 9)

# Create a game instance
game_instance = GameState()

@app.route("/")
def hello_world():
    return format_response("Guess a number between 0 and 9", GUESS_URL)

@app.route("/<int:number>")
def game(number):
    result = game_instance.guess(number)

    if result == "found":
        return format_response(f"You found me! Number: {game_instance.number}", FOUND_URL)
    elif result == "low":
        return format_response(f"Too low, try again! Number: {game_instance.number}", LOW_URL)
    else:
        return format_response(f"Too high, try again! Number: {game_instance.number}", HIGH_URL)

def format_response(message, image_url):
    return f'<p>{message}</p><img src="{image_url}" width="200"> '

if __name__ == "__main__":
    app.run(debug=True)
