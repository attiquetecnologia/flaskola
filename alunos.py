from flask import Blueprint, redirect, render_template, request, url_for, flash

bp = Blueprint("Aluno", __name__)

@bp.route("/alunos/lista")
def lista():
    from database.dados import alunos

    # Função lambda cria funções de 1 linha só
    # media = lambda t,p1,p2: t*.3+p1*.35+p2*.35
    def media(t, p1, p2):
        return t*.3+p1*.35+p2*.35

    return render_template("alunos/lista.html", alunos=alunos, media=media)

@bp.route("/alunos/add", methods=("GET", "POST"))
def add():
    from database.dados import alunos
    erros = []
    
    if request.method=="POST":
        nome = request.form.get("nome")
        usuario = request.form.get("email")
        t = float(request.form.get("t"))
        p1 = float(request.form.get("p1"))
        p2 = float(request.form.get("p2"))
        
        # Validações
        if not nome: erros.append("Nome é um campo obrigatório")
        if not usuario: erros.append("Email é um campo obrigatório")
        if not t or t <0 or t > 10: erros.append("Trabalho é um campo obrigatório ou valores não entre 0-10")
        if not p1 or p1 <0 or p1 > 10: erros.append("Prova 1 é um campo obrigatório ou valores não entre 0-10")
        if not p2 or p2 <0 or p2 > 10: erros.append("Prova 2 é um campo obrigatório ou valores não entre 0-10")

        #verifica se já existe
        if usuario in str(alunos): erros.append("Email já registrado")

        if len(erros) == 0:
            last_id = max(alunos.keys()) # ultimo id
            id = last_id+1
            # salva usuário no banco de dados
            alunos[id] = {"nome": nome, "usuario": usuario, "t": t
            , "p1": p1, "p2": p2 }
            
            flash(f"Usuário {nome}, salvo com sucesso!")

            return redirect(url_for("Aluno.edit", id=id))

    return render_template("alunos/form.html", erros=erros)

@bp.route("/alunos/<int:id>/delete", methods=("GET", "POST"))
def delete(id):
    from database.dados import alunos

    aluno = alunos.get(id)

    if request.method == "POST" and request.form.get("apagar") == "sim":
        del alunos[id] # deleta o aluno do dicionário
        return redirect(url_for("Aluno.lista"))

    return render_template("alunos/delete.html", id=id, aluno=aluno)

@bp.route("/alunos/<int:id>/edit", methods=("GET", "POST"))
def edit(id):
    from database.dados import alunos
    erros = []
    aluno = alunos.get(id)
    
    if request.method=="POST":
        nome = request.form.get("nome")
        usuario = request.form.get("email")
        t = float(request.form.get("t"))
        p1 = float(request.form.get("p1"))
        p2 = float(request.form.get("p2"))
        
        # Validações
        if not nome: erros.append("Nome é um campo obrigatório")
        if not usuario: erros.append("Email é um campo obrigatório")
        if not t or t <0 or t > 10: erros.append("Trabalho é um campo obrigatório ou valores não entre 0-10")
        if not p1 or p1 <0 or p1 > 10: erros.append("Prova 1 é um campo obrigatório ou valores não entre 0-10")
        if not p2 or p2 <0 or p2 > 10: erros.append("Prova 2 é um campo obrigatório ou valores não entre 0-10")

        if len(erros) == 0:
            # altera usuário no banco de dados
            alunos[id]["nome"] = nome
            alunos[id]["usuario"] = usuario
            alunos[id]["t"] = t
            alunos[id]["p1"] = p1
            alunos[id]["p2"] = p2
            
            flash(f"Usuário {nome}, salvo com sucesso!")

            return redirect(url_for("Aluno.edit", id=id))

    return render_template("alunos/form.html", id=id, aluno=aluno, erros=erros)