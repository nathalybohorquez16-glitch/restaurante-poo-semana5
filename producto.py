# Clase que representa un producto del restaurante

class Producto:
    def __init__(self, nombre: str, precio: float, cantidad: int, disponible: bool):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        self.disponible = disponible

    def __str__(self):
        estado = "Disponible" if self.disponible else "No disponible"
        return f"Producto: {self.nombre} | Precio: ${self.precio:.2f} | Cantidad: {self.cantidad} | {estado}"
