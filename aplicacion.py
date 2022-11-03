username = open("login.txt")
pasword= open("clave.txt")

usuario = username.read()
clave = pasword.read()

print("Bienvenido, ingrese su usuario y contraseña")
print("Usuario: ")
user =input()
print("Contrasena: ")
pwd = input()

if user == usuario and pwd==clave:
    print("Bienvenido al programa")
    print("    Menú")
    print("1. Listar persona")
    print("2. Agregar personas")
    print("3. Salir")
else:
    print("usuario o contraseña invalido!")
    print("Usuario: ")
    user =input()
    print("Contrasena: ")
    pwd = input()
if user == usuario and pwd==clave:
      print("Bienvenido al programa")
      print("    Menú")
      print("1. Listar persona")
      print("2. Agregar personas")
      print("3. Salir")
else:
    print("usuario o contraseña invalido!")
