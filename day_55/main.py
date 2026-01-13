from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return ('<h1 style="text-align: center">Hello World!</h1>'
            '<p>This is a paragraph</p>'
            '<img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExdHUwbHYzY3owNHA1ZWcyYmZtajQ5ZjRiZGRhbGpjdDJkYjh1ZDV2dCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/4VglqgTazN7YQ/giphy.gif" width=200>')

def make_bold(func):
    def wrapper(*args, **kwargs):
        return f'<b>{func(*args, **kwargs)}</b>'
    return wrapper

def make_emphasis(func):
    def wrapper(*args, **kwargs):
        return f'<em>{func(*args, **kwargs)}</em>'
    return wrapper

def make_underlined(func):
    def wrapper(*args, **kwargs):
        return f'<u>{func(*args, **kwargs)}</u>'
    return wrapper

@app.route("/bye")
@make_bold
@make_emphasis
@make_underlined
def bye():
    return "Bye!"

@app.route("/username/<name>/<int:age>")
def greet(name, age):
    return f"Hello, {name}, you are {age} years old!"

def main():
    # Run app in debug mode (use the Debugger PIN for the console)
    app.run(debug=True)

if __name__ == '__main__':
    main()
