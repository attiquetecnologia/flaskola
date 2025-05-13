import click
from flask import Flask, render_template, request, flash, redirect
from flask.cli import with_appcontext
from sqlalchemy import text
from database.connection import db

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'txt', 'docx', 'doc'}



def create_app():
    app = Flask(__name__)
    app.secret_key = "abax"
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///flaskola.db"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

    db.init_app(app)
    app.cli.add_command(init_db_command)
    

<<<<<<< HEAD
    # Rota da página inicial
    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route("/envio_atividade")
    def envio_atividade():
        return render_template("atividades/envarquivo02.html")
    
=======
    @app.route("/")
    def index():
        nome = "Rodrigo 123"
        return render_template("index.html", nome=nome)

    

    # Registrar blueprints
>>>>>>> Lara
    from componentes import bp
    app.register_blueprint(bp)

    from usuarios.controller import bp
    app.register_blueprint(bp)

    from alunos.controller import bp
    app.register_blueprint(bp)

<<<<<<< HEAD
    from livros.controller import bp  # <-- caminho atualizado
    app.register_blueprint(bp)

    return app # retorna o app criado
=======
    from atividades.controller import bp
    app.register_blueprint(bp)

    return app
>>>>>>> Lara


def init_db():
    db.drop_all()
    db.create_all()

@click.command("init-db")
@with_appcontext
def init_db_command():
    """Clear existing data and create new tables."""
    init_db()
    click.echo("Initialized the database.")
<<<<<<< HEAD

    

if __name__ == "__main__": # 'função principal' do python
    create_app().run(debug=True, host="0.0.0.0") # executa o flask na porta http://127.0.0.1:5000


=======

if __name__ == "__main__":
    create_app().run(debug=True, host="0.0.0.0")
>>>>>>> Lara
