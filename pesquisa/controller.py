from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def conectar_banco():
    return sqlite3.connect("biblioteca.db")

@app.route('/pesquisa')
def pesquisar():
    termo = request.args.get('q', '')
    
    conn = conectar_banco()
    cursor = conn.cursor()

    # Busca por título, tipo ou autor com LIKE
    consulta = """
        SELECT * FROM acervo
        WHERE titulo LIKE ? OR tipo LIKE ? OR autor LIKE ?
    """
    like_termo = f"%{termo}%"
    cursor.execute(consulta, (like_termo, like_termo, like_termo))
    resultados = cursor.fetchall()
    conn.close()

    # Retorna como JSON
    return jsonify([
        {"id": r[0], "titulo": r[1], "tipo": r[2], "autor": r[3]}
        for r in resultados
    ])

if __name__ == '__main__':
    app.run(debug=True)
