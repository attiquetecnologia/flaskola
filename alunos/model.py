from sqlalchemy import Column, String, Integer, Double
from database.connection import db

class Aluno(db.Model):
    __tablename__ = "alunos"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False )
    email = Column(String(200), nullable=False)
    senha = Column(String(2000))    