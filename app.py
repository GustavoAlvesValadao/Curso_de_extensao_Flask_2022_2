# coding: utf-8
from flask import Flask, render_template
app = Flask("projeto")
@app.route("/")
def ola_mundo():
    #criar uma variável com o meu nome
    nome = "Gustavo Alves"
    return render_template("alo.html", n = nome),200

app.run()