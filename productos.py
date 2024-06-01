from flask import Blueprint, render_template, request, redirect, url_for
from sqlalchemy.orm import sessionmaker
from database_setup import engine, Producto, Rubro, Marca, Proveedor

productos_bp = Blueprint('productos', __name__)

Session = sessionmaker(bind=engine)
session = Session()

@productos_bp.route('/productos')
def mostrar_productos():
    productos = session.query(Producto).all()
    return render_template('productos.html', productos=productos)

@productos_bp.route('/productos/agregar', methods=['GET', 'POST'])
def agregar_producto():
    if request.method == 'POST':
        sku = request.form['sku']
        nombre = request.form['nombre']
        precio_costo = request.form['precio_costo']
        precio_venta = request.form['precio_venta']
        idrubro = request.form['idrubro']
        idmarca = request.form['idmarca']
        idproveedor = request.form['idproveedor']
        nuevo_producto = Producto(sku=sku, nombre=nombre, precio_costo=precio_costo, precio_venta=precio_venta, idrubro=idrubro, idmarca=idmarca, idproveedor=idproveedor)
        session.add(nuevo_producto)
        session.commit()
        return redirect(url_for('productos.mostrar_productos'))
    
    rubros = session.query(Rubro).all()
    marcas = session.query(Marca).all()
    proveedores = session.query(Proveedor).all()
    return render_template('agregar_producto.html', rubros=rubros, marcas=marcas, proveedores=proveedores)

@productos_bp.route('/productos/borrar', methods=['POST'])
def borrar_producto():
    producto_id = request.form['id']
    producto = session.query(Producto).filter_by(id=producto_id).first()
    if producto:
        session.delete(producto)
        session.commit()
    return redirect(url_for('productos.mostrar_productos'))

@productos_bp.route('/productos/modificar/<int:id>', methods=['GET', 'POST'])
def modificar_producto(id):
    producto = session.query(Producto).filter_by(id=id).first()
    if request.method == 'POST':
        producto.sku = request.form['sku']
        producto.nombre = request.form['nombre']
        producto.precio_costo = request.form['precio_costo']
        producto.precio_venta = request.form['precio_venta']
        producto.idrubro = request.form['idrubro']
        producto.idmarca = request.form['idmarca']
        producto.idproveedor = request.form['idproveedor']
        session.commit()
        return redirect(url_for('productos.mostrar_productos'))
    
    rubros = session.query(Rubro).all()
    marcas = session.query(Marca).all()
    proveedores = session.query(Proveedor).all()
    return render_template('modificar_producto.html', producto=producto, rubros=rubros, marcas=marcas, proveedores=proveedores)

@productos_bp.route('/productos/rubros')
def mostrar_rubros():
    rubros = session.query(Rubro).all()
    return render_template('rubros.html', rubros=rubros)

@productos_bp.route('/productos/rubros/agregar', methods=['POST'])
def agregar_rubro():
    if request.method == 'POST':
        nombre = request.form['nombre']
        nuevo_rubro = Rubro(nombre=nombre)
        session.add(nuevo_rubro)
        session.commit()
        return redirect(url_for('productos.mostrar_rubros'))
@productos_bp.route('/productos/rubros/borrar/<int:id>', methods=['GET', 'POST'])
def borrar_rubro(id):
    rubro = session.query(Rubro).filter_by(id=id).first()
    if rubro:
        session.delete(rubro)
        session.commit()
    return redirect(url_for('productos.mostrar_rubros'))

@productos_bp.route('/productos/marcas')
def mostrar_marcas():
    marcas = session.query(Marca).all()
    return render_template('marcas.html', marcas=marcas)

@productos_bp.route('/productos/proveedores')
def mostrar_proveedores():
    proveedores = session.query(Proveedor).all()
    return render_template('proveedores.html', proveedores=proveedores)