from flask import Blueprint, render_template, request, redirect, url_for
from database_setup import Compra, Proveedor, Producto, DetalleCompra, session
from datetime import datetime
import json

compras_bp = Blueprint('compras', __name__)

@compras_bp.route('/compras')
def mostrar_compras():
    compras = session.query(Compra).all()
    proveedores = session.query(Proveedor).all()
    productos = session.query(Producto).all()
    return render_template('compras.html', compras=compras, proveedores=proveedores, productos=productos)

@compras_bp.route('/compras/agregar', methods=['GET', 'POST'])
def agregar_compra():
    if request.method == 'POST':
        fecha_str = request.form['fecha']
        fecha = datetime.strptime(fecha_str, '%Y-%m-%d').date()
        numero_comprobante = request.form['numero_comprobante']
        total = request.form['total']
        idproveedor = request.form['idproveedor']

        compra = Compra(fecha=fecha, numero_comprobante=numero_comprobante, total=total, idproveedor=idproveedor)
        session.add(compra)
        session.commit()

        # Extraer items del campo oculto del formulario
        items_json = request.form['items']
        items = json.loads(items_json)

        for item in items:
            idproducto = item['idproducto']
            cantidad = item['cantidad']
            precio_unitario = item['precio']
            precio_total = item['precioTotal']
            stock_futuro = item['stockFuturo']

            detalle_compra = DetalleCompra(
                idcompra=compra.id,
                idproducto=idproducto,
                cantidad=cantidad,
                costo_unitario=precio_unitario,
                precio_total=precio_total
            )
            session.add(detalle_compra)

            # Actualizar el stock del producto con el valor de "stock futuro"
            producto = session.query(Producto).filter_by(id=idproducto).first()
            if producto:
                producto.stock = stock_futuro

        session.commit()

        return redirect(url_for('compras.mostrar_compras'))

    proveedores = session.query(Proveedor).all()
    productos = session.query(Producto).all()
    return render_template('compras.html', proveedores=proveedores, productos=productos)
