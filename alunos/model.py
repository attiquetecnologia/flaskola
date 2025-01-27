from sqlalchemy import Column, String, Integer, Double
from database.connection import db

class Aluno(db.Model):
    __tablename__ = "alunos"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False)
    email = Column(String, nullable=False)
    trabalho = Column(Double)
    prova1 = Column(Double)
    prova2 = Column(Double)
    avatar = Column(String(1000))