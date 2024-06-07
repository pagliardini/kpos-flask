from flask import render_template, request, redirect, url_for, Blueprint
from database_setup import Compra, Proveedor, Producto, DetalleCompra, session
from datetime import datetime
import json

ventas_bp = Blueprint('ventas', __name__)
@ventas_bp.route('/ventas')
def mostrar_ventas():
    productos = session.query(Producto).all()
    return render_template('ventas.html', productos=productos)