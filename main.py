from modelos.producto import Producto
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante

# Crear restaurante
restaurante = Restaurante()

# Crear productos
producto1 = Producto("Pizza Familiar", 15.50, 10, True)
producto2 = Producto("Hamburguesa", 8.75, 20, True)

# Crear clientes
cliente1 = Cliente("María López", 25, "0991234567", True)
cliente2 = Cliente("Carlos Pérez", 31, "0987654321", False)

# Agregar productos
restaurante.agregar_producto(producto1)
restaurante.agregar_producto(producto2)

# Agregar clientes
restaurante.agregar_cliente(cliente1)
restaurante.agregar_cliente(cliente2)

# Mostrar información
restaurante.mostrar_productos()
restaurante.mostrar_clientes()
