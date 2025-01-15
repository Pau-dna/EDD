class Direccion:
    #Atributos
    def __init__(self,calle:str= None,nomenclatura: str=None ,barrio: str= None,ciudad: str= None,edificio: str=None,apto:str=None):      
        self.__calle = calle
        self.__nomenclatura = nomenclatura
        self.__barrio = barrio
        self.__ciudad = ciudad 
        self.__edificio = edificio
        self.__apto = apto
        
    # Getters y Setters
    
    @property 
    def getCalle(self):
        return self.__calle

    def setCalle(self, calle):
        self.__calle = calle
    
    @property 
    def getCiudad(self):
        return self.__ciudad

    def setCiudad(self, ciudad):
        self.__ciudad = ciudad
    
    @property  
    def getNomenclatura(self):
        return self.__nomenclatura

    def setNomenclatura(self, nomenclatura):
        self.__nomenclatura = nomenclatura
    
    @property
    def getEdificio(self):
        return self.__edificio

    def setEdificio(self, edificio):
        self.__edificio = edificio
    
    @property
    def getBarrio(self):
        return self.__barrio

    def setBarrio(self, barrio):
        self.__barrio = barrio
      
    @property   
    def getApto(self):
        return self.__apto

    def setApto(self, apto):
        self.__apto= apto
        
    #Metodo toString()
    def __str__(self): 
        return f"{self.__calle} {self.__nomenclatura} {self.__barrio} {self.__ciudad} {self.__edificio} {self.__apto}"
