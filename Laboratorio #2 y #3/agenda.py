from usuario import *
class Agenda:
    #Atributos
    def __init__(self, capacity=0):  
        self.__registro = [None] * capacity  # Array con tamaño fijo
        self.__no_reg = 0  # Número de registros actuales
        self.__capacity = capacity
    
  # Getters
    @property
    def getCapacity(self):
        return self.__capacity

    @property
    def getRegistro(self):
        return self.__registro

    @property
    def getNoReg(self):
        return self.__no_reg
    
         
       
    def agregar(self, usuario):
       
        # Verificar si el usuario ya existe en el registro
        if self.buscar(usuario.getId) != -1:
            return False  # El usuario ya está registrado

        # Verificar si hay espacio para agregar un nuevo usuario
        if self.__no_reg < self.__capacity:
            # Insertar en orden, desplazando elementos si es necesario
            i = self.__no_reg
            self.__registro[i] = usuario
            self.__no_reg += 1
            return True

        return False  # No hay espacio en la agenda
    
    
    def buscar(self, id):
        for i in range(self.__no_reg):  # Recorrer solo los registros activos
            if self.__registro[i] is not None and self.__registro[i].getId == id:
                return i
        return -1  # Usuario no encontrado
    


    def eliminar(self, i):
        if i < 0 or i >= self.__no_reg:
            return None
        else:
            # Guardar el usuario que será eliminado
            temp = self.__registro[i]

            # Desplazar usuarios para llenar el vacío
            for j in range(i, self.__no_reg - 1):
                self.__registro[j] = self.__registro[j + 1]
            self.__registro[self.__no_reg - 1] = None
            self.__no_reg -= 1
            return temp

    def to_file(self, file_path):
        
        try:
            with open(file_path, "w") as file:
                for i in range(self.__no_reg):
                    usuario = self.__registro[i]
                    # Serializamos los datos del usuario
                    file.write(f"{usuario.getNombre},{usuario.getId},{usuario.getFecha_nacimiento.get_Dia}/{usuario.getFecha_nacimiento.get_Mes}/{usuario.getFecha_nacimiento.get_A},{usuario.getCiudad_nacimiento},{usuario.getTel},{usuario.getEmail},{usuario.getDir.getCalle},{usuario.getDir.getNomenclatura},{usuario.getDir.getBarrio},{usuario.getDir.getCiudad},{usuario.getDir.getEdificio},{usuario.getDir.getApto}\n")
            print("Agenda exportada con éxito.")
        except Exception as e:
            print(f"Error al exportar la agenda: {e}")
            
    def import_from_file(self, file_path):
        try:
            with open(file_path, "r") as file:
                for line in file:
                    # Dividir los datos en partes
                    data = line.strip().split(",")
                    nombre = data[0]
                    id_ = int(data[1])
                    dd, mm, aa = map(int, data[2].split("/"))
                    fecha_nacimiento = Fecha(dd, mm, aa)
                    ciudad_nacimiento = data[3]
                    tel = int(data[4])
                    email = data[5]
                    direccion = Direccion(data[6], data[7], data[8], data[9], data[10], data[11])
                    usuario = Usuario(nombre, id_, fecha_nacimiento, ciudad_nacimiento, tel, email, direccion)
                    
                    # Intentar agregar al usuario
                    self.agregar(usuario)
            print("Agenda importada con éxito.")
        except Exception as e:
            print(f"Error al importar la agenda: {e}")





   