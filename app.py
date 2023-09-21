from flask import Flask, render_template, request, session # importa bibliotecas

def create_app(): # cria uma função para definir o aplicativo
    app = Flask(__name__) # instancia o Flask
    
    @app.route("/") # cria uma rota
    def index(): # função que gerencia rota
        nome = "Marcão"
        return render_template("index.html", nome=nome) # combina o python com html

    @app.route("/alunos")
    def alunos():
        import json
        from database.dados import alunos

        # Função lambda cria funções de 1 linha só
        # media = lambda t,p1,p2: t*.3+p1*.35+p2*.35
        def media(t, p1, p2):
            return t*.3+p1*.35+p2*.35
        
        return render_template("lista.html", alunos=alunos, media=media )

    @app.route("/login", methods=('POST' , 'GET'))
    def login():
        if request.form.get('POST'):
           email = request.form.get('email')
           senha = request.form.get('senha')
                  
           from database.dados import alunos
           for  k,v in alunos.items():
               if email == v.get('usuario') and senha == v.get('senha'):
                   session['user'] =v
        return render_template("login.html")
    
    return app # retorna o app criado

if __name__ == "__main__": # 'função principal' do python
    create_app().run(debug=True) # executa o flask na porta http://127.0.0.1:5000