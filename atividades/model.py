from sqlalchemy import Column, String, Integer, Double
from database.connection import db

class Atividade(db.Model):
    __tablename__ = "atividades"

    id = Column(Integer, primary_key=True, autoincrement=True)
    titulo = Column(String, nullable=False)
    descricao = Column(String, nullable=False)
    anexo = Column(String)
    data_de_criacao = Column(String)
    links = Column(String)
    nota = Column(Double)
    

