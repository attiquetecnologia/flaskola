from flask import Blueprint, redirect, render_template, request, url_for, flash
from sqlalchemy import select
from database.connection import db
from livros.model import Livro


bp = Blueprint("Pesquisa", __name__)

@bp.route("/pesquisa" , methods=("GET", "POST"))
def pesquisa():
    termo = request.args.get('q', '')
    
    livros = Livro.query.all()
    # Busca por título, tipo ou autor com LIKE
    consulta = """
        SELECT * FROM acervo
        WHERE titulo LIKE ? OR tipo LIKE ? OR autor LIKE ?
    """
    
    # Retorna como JSON
    return render_template("pesquisa/pesquisa.html", livros=livros)
