from usuario import *
class Agenda:
    #Atributos
    def __init__(self,registro= [],no_reg: int=0,capacity: int=0):  
            
            self.__registro = []*capacity
            self.__no_reg = no_reg
            self.__capacity = capacity
            

    
    @property 
    def getCapacity(self):
        return self.__capacity  
    @property 
    def getRegistro(self):
        return self.__registro
    
    def agregar(self,u):
        if u in self.__registro:
            return False
        elif (len(self.getRegistro)+1)<= self.getCapacity:
            self.__registro.append(u)
            return True
        else:
            return False
            
    def buscar(self,id):
        for x in self.getRegistro:
            indice=0
            if x.getId() == id:
                return indice
            indice+=1

    
if __name__ == "__main__":
        persona1=Usuario("j",1,Fecha(),"dfgd",546,"fdsgsf",Direccion())
        persona2=Usuario("j",2,Fecha(),"dfgd",546,"fdsgsf",Direccion())
        persona3=Usuario("j",3,Fecha(),"dfgd",546,"fdsgsf",Direccion())
        lista=Agenda()
        
        lista.agregar(persona1)
        lista.agregar(persona2)
        lista.agregar(persona3)
        print(lista.buscar(1))
        
            