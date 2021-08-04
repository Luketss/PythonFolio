import random

from flask import Flask

app = Flask(__name__)

random_number = random.randint(0,10)


def show_gif(function):
    def wrapper():
        link = ["https://media.giphy.com/media/KuLvx2C1rRTynZR2ny/giphy.gif",
                "https://media.giphy.com/media/lIU5ADLW3ogegKsU9B/giphy.gif",
                "https://media.giphy.com/media/908dLAMIGbPnKfy1nh/giphy.gif"]
        return f'{function()} <img src="{link[random.randint(0,2)]}" alt="number"  width="250" />'
    return wrapper

@app.route('/')
@show_gif
def guess():
    return "<h1>Guess a number between 0 and 9</h1>"

@app.route('/<int:num>')
def check_guess(num):
    if num == random_number:
        return '<h1>Acertou</h1><img src="https://media.giphy.com/media/i45a1BvsMhASAYlZSK/giphy.gif" alt="acert"  width="250" />'
    elif num < random_number:
        return '<h1>Too low</h1><img src="https://media.giphy.com/media/2uI9astifwiSUWVOTT/giphy.gif" alt="low"  width="250" />'
    elif num > random_number:
        return '<h1>Too high</h1><img src="https://media.giphy.com/media/wHB67Zkr63UP7RWJsj/giphy.gif" alt="high"  width="250" />'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
