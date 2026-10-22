"""Registro de ubicación y disponibilidad de una copia de un recurso."""


class RegistroAcceso:

    def __init__(self, ubicacion, disponible=True):
        if not isinstance(ubicacion, str) or not ubicacion.strip():
            raise ValueError("La ubicación no puede estar vacía.")

        self.ubicacion = ubicacion.strip()
        self.disponible = disponible

    def descripcion(self):
        if self.disponible:
            estado = "Disponible"
        else:
            estado = "Prestado / No disponible"

        return f"[{estado}] Ubicación/Acceso: {self.ubicacion}"
