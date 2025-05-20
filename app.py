import click
from flask import Flask, render_template
from flask.cli import with_appcontext
from sqlalchemy import text
from database.connection import db

# IMPORTAR O MODELO DE ATIVIDADE
from atividades.model import Atividade
from livros.model import Livro

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'txt', 'docx', 'doc'}

def create_app():
    app = Flask(__name__)
    app.secret_key = "abax"
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///flaskola.db"
    app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:1234@10.134.75.83/flaskola?charset=utf8mb4"

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

    db.init_app(app)
    app.cli.add_command(init_db_command)

    # ROTA INDEX MOSTRANDO LISTA DE ATIVIDADES
    @app.route("/")
    def index():
        livros = Livro.query.all()
        atividades = Atividade.query.all()
        return render_template("index.html", livros=livros, atividades=atividades)

    # REGISTRAR BLUEPRINTS
    from componentes import bp
    app.register_blueprint(bp)

    from usuarios.controller import bp
    app.register_blueprint(bp)

    from alunos.controller import bp
    app.register_blueprint(bp)

    from testes.controller import bp
    app.register_blueprint(bp)

    from livros.controller import bp
    app.register_blueprint(bp)

    from atividades.controller import bp
    app.register_blueprint(bp)

    return app

def init_db():
    db.drop_all()
    db.create_all()

@click.command("init-db")
@with_appcontext
def init_db_command():
    """Clear existing data and create new tables."""
    init_db()
    click.echo("Initialized the database.")

if __name__ == "__main__":
    create_app().run(debug=True, host="0.0.0.0")
