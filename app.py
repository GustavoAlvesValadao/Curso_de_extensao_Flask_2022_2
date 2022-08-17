# coding: utf-8
from flask import Flask, render_template, request
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

#Rota formulário
@app.route("/form")
def form():
    return render_template("form.html"), 200

#Rota tratamento do formulário
@app.route("/form_recebe", methods=["GET", "POST"])
def form_recebe():
    nome = ""
    if request.method == "POST":
        nome = request.form["nome"]
        return "Nome: {}".format(nome), 200
    else:
        return "Não pode chamar direto no GET", 200


app.run()