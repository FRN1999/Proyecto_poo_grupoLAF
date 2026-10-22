"Clase derivada de Recurso el cual describe un libro impreso de manera fisica y con ISBN unico"


from .recurso import Recurso

class LibroImpreso(Recurso):
    # Herencia: Aquí LibroImpreso se refiere Recurso con soporte Físico.

    def __init__(self, codigo, titulo, autor, anio, isbn):
        # La clase base inicializa código, título, autor, año, soporte y registros.
        super().__init__(codigo, titulo, autor, anio, "Físico")
        if not isinstance(isbn, str) or not isbn.strip():
            raise ValueError("El ISBN no puede estar vacío.")
        self.isbn = isbn.strip()

    def obtener_detalle(self):
        detalle = f"Libro impreso: {super().obtener_detalle()} | ISBN: {self.isbn}"
        registro = self.ultimo_registro()
        if registro is not None:
            detalle += f" | Último registro físico: {registro.descripcion()}"
        return detalle
    
