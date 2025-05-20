from flask import Blueprint, redirect, render_template, request, url_for, flash
from sqlalchemy import select
from database.connection import db

bp = Blueprint("Testes", __name__)

@bp.route("/teste/menu_sanduiche")
def menu_sanduiche():

    return render_template("testes/menu_sanduiche.html")
