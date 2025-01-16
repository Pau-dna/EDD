from usuario import *
from fecha import *
from direccion import *
from listas import *
import sys

class EnumRoles:
    ADMINISTRADOR = "Administrador"
    INVESTIGADOR = "Investigador"

class ManejadorTxt():
    
    pathEmpleados = "Empleados.txt"
    pathPasswords = "Password.txt"
    
    def cargarempleados(self):
        empleados = DoubleList()
        passwords = self.cargarPasswords()
        
        archivo = open(ManejadorTxt.pathEmpleados, 'r')
        for renglon in archivo:
            datosEmpleado = renglon.strip().split(' ')
            cedula = datosEmpleado[1]
            password = self.obtener_password(passwords, cedula)
            tipo = self.obtener_tipo(passwords, cedula)
            
            fecha = Fecha(datosEmpleado[2], datosEmpleado[3], datosEmpleado[4])
            direccion = Direccion(datosEmpleado[8], datosEmpleado[9], datosEmpleado[10], datosEmpleado[11], datosEmpleado[12], datosEmpleado[13])
            empleado = Empleado(datosEmpleado[0], cedula, fecha, datosEmpleado[5], datosEmpleado[6], datosEmpleado[7], direccion, password, tipo)
            empleados.addLast(empleado)
            
        return empleados
            
    def cargarPasswords(self):
        archivo = open(ManejadorTxt.pathPasswords, 'r')
        passwords = DoubleList()
        for renglon in archivo:
            datosPassword = renglon.strip().split(' ')
            password = Password(datosPassword[0], datosPassword[1], datosPassword[2])
            passwords.addLast(password)
        return passwords

    def obtener_password(self, passwords, cedula):
        node = passwords._head
        while node != None:
            if node.getData().Id == cedula:
                return node.getData().password
            node = node.getNext()
        return None

    def obtener_tipo(self, passwords, cedula):
        node = passwords._head
        while node != None:
            if node.getData().Id == cedula:
                return node.getData().tipoEmpleado
            node = node.getNext()
        return None

    def guardar_empleados(self, empleados):
        archivo = open(ManejadorTxt.pathEmpleados, 'w')
        node = empleados._head
        while node != None:
            empleado = node.getData()
            line = f"{empleado.getNombre()} {empleado.getId()} {empleado.getFecha_nacimiento().get_Dia()} {empleado.getFecha_nacimiento().get_Mes()} {empleado.getFecha_nacimiento().get_A()} {empleado.getCiudad_nacimiento()} {empleado.getTel()} {empleado.getEmail()} {empleado.getDir().getCalle()} {empleado.getDir().getNomenclatura()} {empleado.getDir().getBarrio()} {empleado.getDir().getCiudad()} {empleado.getDir().getEdificio()} {empleado.getDir().getApto()}"
            archivo.write(f"{line}\n")
            node = node.getNext()
        archivo.close()

    def guardar_passwords(self, empleados):
        archivo = open(ManejadorTxt.pathPasswords, 'w')
        node = empleados._head
        while node != None:
            empleado = node.getData()
            line = f"{empleado.getId()} {empleado.password} {empleado.tipo}"
            archivo.write(f"{line}\n")
            node = node.getNext()
        archivo.close()
    
class Empleado(Usuario):
    def __init__(self, nombre, Id, fecha_nacimiento, ciudad_nacimiento, tel, email, dire, password, tipo):
        super().__init__(nombre, Id, fecha_nacimiento, ciudad_nacimiento, tel, email, dire)
        self.password = password
        self.tipo = tipo
        
    def setPassword(self, password):
        self.password = password
        
    def __str__(self): 
        return f"{self.getNombre()} {self.getId()} {self.password} {self.tipo}"
    pass

class Password():
    def __init__(self, Id, password, tipoEmpleado):
        self.Id = Id
        self.password = password
        self.tipoEmpleado = tipoEmpleado

class Investigador(Empleado):
    def consultarListaEquipo(self):
        pass
    def solicitarEquipo(self, nombre, num_placa, fecha_compra, valor_compra, empleado):
        nuevoEquipo = Equipo(nombre, num_placa, fecha_compra, valor_compra, empleado)
        pass
    def solicitarEliminacion(self):
        pass
    pass

class Administrador(Investigador):
    @classmethod
    def cambiar_password(cls, cedula, password):
        node = ManejadorTxt().empleados._head
        while node != None:
            if node.getData().getId == cedula:
                node.getData().setPassword(password)
            node = node.getNext()
        ManejadorTxt.guardar_passwords("C:/Users/andre/Documents/GitHub/EDD/practica/Password.txt")
    
    @classmethod
    def agregar_usuario(cls, nombre, Id, fecha_nacimiento, ciudad_nacimiento, tel, email, dire, password, tipo):
        empleado = Empleado(nombre, Id, fecha_nacimiento, ciudad_nacimiento, tel, email, dire, password, tipo)
        ManejadorTxt().empleados.addLast(empleado)
        ManejadorTxt.guardar_empleados("C:/Users/andre/Documents/GitHub/EDD/practica/Empleados.txt")
        ManejadorTxt.guardar_passwords("C:/Users/andre/Documents/GitHub/EDD/practica/Password.txt")
        pass
    
    @classmethod
    def eliminar_usuario(cls, cedula):
        node = ManejadorTxt().empleados._head
        while node != None:
            if node.getData().getId == cedula:
                ManejadorTxt().empleados.remove(node)
            node = node.getNext()
        ManejadorTxt.guardar_empleados("C:/Users/andre/Documents/GitHub/EDD/practica/Empleados.txt")
        ManejadorTxt.guardar_passwords("C:/Users/andre/Documents/GitHub/EDD/practica/Password.txt")
    pass

class Equipo():
    def __init__(self, nombre, num_placa, fecha_compra, valor_compra, empleado):
        self._nombre = nombre
        self._num_placa = num_placa
        self._fecha_compra = fecha_compra
        self._valor_compra = valor_compra
        self._empleado = empleado
        
class Sistema():
    @classmethod
    def verificarInfo(cls, cedula, password):
        node = ManejadorTxt().empleados._head
        while node != None:
            if node.getData().getId == cedula and node.getData()._password == password:
                return True
            node = node.getNext()
        return None
    @classmethod
    def verificarRol(cls, cedula):
        node = ManejadorTxt().empleados._head
        while node != None:
            if node.getData().getId == cedula:
                return node.getData()._tipo
            node = node.getNext()
        return None
    
    @classmethod
    def login(cls, cedula, password):
        manejador = ManejadorTxt()
        empleados = manejador.cargarempleados()
        passwords = manejador.cargarPasswords()
        
        nodeEmpleados = empleados._head
        nodePasswords = passwords._head
        while nodeEmpleados != None:
            if nodeEmpleados.getData().id == cedula and nodePasswords.getData().password == password:
                return nodeEmpleados.getData()
            nodeEmpleados = nodeEmpleados.getNext()
            nodePasswords = nodePasswords.getNext()
        return None

    
class App():
    usuario = None
    
    def __init__(self):
        serializador = ManejadorTxt()
        
        empleados = serializador.cargarempleados()
        empleados.printData()
        pass
     
    def main_loop(self):
        while True:
            
            print("Bienvenido al sistema de inventario")    
            
            while self.usuario == None:
                inputId = input("Ingrese su cedula: ")
                inputPassword = input("Ingrese su contraseña: ")
                self.usuario = Sistema.login(inputId, inputPassword)
                
                if self.usuario == None:
                    print("Cedula o contraseña incorrecta")

            print("Bienvenido", self.usuario.nombre)

            print(f"Userr: {self.usuario.tipo}")
            if self.usuario.tipo == "administrador":
                self.menu_administrador()
            else:
                self.menu_investigador()

    def mostrarListaEquipos(self):
        
        
        pass
        
    def menu_administrador(self):
         while True:
            print("--- Ingresaste como Administrador --- ")
            
            print("Menu:")
            print("1.Consultar Lista de Equipos")
            print("2.Registrar nuevo Usuario")
            print("3.Cambiar Contraseñas")
            print("4.Eliminar Usuario")
            print("5.Responder Solicitudes")
            print("6.Salir")

            print(". . . . . . . . . . ")
            
            opcion = input("Elija la opción del Menu: ")

            match opcion:
                case '1':
                    self.menuMensaje()
                case '2':
                    nombre = input("Ingrese el nombre del usuario: ")
                    cedula = input("Ingrese la cedula del usuario: ")
                    
                    fecha_nacimiento = Fecha(input("Ingrese el dia de nacimiento: "), input("Ingrese el mes de nacimiento: "), input("Ingrese el año de nacimiento: "))
                    ciudad_nacimiento = input("Ingrese la ciudad de nacimiento: ")
                    tel = input("Ingrese el telefono del usuario: ")
                    email = input("Ingrese el correo del usuario: ")
                    dire = Direccion(input("Ingrese la calle: "), input("Ingrese la nomenclatura: "), input("Ingrese el barrio: "), input("Ingrese la ciudad: "), input("Ingrese el edificio: "), input("Ingrese el apto: "))
                    password = input("Ingrese la contraseña del usuario: ")
                    tipo = input("Ingrese el tipo de usuario: ")
                    
                    Administrador.agregar_usuario(nombre, cedula, fecha_nacimiento, ciudad_nacimiento, tel, email, dire, password, tipo)
                    
                case '3':
                    cedula = input("Ingrese la cedula del usuario: ")
                    password = input("Ingrese la nueva contraseña: ")
                    Administrador.cambiar_password(cedula, password)
                case '4':
                    cedula = input("Ingrese la cedula del usuario: ")
                    Administrador.eliminar_usuario(cedula)
                case '5':
                    pass
                case '6':
                    print('Saliendo del sistema, hasta luego!')
                    sys.exit()
                case _:
                    print('Opcion no valida')
    
    def menu_investigador(self):
        print("Ingresaste como Investigador")
        print("Menu:")
        print("1.Consultar Lista de Equipos")
        print("2.Solicitar nuevo Equipo")
        print("3.Solicitar eliminación de Equipo")
        print("4.Verificar Estado de su Solicitud")
        print("5.Salir")
        opcion = input("Elija la opción del Menu: ")
        pass    

app = App()
app.main_loop()