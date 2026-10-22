"SeccionBiblioteca reune los recursos que se crearon fuera de la sección."

class SeccionBiblioteca:
    #Reúne recursos que fueron creados fuera de la sección.

    def __init__(self, nombre):
        self.nombre = nombre
        self._recursos = []
        self._bibliotecario = None

    def asignar_bibliotecario(self, bibliotecario):
        # Es Asociación pues los dos objetos existen por separado.
        self._bibliotecario = bibliotecario

    @property
    def bibliotecario(self):
        return self._bibliotecario

    def agregar_recurso(self, recurso):
        # Es Agregación pues recibimos un objeto de Recurso ya creado.
        self._recursos.append(recurso)

    def total_recursos(self):
        return len(self._recursos)

    def mostrar_estado(self):
        print("Sección Biblioteca PUCE:", self.nombre)
        if self._bibliotecario is not None:
            print("Catalogador a cargo:", self._bibliotecario.nombre)

        for recurso in self._recursos:
            registro = recurso.ultimo_registro()
            if registro is None:
                print("-", recurso.titulo, f"({recurso.soporte}) sin registros")
            else:
                print("-", recurso.titulo, f"({recurso.soporte}) ->", registro.descripcion())

    def mostrar_catalogo_polimorfico(self):
        print("Sección Biblioteca PUCE:", self.nombre)
        if self._bibliotecario is not None:
            print("Catalogador a cargo:", self._bibliotecario.nombre)
        for recurso in self._recursos:
            print("-", recurso.obtener_detalle())
