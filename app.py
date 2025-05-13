import os
import click
from flask import Flask, render_template, request, flash, redirect
from flask.cli import with_appcontext
from werkzeug.utils import secure_filename
from sqlalchemy import text
from database.connection import db

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'txt', 'docx', 'doc'}

def arquivo_permitido(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def create_app():
    app = Flask(__name__)
    app.secret_key = "abax"
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///flaskola.db"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

    db.init_app(app)
    app.cli.add_command(init_db_command)

    @app.route("/")
    def index():
        nome = "Rodrigo 123"
        return render_template("index.html", nome=nome)

    @app.route("/enviar_arquivo", methods=["GET", "POST"])
    def enviar_arquivo():
        if request.method == "POST":
            titulo = request.form.get("titulo")
            links = request.form.get("links")
            descricao = request.form.get("descricao")
            arquivos = request.files.getlist("arquivo")

            success_count = 0
            error_messages = []

            for arquivo in arquivos:
                if arquivo and arquivo.filename != "" and arquivo_permitido(arquivo.filename):
                    nome_seguro = secure_filename(arquivo.filename)
                    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
                    caminho_arquivo = os.path.join(UPLOAD_FOLDER, nome_seguro)
                    arquivo.save(caminho_arquivo)
                    success_count += 1
                else:
                    error_messages.append(f"Arquivo inválido: {arquivo.filename}")

            if success_count > 0:
                flash(f"{success_count} arquivo(s) enviado(s) com sucesso!", "success")
            if error_messages:
                flash("Erros: " + ", ".join(error_messages), "danger")
            
            return redirect("/enviar_arquivo")

        return render_template("enviararquivo01.html")

    # Registrar blueprints
    from componentes import bp
    app.register_blueprint(bp)

    from usuarios.controller import bp
    app.register_blueprint(bp)

    from alunos.controller import bp
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