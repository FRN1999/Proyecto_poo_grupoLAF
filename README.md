# Catálogo de recursos de la Biblioteca PUCE

## Integrantes

- Luciana Aldás
- Francisco Narváez
- Anahí Real

## Problema

El registro manual de materiales bibliográficos heterogéneos, como libros impresos y tesis digitales, puede tomar tiempo y causar errores al catalogar los recursos o anotar sus ubicaciones y enlaces de acceso.

## Usuario

El sistema está dirigido al personal de catalogación, bibliotecarios y administradores del repositorio documental de la Biblioteca PUCE.

## Objetivo

Desarrollar una aplicación de consola en Python que permita organizar, consultar y registrar libros impresos y recursos digitales mediante los fundamentos de Programación Orientada a Objetos.

## Alcance

Esta versión final evoluciona la primera entrega monolítica: separa las clases en módulos, incorpora validaciones, fichas específicas para recursos físicos y digitales, un menú interactivo, pruebas con `assert` y un diagrama UML actualizado. Los datos se mantienen en memoria mientras el programa está abierto; no se utiliza una base de datos.

## Funcionalidades implementadas

- Mostrar el catálogo de una sección de biblioteca.
- Registrar libros impresos con código, título, autor, año, ISBN y ubicación física.
- Registrar recursos digitales con código, título, autor, año, formato y enlace URL.
- Validar campos de texto requeridos y que el año sea un entero entre 1500 y 2026.
- Mostrar la ubicación física del libro y su disponibilidad; en los recursos digitales se muestra el formato y el enlace.
- Asociar un bibliotecario a una sección.
- Consultar el total de recursos de una sección desde sus métodos.

## Clases y responsabilidades

Las clases se encuentran en `modelos/`:

- **`RegistroAcceso`** (`registro_acceso.py`): conserva la ubicación o enlace y la disponibilidad de una copia.
- **`Recurso`** (`recurso.py`): almacena los datos comunes, valida sus valores y administra los registros de acceso.
- **`LibroImpreso`** (`libro_impreso.py`): especializa `Recurso` para libros físicos e incluye el ISBN.
- **`RecursoDigital`** (`recurso_digital.py`): especializa `Recurso` para materiales digitales e incluye el formato y el enlace URL.
- **`Bibliotecario`** (`bibliotecario.py`): representa al bibliotecario asociado con una sección.
- **`SeccionBiblioteca`** (`seccion_biblioteca.py`): reúne recursos, mantiene al bibliotecario asociado y presenta el catálogo.

## Conceptos de Programación Orientada a Objetos

- **Encapsulación y validación:** `Recurso` guarda sus datos comunes en atributos protegidos (`_codigo`, `_titulo`, `_autor`, `_anio`, `_soporte`) y ofrece propiedades de lectura. Su constructor valida los textos y el año.
- **Herencia y `super()`:** `LibroImpreso` y `RecursoDigital` heredan de `Recurso` y reutilizan su inicialización común mediante `super().__init__()`.
- **Sobrescritura y polimorfismo:** ambas subclases sobrescriben `obtener_detalle()`. `SeccionBiblioteca.mostrar_catalogo_polimorfico()` recorre los recursos y llama a `obtener_detalle()` sin tener que distinguir sus clases.
- **Composición:** `Recurso` crea y administra sus propios objetos `RegistroAcceso` mediante `registrar_copia()`.
- **Agregación:** `SeccionBiblioteca` contiene una lista de recursos que recibe ya creados mediante `agregar_recurso()`.
- **Asociación:** `SeccionBiblioteca` mantiene una referencia al `Bibliotecario` asignado mediante `asignar_bibliotecario()`.

El diagrama editable está en `diagrama_final.mmd` y su versión visible está en `diagrama_final.pdf`.
La guía secuencial para explicar el código y los conceptos de POO está en `GUIA_EXPLICACION_CODIGO.pdf`.

## Estructura del proyecto

```text
main.py
README.md
diagrama_final.mmd
diagrama_final.pdf
GUIA_EXPLICACION_CODIGO.pdf
modelos/
  __init__.py
  registro_acceso.py
  recurso.py
  libro_impreso.py
  recurso_digital.py
  bibliotecario.py
  seccion_biblioteca.py
pruebas/
  __init__.py
  test_proyecto.py
```

## Ejecución

Desde la carpeta raíz del proyecto, inicia el menú con:

```bash
python main.py
```

Ejecuta las pruebas con:

```bash
python -m pruebas.test_proyecto
```

Si tu instalación usa el comando `python3`, puedes ejecutar `python3 main.py` y `python3 -m pruebas.test_proyecto`.
