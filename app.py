from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, my Flask!"

@app.route('/hello/<name>')
def hello(name):
    return f"Hello, {name}!"

@app.route('/square/<int:number>')
def square(number):
    return str(number * number)

@app.route('/mostrar')
def mostrar():
    return render_template('mostrar.html', name="Flask User")  