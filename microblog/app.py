#python -m venv venv
#.\venv\Scripts\activate
#pip install flask
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/contato")
def contato():
    return render_template ("contato.html", tel = "(87) 99643-3562", email = "josericardo1@aluno.ifsertao-pe.edu.br")

@app.route("/operaçao/<int: num1>/<int:num2>")
def operaçao(num1, num2):
    resultado = num1 + num2
    return 

if __name__ == '__main__':
    app.run()
