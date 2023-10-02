from flask import Blueprint, redirect, request, render_template

bp = Blueprint("Componentes", __name__)

@bp.route("/estados_lista")
def estados():
    lista = ["SP", "RJ", "MG", "ES", "PR", "SC", "RS"] # complete com outros estados

    return render_template("componentes/estados_lista.html", lista=lista)

@bp.route("/carros", methods=("GET", "POST"))
def carros():
    marcas = ["VW", "Ford", "Chevrolet"]
    modelos = ["Gol", "Fox", "Prisma", "Camaro", "Onix", "Fiesta"]
    
    mensagem = None
    if request.method=="POST":
        marca = request.form.get("marca")
        modelo = request.form.get("modelo")

        if marca == "VW" and modelo in ["Gol", "Fox"]:
            mensagem = "Parabéns você acertou!!!"
        else:
            mensagem = "Sinto muito combinação incorreta!!!"

    return render_template("componentes/carros.html", marcas=marcas, modelos=modelos, mensagem=mensagem)

@bp.route("/parcelas", methods=("GET", "POST"))
def calc_parcelas():
    resultado = None
    if request.method == "POST":
        total = float(request.form.get("total"))
        juros = float(request.form.get("juros"))
        parcelas = int(request.form.get("parcelas"))

        resultado = (total/parcelas)+(total/parcelas)*juros/100

    return render_template("componentes/calc_parcelas.html", resultado=resultado)