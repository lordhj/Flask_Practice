from flask import Flask
app = Flask(__name__)

def make_bold(function):
    def wrapper():
        return "<b> "+function()+" </b>"
    return wrapper

def make_emphasis(function):
    def wrapper():
        return "<em>" + function() + "</em>"
    return wrapper

def make_underlined(function):
    def wrapper():
        return "<u>" + function() + "</u>"
    return wrapper

@app.route('/')
def hello_world():
    return '<h1 style="text-align:center">Hello, World! This is the prime heading of the page...</h1>'\
        '<p>As we have already welcomed you. Lets acknowledge the greatness of the lord. Til the kingdome come!!!</p>'\
        '<img src="https://media.giphy.com/media/3o6gDWzmAzrpi5DQU8/giphy.gif">'

@app.route('/owner')
def say_owner():
    return 'Kira is the owner of this server.'

@app.route('/bye')
@make_bold
@make_emphasis
def say_bye():
    return 'Bye Bye'

@app.route('/username/<path:name>')
def greet(name):
    return f'Hello {name} How are you?'

if __name__ == "__main__":
    app.run(debug=True)
