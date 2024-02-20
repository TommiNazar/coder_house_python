
# base de datos

base_dato = { "leandro" : "387", "graciela" : "987"}


#funcion de registro de usuarios

def registrar (BD):

    t = 0

    while t == 0:
        usuario = input("ingrese nombre del usuario: ")
        contraseña = input("ingrese contraseña: ")
        BD [usuario] = contraseña

        reingreso = input("presione 1 se quiere agregar otro usuario o 2 si quiere volver al menu: ")
        if reingreso == "1" :
            t = 0
        else:
            t = 1
    
#funcion de leer la base de datos

def leer_bd (BD):
    print(f"\nla base de dato es: \n", BD)

#funcion de logeo
def loging (BD):
    usuario = input("ingrese nombre del usuario: ")
    contraseña = input("ingrese contraseña: ")

    if usuario not in BD or contraseña not in BD[usuario] :
        print("ingreso mal el nombre del usuario")
        print("o mal contraseña")
        programa()

    
        
    if usuario in BD and contraseña in BD[usuario] : 
        print(f"bienvenido {usuario} has ingresado correctamente")
        reingreso = input("1 si quiere volver al menu: ")
        if reingreso == "1" :
            programa()
        else:
            salir()

#funcion de cerrar programa
def salir ():
    print ("chau")

#funcion que gestiona al programa
def programa ():

    i = 0

    while i == 0:
        n = input("\n ingresa 1 si quieres registrar un usuarion \n ingrese 2 si quiere ver la base de dato \n ingrese 3 si quiere logearse \n ingrese 4 para salir: ")
        if n == "1":
            registrar(base_dato)
        if n == "2":
            leer_bd (base_dato)
        if n =="3":
            loging(base_dato)
        if n == "4":
            salir()
            i = 1
            break
        

#llamar a la funcion q engloba el programa
programa()




