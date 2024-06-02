# compras_blueprint.py
from flask import Blueprint, render_template, request, redirect, url_for
from sqlalchemy.orm import sessionmaker
from database_setup import engine, Compra, Proveedor

compras_bp = Blueprint('compras', __name__)

Session = sessionmaker(bind=engine)
session = Session()

@compras_bp.route('/compras', methods=['GET', 'POST'])
def mostrar_compras():
    if request.method == 'POST':
        # Procesar los datos del formulario y guardar la compra en la base de datos
        idproveedor = request.form['idproveedor']
        fecha = request.form['fecha']
        cuit = request.form['cuit']
        numero_comprobante1 = request.form['numero_comprobante1']
        numero_comprobante2 = request.form['numero_comprobante2']
        codigo = request.form['codigo']
        descuento = request.form['descuento']
        iva27 = request.form['iva27']
        exento = request.form['exento']
        municipal = request.form['municipal']
        iva105 = request.form['iva105']
        percep = request.form['percep']
        perc_munic = request.form['perc_munic']
        iva21 = request.form['iva21']
        ib = request.form['ib']
        otros = request.form['otros']
        neto = request.form['neto']
        total = request.form['total']
        observacion = request.form['observacion']
        estado = request.form['estado']

        # Crear una nueva compra
        nueva_compra = Compra(
            fecha=fecha,
            idproveedor=idproveedor,
            cantidad=cantidad,
            precio_costo=precio_costo,
            precio_venta=precio_venta,
            cuit=cuit,
            numero_comprobante1=numero_comprobante1,
            numero_comprobante2=numero_comprobante2,
            codigo=codigo,
            descuento=descuento,
            iva27=iva27,
            exento=exento,
            municipal=municipal,
            iva105=iva105,
            percep=percep,
            perc_munic=perc_munic,
            iva21=iva21,
            ib=ib,
            otros=otros,
            neto=neto,
            total=total,
            observacion=observacion,
            estado=estado
        )

        session.add(nueva_compra)
        session.commit()
        return redirect(url_for('compras.mostrar_compras'))

    compras = session.query(Compra).all()
    proveedores = session.query(Proveedor).all()
    return render_template('compras.html', compras=compras, proveedores=proveedores)
