import sqlite3
import logging

def criar_tabela():
    conexao = sqlite3.connect('database.db')
    cursor = conexao.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        senha TEXT NOT NULL
    )''')
    conexao.commit()
    conexao.close()

def inserir_usuario(nome, email, senha):
    conexao = sqlite3.connect('database.db')
    cursor = conexao.cursor()
    cursor.execute('INSERT INTO usuarios (nome, email, senha) VALUES (?, ?, ?)', (nome, email, senha))
    conexao.commit()
    conexao.close()

def buscar_usuario(email=None, senha=None):
    conexao = sqlite3.connect('database.db')
    cursor = conexao.cursor()
    if email and senha:
        cursor.execute('SELECT * FROM usuarios WHERE email=? AND senha=?', (email, senha))
    elif email:
        cursor.execute('SELECT * FROM usuarios WHERE email=?', (email,))
    else:
        cursor.execute('SELECT * FROM usuarios')
    usuarios = cursor.fetchall()
    conexao.close()
    return usuarios

def buscar_usuario_por_id(usuario_id):
    conexao = sqlite3.connect('database.db')
    cursor = conexao.cursor()
    cursor.execute('SELECT * FROM usuarios WHERE id=?', (usuario_id,))
    usuario = cursor.fetchone()
    conexao.close()
    return usuario

def atualizar_usuario(usuario_id, nome, email, senha):
    conexao = sqlite3.connect('database.db')
    cursor = conexao.cursor()
    cursor.execute('UPDATE usuarios SET nome=?, email=?, senha=? WHERE id=?', (nome, email, senha, usuario_id))
    conexao.commit()
    conexao.close()

def excluir_usuario(usuario_id):
    conexao = sqlite3.connect('database.db')
    cursor = conexao.cursor()
    cursor.execute('DELETE FROM usuarios WHERE id=?', (usuario_id,))
    conexao.commit()
    conexao.close()
