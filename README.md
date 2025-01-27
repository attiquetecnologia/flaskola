# faslkola
Flaskola é um projeto de aprendizagem para alunos de desenvolvimento de sistemas.
O objetivo é servir como aplicação base pre-configurada onde serão feitas mudanças
ao longo das aulas.

# Instalação
1- Faça clone com 
$ git clone https://github.com/attiquetecnologia/flaskola.git flaskola
2- Acesse o diretório do projeto
$ cd flaskola
3- Configure o virtualenv
$ python -m venv .venv
4.1 - Ative o virtualenv se Windows
$ source ./venv/Scripts/activate
4.2 - Ative o virtualenv se Linux
$ source ./venv/bin/activate
5 - Atualize o pip
$ python -m pip install --upgrade pip
6 - Instale os requerimentos.txt
$ pip install -r requirements.txt
7 - Crie o banco de dados
$ flask.exe --app app init-db
8 - Execute a aplicação no VSCode teclando <F5>