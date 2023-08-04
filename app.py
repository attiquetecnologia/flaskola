from flask import Flask, render_template # importa bibliotecas

def create_app(): # cria uma função para definir o aplicativo
    app = Flask(__name__) # instancia o Flask
    
    @app.route("/") # cria uma rota
    def index(): # função que gerencia rota
        return render_template("index.html") # combina o python com html

    @app.route("/login")
    def login():
        return "<H1>Login ainda não implementado</h1>"
    return app # retorna o app criado

if __name__ == "__main__": # 'função principal' do python
    create_app().run() # executa o flask na porta http://127.0.0.1:5000