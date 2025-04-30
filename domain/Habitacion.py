class Habitacion:
    def __init__(self, id, numero, tipo, precio):
        self.id = id
        self.numero = numero
        self.tipo = tipo
        self.precio = precio

    def __str__(self):
        return f"Habitación(ID={self.id}, Número={self.numero}, Tipo={self.tipo}, Precio={self.precio})"