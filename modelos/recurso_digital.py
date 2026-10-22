"Recurso de libros digitales es la clase que hereda de Recurso y añade el tipo de formato digital."

from .recurso import Recurso

class RecursoDigital(Recurso):
    #Herencia: RecursoDigital es un tipo de Recurso con soporte Digital.

    def __init__(self, codigo, titulo, autor, anio, formato, url=""):
        super().__init__(codigo, titulo, autor, anio, "Digital")
        if not isinstance(formato, str) or not formato.strip():
            raise ValueError("El formato no puede estar vacío.")
        if not isinstance(url, str):
            raise ValueError("El enlace URL debe ser texto.")
        self.formato = formato.strip()
        self.url = url.strip()

    def obtener_detalle(self):
        enlace = self.url
        if not enlace and self.ultimo_registro() is not None:
            enlace = self.ultimo_registro().ubicacion
        if not enlace:
            enlace = "Sin enlace registrado"
        return f"Recurso digital: {super().obtener_detalle()} | Formato: {self.formato} | Enlace URL: {enlace}"
