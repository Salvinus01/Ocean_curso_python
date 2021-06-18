import sqlite3
from flask import Flask

# Configuracoes

DATABASE = './flaskr'
SECRET_KEY = "pudim"
USERNAME = "admin"
PASSWORD = "admin"

# Aplicacao

app = Flask(__name__)
app.config.from_object(__name__)

def connec_db():
    return sqlite3.connect(DATABASE)

@app.route('/')
def index():
    return "<h1>Hellow World</1>"