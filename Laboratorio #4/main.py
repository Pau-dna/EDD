from listas import DoubleList, SimpleList, SimpleNode, DoubleNode
from usuario import Usuario
from fecha import Fecha
from agenda import Agenda
from direccion import Direccion

predefinidos = [
    "Carlos - 123 - 16/7/2005 - Medellin - 123456789 - miamor@unal - Calle 6, Cra 6, Barrio 3, Ciudad 1, Edificio 1, Apto 100",
    "Alejandra - 201 - 16/7/2005 - Ibague - 987654321 - miaumiau@unal - Calle 5, Cra 5, Barrio 1, Ciudad 1, Edificio 2, Apto 201",
    "Sebas - 302 - 16/7/2005 - Espinal - 12349876 - sebas@unal - Calle 4, Cra 4, Barrio 1, Ciudad 1, Edificio 3, Apto 302",
    "Horus - 403 - 16/7/2005 - Amazonas - 98712340 - horus@unal - Calle 3, Cra 3, Barrio 1, Ciudad 1, Edificio 4, Apto 403",
    "Artemis - 504 - 16/7/2005 - Bogota - 19283745 - artemis@unal - Calle 2, Cra 2, Barrio 1, Ciudad 1, Edificio 5, Apto 504",
]

def crearUsuarioDesdeTexto(informacion: str):
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

def crearFechaDesdeTexto(fecha: str):
    datosFecha = fecha.split('/')
    return Fecha(int(datosFecha[0]), int(datosFecha[1]), int(datosFecha[2]))

def crearDireccionDesdeTexto(direccion: str):
    datosDireccion = direccion.split(', ')
    return Direccion(datosDireccion[0], datosDireccion[1], datosDireccion[2], datosDireccion[3], datosDireccion[4], datosDireccion[5])

def crearUsuarioDesdeEntradas():
    usuario = Usuario(
        input('Ingrese su nombre: '),
        input('Ingrese su id: ')
    )
    usuario.setCiudad_nacimiento(
        input('Ingrese su ciudad de nacimiento: ')
    )
    usuario.setTel(
        input('Ingrese su numero detelefono: ')
    )
    usuario.setEmail(input('Ingrese su correo electronico: '))  

    fecha = Fecha(
        int(input('Ingrese el dia de su fecha de nacimiento: ')),
        int(input('Ingrese el mes de su fecha de nacimiento: ')),
        int(input('Ingrese el año de su fecha de nacimiento: '))
    )

    direccion = Direccion()

    print("Informacion de direccion:")
    direccion.setCalle(
        input('Ingrese la calle de su direccion: ')
    )
    direccion.setNomenclatura(
        input('Ingrese la nomenclatura de su direccion: ')
    )
    direccion.setBarrio(
        input('Ingrese el barrio de su direccion: ')
    )
    direccion.setCiudad(
        input('Ingrese la ciudad de su direccion: ')
    )
    direccion.setEdificio(
        input('Ingrese el edificio de su direccion: ')
    )
    direccion.setApto(
        input('Ingrese el apartamento de su direccion: ')
    )

    usuario.setFecha_nacimiento(fecha)
    usuario.setDir(direccion)
    return usuario

def problema_a():
    lista_simple = SimpleList()
    for i in range(2, 21, 2):
        lista_simple.addLast((i))
    print("Lista Simple con números pares del 1 al 20:")
    lista_simple.printData()
    
    lista_simple.removeFirst() # Elimina el 2
    lista_simple.removeLast() # Elimina el 20
    
    anterior = lista_simple.first()
    while anterior.getNext().getData() != 10:
        anterior = anterior.getNext()
    
    # Remover el 10
    objetivo = anterior.getNext()
    anterior.setNext(objetivo.getNext())
    print("Lista Simple después de eliminar 1, 10 y 20:")
    lista_simple.printData()

    lista_doble = DoubleList()
    for i in range(2, 21, 2):
        lista_doble.addLast((i))
    print("Lista Doble con números pares del 1 al 20:")
    lista_doble.printData()
    
    lista_doble.removeFirst()
    lista_doble.removeLast()
    siguiente = lista_doble.first()
    while siguiente != None:
        if siguiente.getData() == 10:
            lista_doble.remove(siguiente) # Remover el 10
            break
        siguiente = siguiente.getNext()

    print("Lista Doble después de eliminar 1, 10 y 20:")
    lista_doble.printData()

def problema_b():
    listaSimple = SimpleList()
    listaSimple.addFirst(crearUsuarioDesdeTexto(predefinidos[0]))
    
    for userString in predefinidos[1:]:
        user = crearUsuarioDesdeTexto(userString)
        listaSimple.addLast(user)

    listaSimple.printData()

    listaSimple.addFirst(
        crearUsuarioDesdeEntradas()
    )
    listaSimple.addLast(
        crearUsuarioDesdeEntradas()
    )

    listaSimple.printData()

    print("\n\n\nImplementacion con lista doble...\n\n\n")
    listaDoble = DoubleList()
    listaDoble.addFirst(crearUsuarioDesdeTexto(predefinidos[0]))
    
    for userString in predefinidos[1:]:
        user = crearUsuarioDesdeTexto(userString)
        listaDoble.addLast(user)

    listaDoble.printData()

    listaDoble.addFirst(
        crearUsuarioDesdeEntradas()
    )
    listaDoble.addLast(
        crearUsuarioDesdeEntradas()
    )

    listaDoble.printData()
    
    print("\n\nAgregar usuario en la tercera posicion\n\n")

    usuario = crearUsuarioDesdeEntradas()

    node = listaDoble.first()
    for x in range(2):
        node = node.getNext()
    
    listaDoble.addAfter(node, usuario)

    listaDoble.printData()
    

def main():
    problema_a()
    problema_b()

if __name__ == "__main__":
    main()
