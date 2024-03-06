from modulos.clientes import Cliente
from modulos.funciones import saludar
from modulos.funciones import comprar
from modulos.clientes import clientes
from modulos.funciones import finalizar




cliente1 = Cliente(nombre="Juan", apellido="Pérez", correo="juenp@gmail.com",dni=856664356, contraseña=555555)
print(cliente1)
saludar(cliente1)
cliente1.get_datos()
cliente1.registro(cliente1.nombre, cliente1.contraseña)
comprar()
finalizar(cliente1)


cliente2 = Cliente(nombre="pedro", apellido="alvarez", correo="pedrito@gmail.com",dni=5468786, contraseña=454551)
print(cliente2)
saludar(cliente2)
cliente2.get_datos()
cliente2.registro(cliente2.nombre, cliente2.contraseña)
comprar()
finalizar(cliente2)


cliente3 = Cliente(nombre="sol", apellido="diaz", correo="diazsoliados@gmail.com",dni=3354846, contraseña=1234)
print(cliente3)
saludar(cliente3)
cliente3.get_datos()
cliente3.registro(cliente3.nombre, cliente3.contraseña)
comprar()
finalizar(cliente3)


print(clientes)
cliente2.elimar_registro(cliente2.nombre, cliente2.contraseña)

print(clientes)

