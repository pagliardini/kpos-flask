from database_setup import session, DetalleCompra

detalles_compra = session.query(DetalleCompra).all()

# Display the details
for detalle in detalles_compra:
    print(f"ID Compra: {detalle.idcompra}, Producto: {detalle.nombre_producto}, Cantidad: {detalle.cantidad}, Costo Unitario: {detalle.costo_unitario}, Precio Total: {detalle.precio_total}")
