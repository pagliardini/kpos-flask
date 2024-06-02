from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

# Crear la conexión a la base de datos
engine = create_engine('sqlite:///kpos.db')
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

# Definir el modelo Rubro
class Rubro(Base):
    __tablename__ = 'Rubro'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String, nullable=False)

# Definir el modelo Marca
class Marca(Base):
    __tablename__ = 'Marca'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String, nullable=False)

# Definir el modelo Proveedor
class Proveedor(Base):
    __tablename__ = 'Proveedor'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String, nullable=False)
    cuit = Column(String, nullable=True)

# Definir el modelo Producto
class Producto(Base):
    __tablename__ = 'Productos'
    id = Column(Integer, primary_key=True, autoincrement=True)
    sku = Column(String, nullable=False)
    nombre = Column(String, nullable=False)
    precio_costo = Column(Float, nullable=False)
    precio_venta = Column(Float, nullable=False)
    stock = Column(Integer, nullable=True, default=0)
    idrubro = Column(Integer, ForeignKey('Rubro.id'))
    idmarca = Column(Integer, ForeignKey('Marca.id'))
    idproveedor = Column(Integer, ForeignKey('Proveedor.id'))

    rubro = relationship('Rubro')
    marca = relationship('Marca')
    proveedor = relationship('Proveedor')

# Definir el modelo Compra
class Compra(Base):
    __tablename__ = 'Compra'
    id = Column(Integer, primary_key=True, autoincrement=True)
    fecha = Column(Date, nullable=False)
    numero_comprobante = Column(String, nullable=False)
    total = Column(Float, nullable=False)
    idproveedor = Column(Integer, ForeignKey('Proveedor.id'))

    proveedor = relationship('Proveedor')

# Crear las tablas en la base de datos si no existen
Base.metadata.create_all(engine)

# Insertar datos de ejemplo si no existen
def insertar_datos_ejemplo(modelo, datos_ejemplo):
    for dato in datos_ejemplo:
        if not session.query(modelo).filter_by(nombre=dato.nombre).first():
            session.add(dato)

# Datos de ejemplo
rubros_ejemplo = [Rubro(nombre='Cigarrillos'), Rubro(nombre='Golosinas'), Rubro(nombre='Bebidas')]
marcas_ejemplo = [Marca(nombre='Philip Morris'), Marca(nombre='Coca-Cola'), Marca(nombre='Arcor')]
proveedores_ejemplo = [Proveedor(nombre='Logistica Zona Sur', cuit=20359176377), Proveedor(nombre='DLV'), Proveedor(nombre='Vensal Hnos.')]
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
