from flask import Blueprint, redirect, render_template, request, url_for, flash
from sqlalchemy import select
from database.connection import db
from .model import atividade

bp = Blueprint("Atividades", __name__)

@bp.route("/atividades/lista")
def lista():
    lista = db.session.scalars(select(atividade))

    # Função lambda cria funções de 1 linha só
    # media = lambda t,p1,p2: t*.3+p1*.35+p2*.35
    def media(t, p1, p2):
        return t*.3+p1*.35+p2*.35

    return render_template("atividades/lista.html", lista=lista, media=media)

@bp.route("/atividades/add", methods=("GET", "POST"))
def add():
    erros = []
    
    if request.method=="POST":
        nome = request.form.get("nome")
        email = request.form.get("email")
        t = float(request.form.get("t"))
        p1 = float(request.form.get("p1"))
        p2 = float(request.form.get("p2"))
        
        # Validações
        if not nome: erros.append("Nome é um campo obrigatório")
        if not email: erros.append("Email é um campo obrigatório")
        if not t or t <0 or t > 10: erros.append("Trabalho é um campo obrigatório ou valores não entre 0-10")
        if not p1 or p1 <0 or p1 > 10: erros.append("Prova 1 é um campo obrigatório ou valores não entre 0-10")
        if not p2 or p2 <0 or p2 > 10: erros.append("Prova 2 é um campo obrigatório ou valores não entre 0-10")

        if len(erros) == 0:
            # salva usuário no banco de dados
            atividade = atividade(**{"nome": nome, "email": email, "t": t
            , "p1": p1, "p2": p2 })
            db.session.add(atividade)
            db.session.commit() # persiste no banco

            flash(f"Usuário {nome}, salvo com sucesso!")

            return redirect(url_for("atividade.edit", id=atividade.id))

    return render_template("atividades/form.html", erros=erros)

@bp.route("/atividades/<int:id>/delete", methods=("GET", "POST"))
def delete(id):
    atividade = atividade.query.filter_by(id=id).first()

    if request.method == "POST" and request.form.get("apagar") == "sim":
        db.session.delete(atividade) # deleta o atividade
        db.session.commit()
        
        return redirect(url_for("atividade.lista"))

    return render_template("atividades/delete.html", id=id, atividade=atividade)

@bp.route("/atividades/<int:id>/edit", methods=("GET", "POST"))
def edit(id):
    erros = []
    atividade = atividade.query.filter_by(id=id).first()
    
    if request.method=="POST":
        nome = request.form.get("nome")
        email = request.form.get("email")
        t = float(request.form.get("t"))
        p1 = float(request.form.get("p1"))
        p2 = float(request.form.get("p2"))
        
        # Validações
        if not nome: erros.append("Nome é um campo obrigatório")
        if not email: erros.append("Email é um campo obrigatório")
        if not t or t <0 or t > 10: erros.append("Trabalho é um campo obrigatório ou valores não entre 0-10")
        if not p1 or p1 <0 or p1 > 10: erros.append("Prova 1 é um campo obrigatório ou valores não entre 0-10")
        if not p2 or p2 <0 or p2 > 10: erros.append("Prova 2 é um campo obrigatório ou valores não entre 0-10")

        if len(erros) == 0:
            # altera usuário no banco de dados
            atividade.nome = nome
            atividade.email = email
            atividade.t = t
            atividade.p1 = p1
            atividade.p2 = p2
            db.session.add(atividade)
            db.session.commit()

            flash(f"Usuário {nome}, salvo com sucesso!")

            return redirect(url_for("atividade.edit", id=id))

    return render_template("atividades/form.html", id=id, atividade=atividade, erros=erros)