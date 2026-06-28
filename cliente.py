# Clase que representa un cliente del restaurante

class Cliente:
    def __init__(self, nombre: str, edad: int, telefono: str, frecuente: bool):
        self.nombre = nombre
        self.edad = edad
        self.telefono = telefono
        self.frecuente = frecuente

    def __str__(self):
        tipo = "Cliente frecuente" if self.frecuente else "Cliente nuevo"
        return f"Cliente: {self.nombre} | Edad: {self.edad} | Teléfono: {self.telefono} | {tipo}"
