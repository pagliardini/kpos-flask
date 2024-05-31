from flask import Blueprint, render_template, request, redirect, url_for
from sqlalchemy.orm import sessionmaker
from database_setup import engine, Producto, Rubro, Marca, Proveedor

productos_bp = Blueprint('productos', __name__)

Session = sessionmaker(bind=engine)
session = Session()

@productos_bp.route('/productos')
def mostrar_productos():
    # Obtener todos los productos de la base de datos e incluir las relaciones
    productos = session.query(Producto).all()
    return render_template('productos.html', productos=productos)

@productos_bp.route('/agregar', methods=['GET', 'POST'])
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
    
    # Obtener rubros, marcas y proveedores para mostrarlos en el formulario
    rubros = session.query(Rubro).all()
    marcas = session.query(Marca).all()
    proveedores = session.query(Proveedor).all()
    return render_template('agregar_producto.html', rubros=rubros, marcas=marcas, proveedores=proveedores)

@productos_bp.route('/borrar', methods=['POST'])
def borrar_producto():
    producto_id = request.form['id']
    producto = session.query(Producto).filter_by(id=producto_id).first()
    if producto:
        session.delete(producto)
        session.commit()
    return redirect(url_for('productos.mostrar_productos'))

@productos_bp.route('/modificar/<int:id>', methods=['GET', 'POST'])
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
    
    # Obtener rubros, marcas y proveedores para mostrarlos en el formulario
    rubros = session.query(Rubro).all()
    marcas = session.query(Marca).all()
    proveedores = session.query(Proveedor).all()
    return render_template('modificar_producto.html', producto=producto, rubros=rubros, marcas=marcas, proveedores=proveedores)
