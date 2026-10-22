"""Interfaz de consola para el catálogo de la Biblioteca PUCE."""
from modelos import Bibliotecario, LibroImpreso, RecursoDigital, SeccionBiblioteca


def inicializar_sistema():
    seccion = SeccionBiblioteca("Ciencias Exactas e Ingeniería")
    seccion.asignar_bibliotecario(Bibliotecario("Ana Paredes"))

    libro = LibroImpreso("LIB-01", "Estructuras de Datos en Python", "Mark Weiss", 2020, "978-013409")
    libro.registrar_copia("Estantería Central - Piso 2")
    digital = RecursoDigital("TES-01", "Minería de Texto en Repositorios PUCE", "Carlos Mora", 2024, "PDF", "https://repositorio.puce.edu.ec/handle/22000/123")
    digital.registrar_copia(digital.url)
    seccion.agregar_recurso(libro)
    seccion.agregar_recurso(digital)
    return seccion


def registrar_libro(seccion):
    try:
        libro = LibroImpreso(
            input("Código: "), input("Título: "), input("Autor: "),
            int(input("Año (1500-2026): ")), input("ISBN: ")
        )
        ubicacion = input("Ubicación física: ")
        libro.registrar_copia(ubicacion)
        seccion.agregar_recurso(libro)
        print("Libro impreso registrado.")
    except ValueError as error:
        print(f"No se pudo registrar: {error}")


def registrar_digital(seccion):
    try:
        digital = RecursoDigital(
            input("Código: "), input("Título: "), input("Autor: "),
            int(input("Año (1500-2026): ")), input("Formato: "), input("Enlace URL: ")
        )
        if digital.url:
            digital.registrar_copia(digital.url)
        seccion.agregar_recurso(digital)
        print("Recurso digital registrado.")
    except ValueError as error:
        print(f"No se pudo registrar: {error}")


def main():
    seccion = inicializar_sistema()
    while True:
        print("\n=== Catálogo Biblioteca PUCE ===")
        print("1. Ver catálogo completo")
        print("2. Registrar nuevo Libro Impreso")
        print("3. Registrar nuevo Recurso Digital")
        print("0. Salir")
        opcion = input("Selecciona una opción: ").strip()
        if opcion == "1":
            seccion.mostrar_catalogo_polimorfico()
        elif opcion == "2":
            registrar_libro(seccion)
        elif opcion == "3":
            registrar_digital(seccion)
        elif opcion == "0":
            print("Hasta pronto.")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")


if __name__ == "__main__":
    main()
    
