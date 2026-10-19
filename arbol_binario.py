# -*- coding: utf-8 -*-
"""
MI ARBOL BINARIO
----------------
Programa que permite ingresar una serie de elementos para almacenarlos en un
arbol binario de busqueda (ABB) y realizar los recorridos en inorder,
preorder y posorder. Adicionalmente permite buscar y eliminar elementos,
visualizar la estructura del arbol y consultar estadisticas basicas.

Autor:     [Nombre completo del estudiante]
Curso:     [Nombre del curso]
Actividad: MA Evaluacion 8 - Reporte academico "Mi arbol binario"
Fecha:     [Fecha de entrega]
"""


class Nodo:
    """Nodo de un arbol binario: guarda el dato y las referencias a sus
    hijos izquierdo y derecho."""

    def __init__(self, dato):
        self.dato = dato
        self.izquierdo = None
        self.derecho = None


class ArbolBinarioBusqueda:
    """Arbol binario de busqueda.

    Invariante: para cada nodo, todos los datos del subarbol izquierdo son
    menores que el dato del nodo y todos los datos del subarbol derecho son
    mayores.
    """

    def __init__(self):
        self.raiz = None

    # ------------------------- INSERCION ------------------------------ #
    def insertar(self, dato):
        """Inserta un dato en el arbol manteniendo el orden del ABB."""
        if self.raiz is None:
            self.raiz = Nodo(dato)
        else:
            self._insertar(dato, self.raiz)

    def _insertar(self, dato, actual):
        """Metodo recursivo de apoyo: baja por el arbol hasta encontrar la
        posicion vacia donde el nuevo dato debe alojarse."""
        if dato < actual.dato:
            if actual.izquierdo is None:
                actual.izquierdo = Nodo(dato)
            else:
                self._insertar(dato, actual.izquierdo)
        elif dato > actual.dato:
            if actual.derecho is None:
                actual.derecho = Nodo(dato)
            else:
                self._insertar(dato, actual.derecho)
        # Si el dato ya existe no se inserta (el arbol no admite duplicados).

    # ------------------------- RECORRIDOS ----------------------------- #
    def recorrido_inorder(self):
        """Visita: subarbol izquierdo - raiz - subarbol derecho."""
        valores = []
        self._inorder(self.raiz, valores)
        return valores

    def _inorder(self, actual, valores):
        if actual is not None:
            self._inorder(actual.izquierdo, valores)
            valores.append(actual.dato)
            self._inorder(actual.derecho, valores)

    def recorrido_preorder(self):
        """Visita: raiz - subarbol izquierdo - subarbol derecho."""
        valores = []
        self._preorder(self.raiz, valores)
        return valores

    def _preorder(self, actual, valores):
        if actual is not None:
            valores.append(actual.dato)
            self._preorder(actual.izquierdo, valores)
            self._preorder(actual.derecho, valores)

    def recorrido_posorder(self):
        """Visita: subarbol izquierdo - subarbol derecho - raiz."""
        valores = []
        self._posorder(self.raiz, valores)
        return valores

    def _posorder(self, actual, valores):
        if actual is not None:
            self._posorder(actual.izquierdo, valores)
            self._posorder(actual.derecho, valores)
            valores.append(actual.dato)

    # ------------------------- ELIMINACION ---------------------------- #
    def eliminar(self, dato):
        """Elimina un dato del arbol. Devuelve True si la eliminacion tuvo
        exito o False si el dato no se encontro."""
        self.raiz, eliminado = self._eliminar(self.raiz, dato)
        return eliminado

    def _eliminar(self, actual, dato):
        if actual is None:
            return None, False
        if dato < actual.dato:
            actual.izquierdo, eliminado = self._eliminar(actual.izquierdo, dato)
        elif dato > actual.dato:
            actual.derecho, eliminado = self._eliminar(actual.derecho, dato)
        else:
            # Caso 1 y caso 2: el nodo es hoja o tiene un solo hijo.
            if actual.izquierdo is None:
                return actual.derecho, True
            if actual.derecho is None:
                return actual.izquierdo, True
            # Caso 3: el nodo tiene dos hijos. Se busca el sucesor inorder
            # (el dato menor del subarbol derecho), se copia en el nodo y
            # despues se elimina el sucesor del subarbol derecho.
            sucesor = self._minimo(actual.derecho)
            actual.dato = sucesor.dato
            actual.derecho, _ = self._eliminar(actual.derecho, sucesor.dato)
            eliminado = True
        return actual, eliminado

    def _minimo(self, actual):
        """Recorre hacia la izquierda hasta hallar el dato minimo."""
        while actual.izquierdo is not None:
            actual = actual.izquierdo
        return actual

    # ------------------------- EXTRAS --------------------------------- #
    def buscar(self, dato):
        """Devuelve True si el dato existe en el arbol."""
        actual = self.raiz
        while actual is not None:
            if dato == actual.dato:
                return True
            actual = actual.izquierdo if dato < actual.dato else actual.derecho
        return False

    def altura(self):
        """Altura del arbol medida en niveles (un nodo = 1 nivel)."""
        return self._altura(self.raiz)

    def _altura(self, actual):
        if actual is None:
            return 0
        return 1 + max(self._altura(actual.izquierdo), self._altura(actual.derecho))

    def total_nodos(self):
        return len(self.recorrido_inorder())

    def imprimir_estructura(self):
        """Muestra el arbol girado 90 grados: los niveles se dibujan de
        izquierda a derecha y la raiz queda mas a la izquierda."""
        if self.raiz is None:
            print("  (el arbol esta vacio)")
        else:
            self._imprimir(self.raiz, 0)

    def _imprimir(self, actual, nivel):
        if actual is not None:
            self._imprimir(actual.derecho, nivel + 1)
            print("    " * nivel + str(actual.dato))
            self._imprimir(actual.izquierdo, nivel + 1)


# ---------------------------------------------------------------------- #
# Interfaz de usuario (menu de consola)                                  #
# ---------------------------------------------------------------------- #

def imprimir_menu():
    print("\n" + "=" * 52)
    print("   MI ARBOL BINARIO - MENU PRINCIPAL")
    print("=" * 52)
    print(" 1. Insertar elemento")
    print(" 2. Eliminar elemento")
    print(" 3. Buscar elemento")
    print(" 4. Recorrido inorder   (izquierda - raiz - derecha)")
    print(" 5. Recorrido preorder  (raiz - izquierda - derecha)")
    print(" 6. Recorrido posorder  (izquierda - derecha - raiz)")
    print(" 7. Mostrar estructura del arbol")
    print(" 8. Informacion del arbol (nodos, altura)")
    print(" 9. Salir")
    print("-" * 52)


def pedir_entero(mensaje):
    """Solicita un numero entero y valida la entrada del usuario."""
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("  [!] Debe escribir un numero entero. Intente de nuevo.")


def main():
    arbol = ArbolBinarioBusqueda()
    while True:
        imprimir_menu()
        opcion = input("Seleccione una opcion: ").strip()
        if opcion == "1":
            dato = pedir_entero("Digite el numero a insertar: ")
            arbol.insertar(dato)
            print("  [OK] Elemento", dato, "insertado en el arbol.")
        elif opcion == "2":
            dato = pedir_entero("Digite el numero a eliminar: ")
            if arbol.eliminar(dato):
                print("  [OK] Elemento", dato, "eliminado del arbol.")
            else:
                print("  [!] El elemento", dato, "no existe en el arbol.")
        elif opcion == "3":
            dato = pedir_entero("Digite el numero a buscar: ")
            encontrado = arbol.buscar(dato)
            if encontrado:
                print("  [i] El elemento", dato, "SI existe en el arbol.")
            else:
                print("  [i] El elemento", dato, "NO existe en el arbol.")
        elif opcion == "4":
            print("  Recorrido inorder :", arbol.recorrido_inorder())
        elif opcion == "5":
            print("  Recorrido preorder:", arbol.recorrido_preorder())
        elif opcion == "6":
            print("  Recorrido posorder:", arbol.recorrido_posorder())
        elif opcion == "7":
            print("  Estructura del arbol (girada 90 grados, la raiz queda a la izquierda):")
            arbol.imprimir_estructura()
        elif opcion == "8":
            print("  Total de nodos:", arbol.total_nodos(),
                  "| Altura:", arbol.altura(), "niveles")
        elif opcion == "9":
            print("  Programa finalizado. Hasta pronto!")
            break
        else:
            print("  [!] Opcion no valida. Elija un numero entre 1 y 9.")


if __name__ == "__main__":
    main()
