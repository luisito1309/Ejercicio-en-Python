#tipos de funciones

def saludar():
    print("hola mundo")

saludar()

#con retorno
def retorno_saludar():
    return "hola maira"

saludar = retorno_saludar
print(saludar())

#con argumentos
def saludar_argumentos(saludar, nombre):
    print(f"{saludar}, {nombre}")
    
#solo un argumneto
saludar_argumentos("hola", "maya")

def saludar_arg(nombre):
    print(f"hola, {nombre}")

saludar_arg("a todos")

#con un argumento predeterminado
def defaul_saludar(nombre="Rodrigo"):
    print(f"hola {nombre}")

defaul_saludar("luis")
defaul_saludar()

def saludo_arg(saludo, nombre):
    print(f"{saludo} {nombre}")

saludo_arg(saludo="hola a todos", nombre ="mi nombre es Rodrigo")
saludo_arg("rodrigo", "hola")


#con numero de variables

def variable_arg_saludar(*names):
    for name in names:
        print(f"hola, {name}")

variable_arg_saludar("luis", "maira", "rodrigo", )


#variable con clave
def variable_clave_argumentos(**datos):
    for clave, value in datos.items():
        print(f"hola, {value}({clave})")

variable_clave_argumentos(
    lenguaje= "python",
    nombre= "luis",
    alias= "luisito",
    edad= 20
)

#funcion en otra funcion

def funcion_externa():
    def funcion_interna():
        print("hola luis")
    funcion_interna()
funcion_externa()

#variables locales y globales

nombre= "luis"
lenguaje="python"
edad=20
carrera="ing sistemas"

def profesion_upds():
    saludar= "buenos dias"
    print(f"{saludar},mi nombre es {nombre} estoy usando {lenguaje},\n y tengo {edad} y estoy en la carrera {carrera}")
profesion_upds()

