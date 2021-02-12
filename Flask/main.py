from flask import Flask, render_template, request, redirect, session, flash

app = Flask(__name__)
app.secret_key = "abc123"

class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console

    def get_nome(self):
        return self.nome
    
jogo1 = Jogo('Super Mario', 'Ação', 'SNES')
jogo2 = Jogo('Pokemon', 'RPG', 'GBA')
lista_de_jogos = [jogo1, jogo2]

@app.route('/')
def index():
    return render_template('lista.html', titulo='Jogos', jogos=lista_de_jogos)

@app.route('/novo')
def insere_jogo():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect('/login?proxima=novo')
    return render_template('insere_jogo.html', titulo='Inserir novo jogo')

@app.route('/criar', methods=['POST'])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console)
    lista_de_jogos.append(jogo)
    return redirect('/')

@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', proxima=proxima)

@app.route('/autenticar', methods=['POST',])
def autenticar():
    if 'mestra' == request.form['senha']:
        session['usuario_logado'] = request.form['usuario'] #busca o dado preenchido dentro do login do usuário e guarda dentro do session
        flash(request.form['usuario'] + ' logado com sucesso!')
        proxima_pagina = request.form['proxima']
        return redirect('/{}'.format(proxima_pagina))
    else:
        flash('Login ou senha incorreto')
        return redirect('/login')

@app.route('/logout', methods=['POST'])
def logout():
    session['usuario_logado'] = None
    flash('Nenhum usuario logado')
    return redirect('/login')

app.run(debug=True)
