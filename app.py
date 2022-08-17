# coding: utf-8
from flask import Flask, render_template
app = Flask("projeto")

# Rota raiz
@app.route("/")
def ola_mundo():
    #criar uma variável com o meu nome
    nome = "Gustavo Alves"
    produtos = [
        {"nome": "Ração", "preço": 199.99},
        {"nome": "Playstation", "preço": 1999.99}
    ]
    return render_template("alo.html", n = nome, aProdutos = produtos),200

# nova rota teste
@app.route("/teste")
@app.route("/teste/<variavel>")
def funcao_teste(variavel = ""):
    return "Nova rota teste<br>Variável: {}".format(variavel), 200

app.run()