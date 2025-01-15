from fecha import *
from direccion import *

class Usuario:
    #Atributos

    def __init__(self, nombre: str = None, id: int = None, fecha_nacimiento: Fecha = Fecha(), 
                 ciudad_nacimiento: str = None, tel: int = None, email: str = None, dir: Direccion = Direccion()):
        
        self.__nombre = nombre
        self.__id = id
        self.__fecha_nacimiento = fecha_nacimiento
        self.__ciudad_nacimiento = ciudad_nacimiento
        self.__tel = tel
        self.__email = email
        self.__dir = dir

    #Setters

    def setNombre(self, nombre: str):
        self.__nombre = nombre

    def setId(self, id: int):
        self.__id = id

    def setFecha_nacimiento(self, fecha: Fecha):
        self.__fecha_nacimiento = fecha

    def setCiudad_nacimiento(self, ciudad: str):
        self.__ciudad_nacimiento = ciudad

    def setTel(self, tel: int):
        self.__tel = tel

    def setEmail(self, email: str):
        self.__email = email

    def setDir(self, dir: Direccion):
        self.__dir = dir
        
    #getters
     
    @property 
    def getNombre(self):
        return self.__nombre
     
    @property 
    def getId(self):
        return self.__id

     
    @property 
    def getFecha_nacimiento(self):
        return self.__fecha_nacimiento

     
    @property 
    def getCiudad_nacimiento(self):
        return self.__ciudad_nacimiento

     
    @property 
    def getTel(self):
        return self.__tel

 
    @property 
    def getEmail(self):
        return self.__email

 
    @property 
    def getDir(self):
        return self.__dir
    
    #Metodo toString()
    def __str__(self): 
        return f"{self.getNombre} {self.getId} {self.getFecha_nacimiento} {self.getCiudad_nacimiento} {self.getTel} {self.getEmail} {self.getDir}"

