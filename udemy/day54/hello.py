from flask import Flask

app = Flask(__name__)

def is_authenticated_decorator(function):
    def wrapper(*args, **kwargs):
        if args[0] == True:
            function()
        return wrapper

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/bye')
@make_bold
def bye():
    return "Bye!"

@app.route('/username/<name>')
def greet(name):
    return f"Hello {name}"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)