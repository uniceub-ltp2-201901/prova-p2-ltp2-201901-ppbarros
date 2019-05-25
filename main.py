'''
Pedro Paulo Rangel Gomes de Barros
RA: 21801748
'''



from flask import Flask, render_template, redirect, url_for, request
from flaskext.mysql import MySQL
from bd import *

app = Flask(__name__)
bd = MySQL()
bd.init_app(app)

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'encurtador'

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/cadastrar', methods=['post'])
def cadastrar_link():
    link = request.form.get('link')
    conn = bd.connect()
    cursor = conn.cursor()
    resposta = encurta_link(link, cursor, conn)
    cursor.close()
    conn.close()
    return render_template('resposta.html', resposta=resposta)

@app.route('/<nome>')
def acesso(nome):
    conn = bd.connect()
    cursor = conn.cursor()
    link = acessar(conn, cursor, nome)
    cursor.close()
    conn.close()
    if link is None:
        return render_template('erro.html')
    return redirect(link[0])

@app.route('/relatorio')
def relatorios():
    conn = bd.connect()
    cursor = conn.cursor()
    links = show_relatorio(cursor)
    cursor.close()
    conn.close()
    return render_template('relatorio.html', links=links)


if __name__ == "__main__":
    app.run(debug=True)