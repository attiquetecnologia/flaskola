import click
from flask import Flask, render_template
from flask.cli import with_appcontext
from sqlalchemy import text
from database.connection import db

def create_app(): # cria uma função para definir o aplicativo
    app = Flask(__name__) # instancia o Flask
    app.secret_key = "abax"

    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///flaskola.db"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    db.init_app(app)
    app.cli.add_command(init_db_command)

    @app.route("/") # cria uma rota
    def index(): # função que gerencia rota
        nome = "Rodrigo 123"

        return render_template("index.html", nome=nome) # combina o python com html

    @app.route("/trabalhos")
    def trabalhos():
        return render_template("trabalhos.html")

    from componentes import bp
    app.register_blueprint(bp)

    from usuarios.controller import bp
    app.register_blueprint(bp)

    from alunos.controller import bp
    app.register_blueprint(bp)

    return app # retorna o app criado

def init_db():
    db.drop_all()
    db.create_all()
    # db.reflect()


@click.command("init-db")
@with_appcontext
def init_db_command():
    """Clear existing data and create new tables."""
    
    init_db()
    click.echo("Initialized the database.")
    

if __name__ == "__main__": # 'função principal' do python
    create_app().run(debug=True, host="0.0.0.0") # executa o flask na porta http://127.0.0.1:5000

