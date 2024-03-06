clientes = []

class Cliente:
    def __init__(self, nombre, apellido, correo, dni, contraseña):
        self.nombre = nombre
        self.apellido = apellido 
        self.correo = correo
        self.dni = dni
        self.contraseña = contraseña

    def __str__(self):
        return f"{self.nombre} {self.apellido} {self.correo} {self.dni} {self.contraseña}"
    
    def get_datos(selt):
        print("Datos del Cliente")
        print(f"Nombre: {selt.nombre}")
        print(f"Apellido: {selt.apellido}")
        print(f"Correo: {selt.correo}")
        print(f"DNI: {selt.dni}")

    def registro(self, nombre, contraseña):
        print ("los datos a guardar son \n","nombre: ",nombre,"contraseña: ", contraseña)
        registro_cliente = f"{nombre}  {contraseña}"
        clientes.append(registro_cliente)

    def elimar_registro(self, nombre, contraseña):
        print ("los datos a eliminar son \n","nombre: ",nombre,"contraseña: ", contraseña)
        eliminar_registro = f"{nombre}  {contraseña}"
        clientes.remove(eliminar_registro)

