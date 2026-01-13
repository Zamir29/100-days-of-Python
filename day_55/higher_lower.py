from flask import Flask
import random

GREETING_TEXT = ('<h1 style="color: black; text-align: center">Guess a number between 0 and 9</h1>'
            '<img style="display: block; margin: auto; width: 50%;" '
            'src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">')

YOU_GUESSED_IT = ('<h1 style="color: green; text-align: center">You guessed the number</h1>'
                  '<img style="display: block; margin: auto; width: 50%;" '
            'src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">')
TOO_LOW = ('<h1 style="color: purple; text-align: center">Too Low, Try again</h1>'
           '<img style="display: block; margin: auto; width: 50%;" '
            'src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">')
TOO_HIGH = ('<h1 style="color: red; text-align: center">Too High, Try again</h1>'
            '<img style="display: block; margin: auto; width: 50%;" '
            'src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">')

app = Flask(__name__)

@app.route("/")
def index():
    return GREETING_TEXT

random_number = random.randint(0,9)

@app.route("/<int:user_number>")
def guess_result(user_number):
    if user_number == random_number:
        return YOU_GUESSED_IT
    elif user_number > random_number:
        return TOO_HIGH
    else:
        return TOO_LOW

def main():
    app.run(debug=True, use_reloader=False)

if __name__ == "__main__":
    main()