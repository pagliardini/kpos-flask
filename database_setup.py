from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

# Crear la conexión a la base de datos
engine = create_engine('sqlite:///productos.db')
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

# Definir el modelo Producto
class Producto(Base):
    __tablename__ = 'Productos'
    id = Column(Integer, primary_key=True, autoincrement=True)
    sku = Column(String, nullable=False)
    nombre = Column(String, nullable=False)
    precio_costo = Column(Float, nullable=False)
    precio_venta = Column(Float, nullable=False)
    idrubro = Column(Integer, ForeignKey('Rubro.id'))
    idmarca = Column(Integer, ForeignKey('Marca.id'))
    idproveedor = Column(Integer, ForeignKey('Proveedor.id'))

    rubro = relationship('Rubro')
    marca = relationship('Marca')
    proveedor = relationship('Proveedor')

# Crear las tablas en la base de datos si no existen
Base.metadata.create_all(engine)

# Insertar datos de ejemplo en las tablas Rubro, Marca y Proveedor
rubros_ejemplo = [Rubro(nombre='Rubro 1'), Rubro(nombre='Rubro 2'), Rubro(nombre='Rubro 3')]
marcas_ejemplo = [Marca(nombre='Marca 1'), Marca(nombre='Marca 2'), Marca(nombre='Marca 3')]
proveedores_ejemplo = [Proveedor(nombre='Proveedor 1'), Proveedor(nombre='Proveedor 2'), Proveedor(nombre='Proveedor 3')]

# Agregar los datos de ejemplo
session.bulk_save_objects(rubros_ejemplo)
session.bulk_save_objects(marcas_ejemplo)
session.bulk_save_objects(proveedores_ejemplo)
session.commit()

# Insertar productos de ejemplo con las relaciones
productos_ejemplo = [
    Producto(sku='SKU001', nombre='Producto 1', precio_costo=10.00, precio_venta=15.00, idrubro=1, idmarca=1, idproveedor=1),
    Producto(sku='SKU002', nombre='Producto 2', precio_costo=20.00, precio_venta=30.00, idrubro=2, idmarca=2, idproveedor=2),
    Producto(sku='SKU003', nombre='Producto 3', precio_costo=30.00, precio_venta=45.00, idrubro=3, idmarca=3, idproveedor=3)
]

# Agregar los productos de ejemplo
session.bulk_save_objects(productos_ejemplo)
session.commit()

print("Datos de ejemplo insertados correctamente.")
