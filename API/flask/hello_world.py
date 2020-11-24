from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return 'Hello, World!'

@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    return '<p>Your browser is %s</p>' % user_agent

@app.route('/login')
def login():
    return render_template('login.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('./404.html'), 404


# @app.route('/user/<name>')
# def user(name):
#     return '<h1>Hello, %s</h1>' % name

if __name__ == "__main__":
    app.run(debug=True)