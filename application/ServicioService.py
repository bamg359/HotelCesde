# servicios.py

class Servicio:
    def __init__(self, nombre, descripcion, disponible=True):
        self.nombre = nombre
        self.descripcion = descripcion
        self.disponible = disponible

    def __str__(self):
        estado = "Disponible" if self.disponible else "No disponible"
        return f"{self.nombre} - {self.descripcion} ({estado})"


class Hotel:
    def __init__(self, nombre):
        self.nombre = nombre
        self.servicios = self._cargar_servicios()

    def _cargar_servicios(self):
        # Lista fija de servicios disponibles en el hotel
        return [
            Servicio("Restaurante", "Comidas y bebidas gourmet disponibles todo el día."),
            Servicio("Gimnasio", "Equipado con máquinas modernas para cardio y fuerza."),
            Servicio("Spa", "Relájate con nuestros masajes y tratamientos faciales."),
            Servicio("Piscina", "Piscina climatizada al aire libre."),
            Servicio("Wi-Fi", "Internet de alta velocidad en todo el hotel."),
            Servicio("Transporte al aeropuerto", "Servicio gratuito al aeropuerto las 24 horas.")
        ]

    def mostrar_servicios(self):
        print(f"\n--- Servicios disponibles en {self.nombre} ---")
        for idx, servicio in enumerate(self.servicios, 1):
            print(f"{idx}. {servicio}")

    def buscar_servicio(self, nombre_servicio):
        for servicio in self.servicios:
            if servicio.nombre.lower() == nombre_servicio.lower():
                return servicio
        return None


# Interfaz de cliente
def menu_cliente(hotel):
    while True:
        print("\n--- Menú de Cliente ---")
        print("1. Ver todos los servicios")
        print("2. Buscar un servicio por nombre")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            hotel.mostrar_servicios()
        elif opcion == "2":
            nombre = input("Ingrese el nombre del servicio a buscar: ")
            servicio = hotel.buscar_servicio(nombre)
            if servicio:
                print(f"\nServicio encontrado:\n{servicio}")
            else:
                print("Servicio no encontrado.")
        elif opcion == "3":
            print("Gracias por visitar el Hotel CESDE.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")