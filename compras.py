from flask import Blueprint, render_template, request, redirect, url_for
from sqlalchemy.orm import sessionmaker
from database_setup import engine, Producto, Rubro, Marca, Proveedor, Compra

compras_bp = Blueprint('compras', __name__)

Session = sessionmaker(bind=engine)
session = Session()

@compras_bp.route('/compras')
def mostrar_compras():
    compras = session.query(Compra).all()
    return render_template('compras.html', compras=compras)
                 
