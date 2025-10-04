from flask import Flask, render_template,redirect, url_for, abort, session, request

app = Flask(__name__)
app.secret_key = "e8df979f5bd299d44fd5d0fe3dea0a16c5feb05776895d162c19bd74e2654e82"

@app.route('/')
def home():
    if 'username' in session:
        return f"Logged in as {session['username']}"
    return "You are not logged in"

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('home'))
    return render_template('login.html')
# session es un diccionario que almacena datos específicos del usuario entre solicitudes.
# request.form hace referencia a los datos enviados en una solicitud POST a traves del formulario html.

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))

# el metodo pop elimina la clave 'username' de la sesión si existe, y si no existe, no hace nada 
# (gracias al segundo argumento None).

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
@app.route("/saludar/<name>", methods=["GET" , "POST" ])
def hola(name):
    return render_template("hola.html", name=name)