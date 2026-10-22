"""Clase base de los recursos bibliográficos de Biblioteca PUCE"""

from .registro_acceso import RegistroAcceso

class Recurso:

    def __init__(self, codigo, titulo, autor, anio, soporte):
        if not codigo.strip() or not titulo.strip() or not autor.strip() or not soporte.strip():
            raise ValueError("Los datos del recurso no pueden estar vacíos.")

        if not isinstance(anio, int) or isinstance(anio, bool) or anio < 1500 or anio > 2026:
            raise ValueError("El año debe ser un número entero entre 1500 y 2026.")

        self._codigo = codigo
        self._titulo = titulo
        self._autor = autor
        self._anio = anio
        self._soporte = soporte

        self._registros = []

    @property
    def codigo(self):
        return self._codigo

    @property
    def titulo(self):
        return self._titulo

    @property
    def autor(self):
        return self._autor

    @property
    def anio(self):
        return self._anio

    @property
    def soporte(self):
        return self._soporte

    def registrar_copia(self, ubicacion, disponible=True):
        nuevo_registro = RegistroAcceso(ubicacion, disponible)
        self._registros.append(nuevo_registro)
        return nuevo_registro

    def ultimo_registro(self):
        if len(self._registros) == 0:
            return None

        return self._registros[-1]

    def obtener_detalle(self):
        return f"[{self._codigo}] {self._titulo} - {self._autor} ({self._anio}) | Soporte: {self._soporte}"

