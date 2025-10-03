from flask import Flask, render_template,redirect, url_for, abort

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

@app.route('/redirect')
def redirect_example():
    return redirect(url_for('home'))   

@app.route('/error')
def error():
    return abort(404)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', error=e), 404

@app.route("/hola/<name>")
@app.route("/saludar/<name>")
def hola(name):
    return render_template("hola.html", name=name)