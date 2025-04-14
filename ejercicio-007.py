"""

herencia 

"""

class Animal :

    def __init__(self, name: str):
        self.name = name

    def sound(self):
        pass

class dog(Animal):

    def sound(self):
        print("guau")

class cat(Animal):

    def sound(self):
        print("miau")

my_animal = Animal("animal")
my_animal.sound()
my_dog = dog("perro")
my_dog.sound()
my_cat = cat("cato")
my_cat.sound()


#ejercicio

class empresa:

    def __init__(self, id:int, name: str):
        self.id = id
        self.name = name
        self.empleados = []
    
    def add(self, empresa):
        self.empleados.append(empresa)

    def print_empleados(self):
        for  empresa in self.empleados:
            print(empresa.name)

class manager(empresa):

    def coordinador_proyectos(self):
        print(f"{self.name} esta coordinando todos los proyectos de la empresa. ")

class proyectosManager(empresa):

    def __init__(self, id:int, name:str, project:str):
        super().__init__(id, name)
        self.project = project

    def coordinador_proyetos(self):
        print(f"{self.name} esta coordinando su proyecto.")
    
class programador(empresa):
    
    def __init__(self, id: int, name:str, lenguaje: str):
        super().__init__(id, name)
        self.lenguaje = lenguaje
    
    def code(self):
        print(f"{self.name} esta programado en  {self.lenguaje}")
    
    def add(self, empresa: empresa):
        print(f"un programador no tiene empleados a su cargo. {empresa.name} no se añadira")
    
my_manager = manager(1, "luis")
my_proyect_manager = proyectosManager(2, "rodrigo", "proyecto 1")
my_proyect_manager2 = proyectosManager(3, "Mairaa", "proyecto2")
my_programmer = programador(4, "nazareth", "java")
my_programmer1 = programador(5, "mia", "c++")
my_programmer2 = programador(6, "monse", "python")
my_programmer3 = programador(7, "lucia", "dart")
my_programmer4 = programador(8, "monchi", "cobol")

my_manager.add(my_proyect_manager)
my_manager.add(my_proyect_manager2)

my_manager.add(my_programmer)
my_manager.add(my_programmer2)
my_manager.add(my_programmer3)
my_manager.add(my_programmer4)

my_programmer.add(my_programmer2)

my_programmer.code()
my_proyect_manager.coordinador_proyetos()
my_manager.coordinador_proyectos()
my_manager.print_empleados()
my_proyect_manager.print_empleados()
my_programmer.print_empleados( )