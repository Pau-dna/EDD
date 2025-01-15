from direccion import *
from fecha import *
from usuario import *
class Main:
  
    if __name__ == "__main__":
        """""
        fecha1 = Fecha(29,10,2005)
        print(f"{fecha1.get_Dia} - {fecha1.get_Mes} - {fecha1.get_A}")
        
        direccion1 = Direccion("Calle 54A", "30-01", "Boston", "Medellín", "Edificio Central", "101")
        print(direccion1)
        
        usuario1 = Usuario("Juan",11111111,Fecha(10,12,2005),"Medellin",333333335,"Correo@gmail.com",Direccion("Calle 10","11-37","San Nicolas","Medellin"))
        print(usuario1)
        """
        
        Nombre= str(input("Ingrese el nombre: "))
        while True:
            try:
                    Id= int(input("Ingrese el id: "))
                    FechaD= int(input("Ingrese dia de la fecha de nacimiento: "))
                    FechaM= int(input("Ingrese mes de la fecha de nacimiento: "))
                    FechaA= int(input("Ingrese año de la fecha de nacimiento: "))   
                    tel=int(input("Ingrese su numero de telefono: "))    
                    break
            except ValueError:
                    print("Error: Debe ingresar un número entero válido.")     
            
        Ciudad= str(input("Ingrese su ciudad de nacimiento: "))
        email=str(input("Ingrese su email: "))
        dirC= str(input("Ingrese su direccion en orden: Calle,Nomenclatura,Barrio,Ciudad,Edificio,Apartamento: "))
        dirN= str(input())
        dirB= str(input())
        dirCi= str(input())
        dirE= str(input())
        dirA= str(input())
        
        usuario2=Usuario(Nombre,Id,Fecha(FechaD,FechaM,FechaA),Ciudad,tel,email,Direccion(dirC,dirN,dirB,dirCi,dirE,dirA))
        
        print(usuario2)
        
        