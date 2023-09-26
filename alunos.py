from flask import Blueprint, render_template

bp = Blueprint("Aluno", __name__)

@bp.route("/alunos/lista")
def lista():
    return render_template("alunos/lista.html")

@bp.route("/alunos/add")
def add():
    return render_template("alunos/form.html")

@bp.route("/alunos/<int:id>delete")
def delete(id):
    return render_template("alunos/delete.html")

@bp.route("/alunos/<int:id>/edit")
def edit(id):
    return render_template("alunos/form.html")