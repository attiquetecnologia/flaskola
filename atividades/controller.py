from flask import Blueprint, redirect, render_template, request, url_for, flash, jsonify
from sqlalchemy import select
from database.connection import db
from .model import Atividade
from werkzeug.utils import secure_filename
import os

bp = Blueprint("Atividades", __name__)
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'txt', 'docx', 'doc'}

def anexo_permitido(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@bp.route("/atividades/lista")
def lista():
    lista = db.session.scalars(select(Atividade))
    return render_template("atividades/lista.html", lista=lista)

@bp.route("/lista_atividades", methods=["GET"])
def listar_atividades():
    atividades = Atividade.query.all()
    return jsonify([{
        "id": l.id,
        "titulo": l.titulo,
        "descricao": l.descricao,
        "anexo": l.anexo,
        "data_de_criacao": l.data_de_criacao,
        "links": l.links,
        "nota": l.nota,
    } for l in atividades])

@bp.route("/atividades/enviar_anexo", methods=["GET", "POST"])
def enviar_anexo():
    if request.method == "POST":
        titulo = request.form.get("titulo")
        links = request.form.get("links")
        descricao = request.form.get("descricao")
        anexo = request.files.get("anexos")

        if anexo and anexo.filename != "" and anexo_permitido(anexo.filename):
            nome_seguro = secure_filename(anexo.filename)
            os.makedirs(UPLOAD_FOLDER, exist_ok=True)
            caminho_anexo = os.path.join(UPLOAD_FOLDER, nome_seguro)
            anexo.save(caminho_anexo)

            atividade = Atividade(
                titulo=titulo,
                links=links,
                descricao=descricao,
                anexo=nome_seguro
            )
            db.session.add(atividade)
            db.session.commit()
            flash("Arquivo enviado com sucesso!", "success")
        else:
            flash("Arquivo inválido ou ausente!", "danger")

        return redirect("/atividades/enviar_anexo")

    return render_template("atividades/enviar_anexo.html")

@bp.route("/atividades/<int:id>/delete", methods=("GET", "POST"))
def delete(id):
    atividade = Atividade.query.filter_by(id=id).first()

    if request.method == "POST" and request.form.get("apagar") == "sim":
        db.session.delete(atividade)
        db.session.commit()
        return redirect(url_for("Atividades.lista"))

    return render_template("atividades/delete.html", id=id, atividade=atividade)

@bp.route("/atividades/<int:id>/edit", methods=("GET", "POST"))
def edit(id):
    erros = []
    atividade = Atividade.query.filter_by(id=id).first()

    if request.method == "POST":
        nome = request.form.get("nome")
        email = request.form.get("email")
        t = float(request.form.get("t"))
        p1 = float(request.form.get("p1"))
        p2 = float(request.form.get("p2"))

        if not nome: erros.append("Nome é um campo obrigatório")
        if not email: erros.append("Email é um campo obrigatório")
        if not t or t < 0 or t > 10: erros.append("Trabalho inválido (0-10)")
        if not p1 or p1 < 0 or p1 > 10: erros.append("Prova 1 inválida (0-10)")
        if not p2 or p2 < 0 or p2 > 10: erros.append("Prova 2 inválida (0-10)")

        if not erros:
            atividade.nome = nome
            atividade.email = email
            atividade.t = t
            atividade.p1 = p1
            atividade.p2 = p2
            db.session.commit()
            flash(f"Usuário {nome}, salvo com sucesso!")
            return redirect(url_for("Atividades.edit", id=id))

    return render_template("atividades/form.html", id=id, atividade=atividade, erros=erros)
