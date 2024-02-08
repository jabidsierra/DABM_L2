class Persona:
    def __init__(self, nombre, tipo_usuario, contrasena,controlador):
        self.nombre = nombre
        self.tipo_usuario = tipo_usuario
        self.contrasena = contrasena
        self.controlador = controlador
        

    def acceder_menu(self):

            while True:
                print("\n"*5)
                print("-"*50)
                print("Menú".center(50," "))
                print("-"*50)
                print("[1] Agregar dispositivo")
                print("[2] Eliminar dispositivo")
                print("[3] Agregar función a dispositivo")
                print("[4] Operar dispositivos")
                print("[5] Salir")
                opcion = int(input("Seleccione una opción: "))
                if opcion == 1:
                    if self.tipo_usuario == "admin":
                        self.controlador.agregar_dispositivo()

                    else:
                        print("No tiene permisos para realizar está acción")
                elif opcion == 2:
                    if self.tipo_usuario == "admin":
                        self.controlador.eliminar_dispositivo()
                    else:
                        print("No tiene permisos para realizar está acción")
                elif opcion == 3:
                    if self.tipo_usuario == "admin":
                        self.controlador.agregar_funcion_dispositivo()
                elif opcion == 4:
                    self.controlador.operar_dispositivos()
                                
                elif opcion == 5:
                    main()
                else:
                    print("Opción inválida")




class Dispositivo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.acciones = []

    def agregar_accion(self,accion):
            self.acciones.append(accion)

class Accion:
    def __init__(self, nombre,parametros=None):
        self.nombre= nombre
        self.parametros = parametros if parametros is not None else []

    def  agregar_parametro(self,parametro):
        self.parametros.append(parametro)
    

class ControladorDispositivo:
    def __init__(self):
        self.dispositivos = []

    def agregar_dispositivo(self):
        print("\n"*5)
        print("-"*50)
        print("Agregar Dispositivo".center(50," "))
        print("-"*50)
        dispositivo = Dispositivo(input("Ingrese el nombre del dispositivo: "))
        self.dispositivos.append(dispositivo)

    def eliminar_dispositivo(self):
        print("\n"*5)
        print("-"*50)
        print("Eliminar dispositivo".center(50," "))
        print("-"*50)
        nombre_dispositivo = input("Ingrese el nombre del dispositivo a eliminar: ")
        for dispositivo in self.dispositivos:
            if dispositivo.nombre == nombre_dispositivo:
                self.dispositivos.remove(dispositivo)
                return
            else:
                print("Dispositivo no encontrado")

    def agregar_funcion_dispositivo(self):
        print("\n"*5)
        print("-"*50)
        print("Agregar Función".center(50," "))
        print("-"*50)
        nombre_dispositivo = input("Ingrese el nombre del dispositivo al que desea agregar una función: ")
        dispositivo = None
        for d in self.dispositivos:
            if d.nombre == nombre_dispositivo:
                dispositivo = d
        
        if dispositivo:
            nombre_funcion = input("Ingrese el nombre de la función: ")
            parametros = input("Ingrese los parámetros de la función (separados por comas): ").split(",")
            funcion = Accion(nombre_funcion, parametros)
            dispositivo.agregar_accion(funcion)
        else:
            print("Dispositivo no encontrado")

    def mostrar_dispositivos_y_acciones(self):
        for dispositivo in self.dispositivos:
            print("Nombre del dispositivo: "+dispositivo.nombre)
            print("Acciones:")
            for accion in dispositivo.acciones:
                print(accion.nombre)
            print()

    def operar_dispositivos(self):
        self.mostrar_dispositivos_y_acciones()
        dispositivo_elegido = input ("Ingrese el nombre del dispositivo a operar: ")
        accion_elegida = input("Ingrese la acción que desea realizar con este dispositivo: ")
        dispositivo = None
        for d in self.dispositivos:
            if d.nombre == dispositivo_elegido:
                dispositivo = d
        if dispositivo:
            accion = None
            for a in dispositivo.acciones:
                if a.nombre == accion_elegida:
                    accion = a
            if accion:
                print("Se va a realizar la acción: ", accion.nombre," en el dispositivo ",dispositivo.nombre)
            else:
                print("La acción: ",accion_elegida," no se encuentra registrada")
        else:
            print("El dispositivo ", dispositivo_elegido," no se encuentra registrado.")


    def mostrar_dispositivos_y_acciones(self):
        for dispositivo in self.dispositivos:
            print("Nombre: "+dispositivo.nombre)
            print("Acciones")
            for accion in dispositivo.acciones:
                print(accion.nombre)
            print()

def main():
    
    controlador = ControladorDispositivo()
    while True:
        print("\n"*5)
        print("-"*50)
        print("Sistema de Control de Dispositivos Domésticos".center(50," "))
        print("-"*50)
        print("[I]Ingresar")
        print("[R]Registrar Usuario")
        print("[S]Salir")

      
        opcion=input(":>").upper()

        if opcion == "R":
            print("\n"*5)
            print("-"*50)
            print("Registro de usuario".center(50," "))
            print("-"*50)
            name=input("Nombre de Usuario: ")
            password=input("Contraseña: ")
            type=input("Tipo de Usuario (\"admin\",\"pac\"): ")

          
            if existe_usuario(name, usuarios):
                print("El usuario ya existe.")
   
            usuario = Persona(name, type, password,controlador)
            usuarios.append(usuario)
            print("Usuario registrado exitosamente.")

        elif opcion == "I":

            print("\n"*5)
            print("-"*50)
            print("Inicio de Sesión".center(50," "))
            print("-"*50)
            name=input("Nombre de Usuario: ")
            password=input("Contraseña: ")
            usuario = next((u for u in usuarios if u.nombre == name and u.contrasena == password), None)

            if usuario:
                usuario.acceder_menu()

            else:
                print("El usuario no existe o la contraseña es incorrecta.")
        elif opcion == "S":
            exit()

        else:
            print("Opción invalida")
            main()

def existe_usuario(name, usuarios):
    return next((u for u in usuarios if u.nombre == name), None) is not None  
usuarios = []
main()

