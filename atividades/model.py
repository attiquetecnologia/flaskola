
class Atividade(db.Model):
    __tablename__ = "atividades"

    id = Column(Integer, primary_key=True, autoincrement=True)
    titulo = Column(String(100), nullable=False)
    descricao = Column(String(500), nullable=False)
    anexo = Column(String(2000))
    data_de_criacao = Column(String(20))
    links = Column(String(2000))
    nota = Column(Double)
    

