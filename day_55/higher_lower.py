from flask import Flask
import random

GREETING_TEXT = ('<h1 style="text-align: center">Guess a number between 0 and 9</h1>'
            '<img style="display: block; margin: auto; width: 50%;" '
            'src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">')

YOU_GUESSED_IT = "<h1>You guessed the number</h1>"
TOO_LOW = "<h1>Too Low, Try again</h1>"
TOO_HIGH = "<h1>Too High, Try again</h1>"

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
    app.run(debug=True)

if __name__ == "__main__":
    main()