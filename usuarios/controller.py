from flask import Blueprint, request, session, url_for, redirect, flash, render_template

bp = Blueprint("Usuario", __name__)

@bp.route("/login", methods=('POST', 'GET'))
def login():
    error = None
    if request.method == 'POST':
        email = request.form.get('email')
        senha = request.form.get('senha')

        from database.dados import alunos
        for k,v in alunos.items():
            if email == v.get('usuario') and senha == v.get('senha'):
                session['user'] = v
                return redirect(url_for('index'))
            else:
                error = "Usuario ou senha inválidos!"

    return render_template("usuarios/login.html", error=error)

@bp.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("index"))

@bp.route("/perfil", methods=("POST", "GET"))
def perfil():
    if 'user' not in session:
        flash("Usuário não está logado!")
        return redirect(url_for("login"))
    
    if request.method == "POST": # lógica para salvar
        pass
    
    # senão pega usuario no banco
    from database.dados import alunos
    for k,v in alunos.items():
        if v.get("usuario") == session['user'].get("usuario"):
            usuario = v # {"nome": "Batman", "t": 9.1, "p1": 8.5, "p2": 9, "avatar": url_for('static', filename="images/batman.jpg"), "usuario":"batman@email.com", "senha":"curinga"}
    
    return render_template("usuarios/perfil.html", usuario=usuario)
