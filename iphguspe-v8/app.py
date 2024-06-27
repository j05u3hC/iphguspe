import logging
import sqlite3
from flask import Flask, render_template, request, redirect, url_for
from conexao import atualizar_usuario, buscar_usuario_por_id, criar_tabela, inserir_usuario, buscar_usuario, excluir_usuario

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('base/login.html')

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']
        inserir_usuario(nome, email, senha)
        return redirect(url_for('login'))
    return render_template('base/cadast_user.html')

@app.route('/conteudo')
def conteudo():
    usuarios = buscar_usuario(email=None)
    return render_template('base/conteudo.html', usuarios=usuarios)

@app.route('/login', methods=['POST'])
def fazer_login():
    email = request.form['email']
    senha = request.form['senha']
    usuario = buscar_usuario(email, senha)
    if usuario:
        return redirect(url_for('conteudo'))
    else:
        return "Usuário não encontrado."

@app.route('/editar/<int:usuario_id>', methods=['GET', 'POST'])
def editar(usuario_id):
    usuario = buscar_usuario_por_id(usuario_id)
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']
        atualizar_usuario(usuario_id, nome, email, senha)
        return redirect(url_for('conteudo'))
    return render_template('base/editreg.html', usuario_id=usuario_id, usuario=usuario)

@app.route('/excluir/<int:usuario_id>', methods=['DELETE'])
def excluir(usuario_id):
    excluir_usuario(usuario_id)
    return redirect(url_for('conteudo'))

if __name__ == '__main__':
    criar_tabela()
    app.run(debug=True)

logging.basicConfig(filename='database.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def adicionar_usuario(nome, email, senha):
    logging.info(f'Novo usuário adicionado: Nome={nome}, Email={email}')

def editar_usuario(nome, email, nova_senha):
    logging.info(f'Usuário editado: Nome={nome}, Novo Email={email}, Nova Senha={nova_senha}')

def excluir_usuario_logging(email):
    logging.info(f'Usuário excluído: Email={email}')

# Exemplos de uso das funções de logging
adicionar_usuario('João', 'joao@example.com', '123456')
editar_usuario('João', 'joao@example.com', 'novasenha123')
excluir_usuario_logging('joao@example.com')
