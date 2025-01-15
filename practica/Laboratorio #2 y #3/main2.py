from direccion import *
from fecha import *
from usuario import *
from agenda import*
class Main:
  
    if __name__ == "__main__":
        
    
        # Crear instancias de usuarios con datos específicos
        usuario1 = Usuario("Juan", 1, Fecha(1, 1, 2000), "Medellín", 1234567890, "juan@example.com", 
                        Direccion("Calle 10", "A", "Centro", "Medellín", "Edificio Alfa", "101"))
        usuario2 = Usuario("Ana", 2, Fecha(15, 5, 1995), "Bogotá", 2345678901, "ana@example.com", 
                        Direccion("Carrera 5", "B", "Chapinero", "Bogotá", "Edificio Beta", "202"))
        usuario3 = Usuario("Luis", 3, Fecha(10, 8, 1990), "Cali", 3456789012, "luis@example.com", 
                        Direccion("Avenida 20", "C", "Norte", "Cali", "Edificio Gamma", "303"))
        usuario4 = Usuario("Sofía", 4, Fecha(22, 3, 1988), "Barranquilla", 4567890123, "sofia@example.com", 
                        Direccion("Calle 30", "D", "Sur", "Barranquilla", "Edificio Delta", "404"))
        usuario5 = Usuario("Carlos", 5, Fecha(5, 12, 1992), "Cartagena", 5678901234, "carlos@example.com", 
                        Direccion("Carrera 50", "E", "Centro Histórico", "Cartagena", "Edificio Epsilon", "505"))

        # Inicializar la agenda
        agenda = Agenda(5)
        agenda.agregar(usuario1)
        agenda.agregar(usuario2)
        agenda.agregar(usuario3)
        agenda.agregar(usuario4)
        agenda.agregar(usuario5)

        # Buscar usuario por ID
        id_buscar = 3
        posicion = agenda.buscar(id_buscar)
        if posicion != -1:
            print(f"Usuario con ID {id_buscar} encontrado en posición {posicion}.")
        else:
            print(f"Usuario con ID {id_buscar} no encontrado.")

        # Exportar la agenda a archivo
        agenda.to_file("Agenda.txt")
        
         # Inicializar la agenda desde un archivo
        agenda = Agenda(5)
        agenda.import_from_file("Agenda.txt")

        # Mostrar todos los usuarios con toString
        print("Usuarios importados:")
        for usuario in agenda.getRegistro:
            if usuario:
                print(usuario)

        # Eliminar un usuario por ID
        id_eliminar = 3
        posicion = agenda.buscar(id_eliminar)
        if posicion != -1:
            eliminado = agenda.eliminar(posicion)
            print(f"Usuario eliminado: {eliminado}")
        else:
            print(f"Usuario con ID {id_eliminar} no encontrado.")

    # Exportar la agenda actualizada a un nuevo archivo
        agenda.to_file("Agenda2.txt")

   