from sqlalchemy import Column, String, Integer, Float, Date
from database.connection import db

class Livro(db.Model):
    __tablename__ = "livros"

    id = Column(Integer, primary_key=True, autoincrement=True)
    titulo = Column(String(100), nullable=False)
    imagem = Column(String(100))
    sinopse = Column(String(500))
    datadelancamento = Column(Date)
    generos = Column(String)
    autor = Column(String)
    # ano_lancamento