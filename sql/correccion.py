from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Crear la conexión a la base de datos
engine = create_engine('sqlite:///productos.db')
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

# Definir el modelo Producto
class Producto(Base):
    __tablename__ = 'Productos'

    id = Column(Integer, primary_key=True, autoincrement=True)
    sku = Column(String, nullable=False)
    nombre = Column(String, nullable=False)
    precio_costo = Column(Float, nullable=False)
    precio_venta = Column(Float, nullable=False)
    idrubro = Column(Integer, nullable=False)
    idmarca = Column(Integer, nullable=False)
    idproveedor = Column(Integer, nullable=False)

# Crear la tabla en la base de datos si no existe
Base.metadata.create_all(engine)

# Función para eliminar duplicados
def eliminar_duplicados():
    # Obtener todos los productos de la base de datos
    productos = session.query(Producto).all()

    # Crear un diccionario para rastrear los productos únicos
    productos_unicos = {}
    
    for producto in productos:
        if producto.nombre not in productos_unicos:
            productos_unicos[producto.nombre] = producto
        else:
            # Eliminar el producto duplicado
            session.delete(producto)
    
    # Confirmar los cambios
    session.commit()

# Ejecutar la función para eliminar duplicados
eliminar_duplicados()

print("Duplicados eliminados correctamente.")
