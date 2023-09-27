from flask import Blueprint, redirect, request, render_template

bp = Blueprint("Componentes", __name__)

@bp.route("/estados_lista")
def estados():
    lista = ["SP", "RJ", "MG", "ES", "PR", "SC", "RS"] # complete com outros estados

    return render_template("componentes/estados_lista.html", lista=lista)

@bp.route("/carros", methods=("GET", "POST"))
def carros():
    carros = {"VW": ["Gol", "Fox"]
        , "Ford": ["Prisma", "Camaro"]
        , "Chevrolet": ["Onix", "Fiesta"]
    }
    mensagem = None
    if request.method=="POST":
        marca = request.form.get("marca")
        modelo = request.form.get("modelo")

        if marca == "VW" and modelo in ["Gol", "Fox"]:
            mensagem = "Parabéns você acertou!!!"
        else:
            mensagem = "Sinto muito combinação incorreta!!!"

    return render_template("componentes/carros.html", marcas=carros.keys(), modelos=[c for c in carros.], mensagem=mensagem)