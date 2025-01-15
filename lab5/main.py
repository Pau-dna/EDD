import random
from listas import DoubleList, SimpleList, SimpleNode, DoubleNode
from usuario import Usuario
from fecha import Fecha
from direccion import Direccion


class Ordenador:
    def __init__(self, capacity):
        self.lista = [0] * capacity
        self.limit = capacity

    def inicializar(self):
        self.lista = [random.randint(0, 100) for _ in range(self.limit)]

    def ordenar_burbuja(self):
        for i in range(self.limit):
            for j in range(0, self.limit - i - 1):
                if self.lista[j] > self.lista[j + 1]:
                    self.lista[j], self.lista[j + 1] = self.lista[j + 1], self.lista[j]

    def ordenar_seleccion(self):
        for i in range(self.limit):
            indexMinimo = i
            for j in range(i + 1, self.limit):
                if self.lista[j] < self.lista[indexMinimo]:
                    indexMinimo = j
            self.lista[i], self.lista[indexMinimo] = self.lista[indexMinimo], self.lista[i]

    def ordenar_insercion(self):
        for i in range(1, self.limit):
            key = self.lista[i]
            j = i - 1
            while j >= 0 and key < self.lista[j]:
                self.lista[j + 1] = self.lista[j]
                j -= 1
            self.lista[j + 1] = key

    def ordenar_mergeSort(self):
        self.lista = self.mergeSort(self.lista)

    def mergeSort(self, array):
        if len(array) > 1:
            mid = len(array) // 2
            L = array[:mid]
            R = array[mid:]

            self.mergeSort(L)
            self.mergeSort(R)

            i = j = k = 0

            while i < len(L) and j < len(R):
                if L[i] < R[j]:
                    array[k] = L[i]
                    i += 1
                else:
                    array[k] = R[j]
                    j += 1
                k += 1

            while i < len(L):
                array[k] = L[i]
                i += 1
                k += 1

            while j < len(R):
                array[k] = R[j]
                j += 1
                k += 1

        return array

    def mostrar(self):
        print(self.lista)

    def busqueda_binaria(self, valor):
        low = 0
        high = self.limit - 1
        while low <= high:
            mid = (low + high) // 2
            if self.lista[mid] == valor:
                return mid
            elif self.lista[mid] < valor:
                low = mid + 1
            else:
                high = mid - 1
        return -1

predefinidos = [
    "Carlos - 564 - 16/7/2005 - Medellin - 123456789 - miamor@unal - Calle 6, Cra 6, Barrio 3, Ciudad 1, Edificio 1, Apto 100",
    "Alejandra - 201 - 16/7/2005 - Ibague - 987654321 - miaumiau@unal - Calle 5, Cra 5, Barrio 1, Ciudad 1, Edificio 2, Apto 201",
    "Sebas - 702 - 16/7/2005 - Espinal - 12349876 - sebas@unal - Calle 4, Cra 4, Barrio 1, Ciudad 1, Edificio 3, Apto 302",
    "Horus - 403 - 16/7/2005 - Amazonas - 98712340 - horus@unal - Calle 3, Cra 3, Barrio 1, Ciudad 1, Edificio 4, Apto 403",
    "Artemis - 504 - 16/7/2005 - Bogota - 19283745 - artemis@unal - Calle 2, Cra 2, Barrio 1, Ciudad 1, Edificio 5, Apto 504",
    "Sora - 804 - 16/7/2005 - Bello - 52342 - soraaa@unal - Calle 2, Cra 2, Barrio 1, Ciudad 1, Edificio 5, Apto 504",
]

def crearUsuarioDesdeTexto(informacion):
    datosUsuario = informacion.split(' - ')
    fecha = crearFechaDesdeTexto(datosUsuario[2])
    direccion = crearDireccionDesdeTexto(datosUsuario[6])
    
    usuario = Usuario(datosUsuario[0], int(datosUsuario[1]))
    usuario.setFecha_nacimiento(fecha)
    usuario.setCiudad_nacimiento(datosUsuario[3])
    usuario.setTel(datosUsuario[4])
    usuario.setEmail(datosUsuario[5])
    usuario.setDir(direccion)
    return usuario

def crearFechaDesdeTexto(fecha):
    datosFecha = fecha.split('/')
    return Fecha(int(datosFecha[0]), int(datosFecha[1]), int(datosFecha[2]))

def crearDireccionDesdeTexto(direccion):
    datosDireccion = direccion.split(', ')
    return Direccion(datosDireccion[0], datosDireccion[1], datosDireccion[2], datosDireccion[3], datosDireccion[4], datosDireccion[5])

class OrdenadorLista:
    
    def __init__(self):
        self.lista = []
    
    def inicializar(self, n):
        self.lista = [random.randint(0, 100) for _ in range(n)]

    def ordenar(self):
        n = len(self.lista)
        for i in range(n):
            for j in range(0, n - i - 1):
                if self.lista[j] > self.lista[j + 1]:
                    self.lista[j], self.lista[j + 1] = self.lista[j + 1], self.lista[j]

    def mostrar(self):
        for item in self.lista:
            print(item, end=' ')
        print()

class OrdenadorAgenda:
    def __init__(self):
        self.lista = DoubleList()
    
    def agregarUsuario(self, usuario):
        self.lista.addLast(usuario)
    
    def ordenar(self):
        end = None
        while end != self.lista.first():
            nodo = self.lista.first()
            while nodo.getNext() != end:
                siguiente = nodo.getNext()
                if nodo.data.id > siguiente.data.id:
                    nodo.data, siguiente.data = siguiente.data, nodo.data
                nodo = nodo.getNext()
            end = nodo
            
    def mostrar(self):
        current = self.lista.first()
        while current:
            u = current.data
            print(f"Cedula: {u.id}, Nombre: {u.nombre}, Apellido: {u.fecha_nacimiento}, Edad: {u.email}")
            current = current.getNext()

def test_ordenador():
    ordenador = Ordenador(10)
    ordenador.inicializar()
    print("Arreglo inicial:")
    ordenador.mostrar()
    ordenador.ordenar_burbuja()
    print("Arreglo ordenado por burbuja:")
    ordenador.mostrar()
    
    ordenador.inicializar()
    print("Arreglo inicial:")
    ordenador.mostrar()
    ordenador.ordenar_seleccion()
    print("Arreglo ordenado por selección:")
    ordenador.mostrar()
    
    ordenador.inicializar()
    print("Arreglo inicial:")
    ordenador.mostrar()
    ordenador.ordenar_insercion()
    print("Arreglo ordenado por inserción:")
    ordenador.mostrar()
    
    ordenador.inicializar()
    print("Arreglo inicial:")
    ordenador.mostrar()
    ordenador.ordenar_mergeSort()
    print("Arreglo ordenado por merge sort:")
    ordenador.mostrar() 
    
    index = int(input(("Ingrese el índice a buscar: ")))
    valor = ordenador.lista[index]  # Tomar un valor del arreglo para la búsqueda binaria
    index = ordenador.busqueda_binaria(valor)
    print(f"Valor {valor} encontrado en el índice {index}")

def test_ordenador_lista():
    ordenador = OrdenadorLista()
    ordenador.inicializar(12)
    print("Lista inicial:")
    ordenador.mostrar()
    ordenador.ordenar()
    print("Lista ordenada:")
    ordenador.mostrar()

def test_OrdenadorAgenda():
    ordenador = OrdenadorAgenda()
    for info in predefinidos:
        usuario = crearUsuarioDesdeTexto(info)
        ordenador.agregarUsuario(usuario)
    print("Agenda inicial:")
    ordenador.mostrar()
    ordenador.ordenar()
    print("Agenda ordenada:")
    ordenador.mostrar()

if __name__ == "__main__":
    test_ordenador()
    test_ordenador_lista()
    test_OrdenadorAgenda()