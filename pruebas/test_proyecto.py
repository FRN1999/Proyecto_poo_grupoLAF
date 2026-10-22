from modelos import Bibliotecario, LibroImpreso, RecursoDigital, SeccionBiblioteca


def ejecutar_pruebas():
    libro = LibroImpreso("LIB-01", "Estructuras de Datos", "Mark Weiss", 2020, "978-013409")
    assert libro.codigo == "LIB-01" and libro.titulo == "Estructuras de Datos"
    assert libro.autor == "Mark Weiss" and libro.anio == 2020 and libro.soporte == "Físico"
    assert libro.isbn == "978-013409"

#Probamos con un año invalido, comprueba que "1499" sea Falso y al ser falso pasa
    try:
        LibroImpreso("LIB-X", "Año inválido", "Autor", 1499, "ISBN-X")
        assert False, "Se esperaba ValueError para el año inválido"
    except ValueError:
        pass

# registramos la ubicación para comprobar la composición, revisa que el ultimo registro no esté vacío y revisa el dato correcto guardado "Estanteria General"
    libro.registrar_copia("Estantería central - Piso 2", True)
    assert libro.ultimo_registro() is not None
    assert "Estantería central" in libro.ultimo_registro().ubicacion

#Creamos una sección y un bibliotecario, el nombre y todo lo necesario de RecursoDigital para comporbar asociación
    digital = RecursoDigital("DIG-01", "Tesis PUCE", "Ana Pérez", 2024, "PDF", "https://repositorio.puce.edu.ec/tesis")
    seccion = SeccionBiblioteca("Ciencias Exactas")
    bibliotecario = Bibliotecario("Ana Paredes")
    seccion.asignar_bibliotecario(bibliotecario)
    seccion.agregar_recurso(libro)
    seccion.agregar_recurso(digital)
    #Comporbación de la asociación
    assert seccion.bibliotecario is bibliotecario
    assert seccion.total_recursos() == 2

    detalle_libro = libro.obtener_detalle()
    detalle_digital = digital.obtener_detalle()
    assert "ISBN" in detalle_libro and "Libro impreso" in detalle_libro
    assert "Formato: PDF" in detalle_digital and "https://repositorio.puce.edu.ec/tesis" in detalle_digital
    assert detalle_libro != detalle_digital
    print("Todas las pruebas se ejecutaron correctamente.")


if __name__ == "__main__":
    ejecutar_pruebas()
