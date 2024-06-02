from flask import Blueprint, render_template, request, redirect, url_for
from database_setup import Compra, Proveedor, session
from datetime import datetime
compras_bp = Blueprint('compras', __name__)

@compras_bp.route('/compras')
def mostrar_compras():
    compras = session.query(Compra).all()
    proveedores = session.query(Proveedor).all()
    return render_template('compras.html', compras=compras, proveedores=proveedores)

@compras_bp.route('/compras/agregar', methods=['GET', 'POST'])
def agregar_compra():
    if request.method == 'POST':
        fecha_str = request.form['fecha']
        fecha = datetime.strptime(fecha_str, '%Y-%m-%d').date()  # Convertir la cadena a objeto date
        numero_comprobante = request.form['numero_comprobante']
        total = request.form['total']
        idproveedor = request.form['idproveedor']

        compra = Compra(fecha=fecha, numero_comprobante=numero_comprobante, total=total, idproveedor=idproveedor)
        session.add(compra)
        session.commit()

        return redirect(url_for('compras.mostrar_compras'))

    proveedores = session.query(Proveedor).all()
    return render_template('compras.html', proveedores=proveedores)
