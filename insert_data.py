from sqlalchemy.orm import sessionmaker
from database_setup import engine, Rubro, Marca, Proveedor, Producto, Compra


# Insertar datos de ejemplo si no existen
def insertar_datos_ejemplo(modelo, datos_ejemplo):
    for dato in datos_ejemplo:
        if not session.query(modelo).filter_by(nombre=dato.nombre).first():
            session.add(dato)

# Datos de ejemplo
rubros_ejemplo = [Rubro(nombre='Cigarrillos'), Rubro(nombre='Golosinas'), Rubro(nombre='Bebidas')]
marcas_ejemplo = [Marca(nombre='Philip Morris'), Marca(nombre='Coca-Cola'), Marca(nombre='Arcor')]
proveedores_ejemplo = [Proveedor(nombre='Logistica Zona Sur'), Proveedor(nombre='DLV'), Proveedor(nombre='Vensal Hnos.')]
productos_ejemplo = [
    Producto(sku='SKU001', nombre='Producto 1', precio_costo=10.00, precio_venta=15.00, stock=5, idrubro=1, idmarca=1, idproveedor=1),
    Producto(sku='SKU002', nombre='Producto 2', precio_costo=20.00, precio_venta=30.00, stock=15, idrubro=2, idmarca=2, idproveedor=2),
    Producto(sku='SKU003', nombre='Producto 3', precio_costo=30.00, precio_venta=45.00, stock=25, idrubro=3, idmarca=3, idproveedor=3)
]

# Insertar datos de ejemplo si no existen
insertar_datos_ejemplo(Rubro, rubros_ejemplo)
insertar_datos_ejemplo(Marca, marcas_ejemplo)
insertar_datos_ejemplo(Proveedor, proveedores_ejemplo)
insertar_datos_ejemplo(Producto, productos_ejemplo)

# Confirmar los cambios
session.commit()

print("Datos de ejemplo insertados correctamente.")
