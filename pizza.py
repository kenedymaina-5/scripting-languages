from flask import flask
app = Flask(__main__)


def home():
    return"Hello! we specialize in pizza toppings<h1>PIZZA TOPPING "

if _name_=="__main__":
    app.run()