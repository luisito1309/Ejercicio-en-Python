"""

clases

"""

class programador:
    apellido : str = None

    def __init__(self, nombre:str, edad:int, lenguaje:list):
        self.nombre = nombre
        self.edad = edad
        self.lenguaje = lenguaje

    def print(self):
        print(
            f"Nombre: {self.nombre} | edad: {self.edad} | lenguaje: {self.lenguaje} | Apellido: {self.apellido}"
        )

mi_programa = programador ("Luis Rodrigo", 20,["python, java, c++"] )
mi_programa.print()
mi_programa.apellido = "Aguilar Justiniano"
mi_programa.print()
mi_programa.edad = 21
mi_programa.print()


#ejercicio

class stack:

    def __init__(self):
        self.stack = []
    def push(self, item):
        self.stack.append(item)
    def pop(self):
        if self.count() == 0:
            return None
        return self.stack.pop()
    def count(self):
        return len(self.stack)
    def print(self):
        for item in reversed(self.stack):
            print(item)

my_stack = stack()
my_stack.push("A")
my_stack.push("B")
my_stack.push("C")
print(my_stack.count())
my_stack.print()
my_stack.pop()
print(my_stack.count())