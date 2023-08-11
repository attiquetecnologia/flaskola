from flask.helpers import url_for
alunos = {
10: {"nome": "Batman", "t": 9.1, "p1": 8.5, "p2": 9, "avatar": url_for('static', filename="images/batman.jpg"), "usuario":"batman", "senha":"curinga"}
,11: {"nome": "Robin", "t": 10, "p1": 9.5, "p2": 10, "avatar": url_for('static', filename="images/robin.jpg"), "usuario":"robin", "senha":"slade"}
,12: {"nome": "Volverine", "t": 6, "p1": 7, "p2": 8, "avatar": url_for('static', filename="images/volverine.png"), "usuario":"volverine", "senha":"xavier"}
,13: {"nome": "Gibak", "t": 8, "p1": 9.5, "p2": 10, "avatar": url_for('static', filename="images/gibak.jpg"), "usuario":"gibak", "senha":"bucky"}
,14: {"nome": "Barbie", "t": 3, "p1": 9.5, "p2": 7, "avatar": url_for('static', filename="images/barbie.jpg"), "usuario":"barbie", "senha":"ken"}
,15: {"nome": "zaza", "t": 4, "p1": 9.5, "p2": 7, "avatar": url_for('static', filename="images/zaza.jpg"), "usuario":"zaza", "senha":"cocorico"}
,15: {"nome": "saitama", "t": 3, "p1": 9.5, "p2": 7, "avatar": url_for('static', filename="images/saitama.jpg"), "usuario":"saitama", "senha":"saitama"}
}