import sqlite3
from flask import Flask, g, render_template, request

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

@app.before_request
def before():
    g.db = connec_db()

@app.teardown_request
def after(exception):
    g.db.close()

#@app.route('/')
#def index():
#    entradas = [{'titulo': 'O primeiro Post',
#                'texto': 'texto do post'},
#                {'titulo': 'Segundo Post',
#                'texto': 'Texto do segundo post'},
#                {'titulo': 'terceiro Post',
#                'texto': 'terceiro post'}
#                ]
#
#    return render_template('index.html', entradas=entradas)

@app.route('/')
def index():
    sql = 'SELECT titulo, texto from entradas order by id desc'
    cur = g.db.execute(sql)
    entradas = [dict(titulo=titulo, texto=texto) for titulo, texto in cur.fetchall()]
    return render_template('index.html', entradas=entradas)


    