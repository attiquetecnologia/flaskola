from flask import Blueprint, request, jsonify
from livros.model import Livro  # <--- IMPORT CORRETO
from database.connection import db
from datetime import datetime

bp = Blueprint("livros", __name__, url_prefix="/livros")

@bp.route("/", methods=["GET"])
def listar_livros():
    livros = Livro.query.all()
    return jsonify([{
        "id": l.id,
        "titulo": l.titulo,
        "imagem": l.imagem,
        "sinopse": l.sinopse,
        "datadelancamento": l.datadelancamento.isoformat() if l.datadelancamento else None,
        "autor": l.autor,
        "generos": l.generos
    } for l in livros])

@bp.route("/", methods=["POST"])
def adicionar_livro():
    data = request.get_json()
    try:
        novo_livro = Livro(
            titulo=data['titulo'],
            imagem=data['imagem'],
            sinopse=data.get('sinopse'),
            datadelancamento=datetime.strptime(data['datadelancamento'], "%Y-%m-%d") if data.get('datadelancamento') else None,
            autor=data.get('autor'),
            generos=data.get('generos')
        )
        db.session.add(novo_livro)
        db.session.commit()
        return jsonify({"mensagem": "Livro adicionado com sucesso"}), 201
    except Exception as e:
        return jsonify({"erro": str(e)}), 400
