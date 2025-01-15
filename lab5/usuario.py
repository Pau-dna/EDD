from fecha import *
from direccion import *


class Usuario:
    def __init__(self, nombre: str = None, idUsuario: str = None):
        self.nombre = nombre
        self.id = idUsuario
        self.fecha_nacimiento: Fecha = None
        self.ciudad_nacimiento: str = None
        self.tel: str = None
        self.email: str = None
        self.dir: Direccion = None
    
    # Setter methods
    def setNombre(self, nombre):
        self.nombre = nombre
    def setId(self, id):
        self.id = int(id)
    def setFecha_nacimiento(self, fecha):
        self.fecha_nacimiento = fecha
    def setCiudad_nacimiento(self, ciudad):
        self.ciudad_nacimiento = ciudad
    def setTel(self, telefono):
        self.tel = telefono
    def setEmail(self, email):
        self.email = email
    def setDir(self, dir):
        self.dir = dir
    
    # Getter methods
    def getNombre(self):
        return self.nombre
    
    def getId(self):
        return self.id
    
    def getFecha_nacimiento(self):
        return self.fecha_nacimiento
    
    def getCiudad_nacimiento(self):
        return self.ciudad_nacimiento
    
    def getTel(self):
        return self.tel
    
    def getEmail(self):
        return self.email
    
    def getDir(self):
        return self.dir
    
    # String representation
    def __str__(self):
        return f'{self.nombre} - {self.id} - {self.fecha_nacimiento} - {self.ciudad_nacimiento} - {self.tel} - {self.email} - {self.dir}'
    