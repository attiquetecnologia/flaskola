from flask import Blueprint, redirect, render_template, request, url_for, flash
from sqlalchemy import select
from database.connection import db

bp = Blueprint("Admin", __name__)

@bp.route("/admin")  # 👈 rota do painel administrativo
def painel_admin():
    return render_template("admin/admin.html")