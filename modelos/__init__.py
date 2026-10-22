"""Clases fundamentales del sistema de catalogación de Biblioteca PUCE."""

from .registro_acceso import RegistroAcceso
from .recurso import Recurso
from .libro_impreso import LibroImpreso
from .recurso_digital import RecursoDigital
from .bibliotecario import Bibliotecario
from .seccion_biblioteca import SeccionBiblioteca

__all__ = ["RegistroAcceso", "Recurso", "LibroImpreso", "RecursoDigital", "Bibliotecario", "SeccionBiblioteca"]





