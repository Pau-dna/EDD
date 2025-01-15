from fecha import *
from direccion import *

class Usuario:
    #Atributos

    def __init__(self, nombre: str = None, id: int = None, fecha_nacimiento: Fecha = Fecha(), 
                 ciudad_nacimiento: str = None, tel: int = None, email: str = None, dir: Direccion = Direccion()):
        
        self.nombre = nombre
        self.id = id
        self.fecha_nacimiento = fecha_nacimiento
        self.ciudad_nacimiento = ciudad_nacimiento
        self.tel = tel
        self.email = email
        self.dir = dir

    #Setters

    def setNombre(self, nombre: str):
        self.nombre = nombre

    def setId(self, id: int):
        self.id = id

    def setFecha_nacimiento(self, fecha: Fecha):
        self.fecha_nacimiento = fecha

    def setCiudad_nacimiento(self, ciudad: str):
        self.ciudad_nacimiento = ciudad

    def setTel(self, tel: int):
        self.tel = tel

    def setEmail(self, email: str):
        self.email = email

    def setDir(self, dir: Direccion):
        self.dir = dir
        
    #getters
     
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
    
    #Metodo toString()
    def str(self): 
        return f"{self.getNombre} {self.getId} {self.getFecha_nacimiento} {self.getCiudad_nacimiento} {self.getTel} {self.getEmail} {self.getDir}"

