"""

MANEJOS DE FICHEROS

"""

import os

file_name = "ing-luis.txt"

with open(file_name, "w")as file:
    file.write("Nombre: Luis Rodrigo\n")
    file.write("Edad: 20 años\n")
    file.write("lenguaje favorito: Python\n")
    file.write("Carreara: Ingenieria de Sistemas")
with open(file_name, "r")as file:
    print(file.read())

os.remove(file_name)




#ejercicio

file_Name = "ejecicios en python"

open(file_Name, "a")

while True:
    print("1. Añadir Producto")
    print("2. Consultar Producto")
    print("3. Actualizar Producto")
    print("4. Borrar Producto")
    print("5. Borrar Producto")
    print("6. Calcular Producto")
    print("7. Calcular Producto")
    print("8. Salir")

    option = input("Selecciona una opcion: ")

    if option == "1":
        name = input("Nombre: ")
        quantity = input("Cantidad: ")
        price = input("Precio: ")
        with open(file_Name, "a")as file:
            file.write(f"{name}, {quantity}, {price}\n")

    if option == "2":
        name = input("Nombre:")
        with open(file_Name, "r")as file:
            for line in file.readlines():
                if line.split(", ")[0]== name:
                    print(line)
                    break

    if option == "3":
        name = input("Nombre: ")
        quantity = input("Cantidad: ")
        price = input("Precio: ")
        with open(file_Name, "r")as file:
            lines = file.readlines()
        with open(file_Name, "w")as file:
            for line in file.readlines:
                if line.split(", ")[0] == name:
                    file.write(f"{name}, {quantity}, {price}\n")
                else:
                    file.write(line)

    if option == "4":
        name = input("Nombre: ")
        with open(file_Name, "r")as file:
            line = file.readline()
        with open(file_Name, "w")as file:
            for line in lines:
                if line.split(", ")[0] != name: 
                    file.write(line)

    if option == "5":
        with open(file_Name, "r")as file:
            print(file.read())

    if option == "6":
        total = 0
        with open(file_Name, "r")as file:
            for line in file.readlineas():
                components = line.split(", ")
                quantity = int(components[1])
                price = float(components[2])
                total += quantity * price
        print(total)
    
    if option == "7":
        name = input("Nombre :")
        total = 0
        with open(file.Name, "r")as file:
            for line in file.readlineas():
                components = line.split(", ")
                if components[0] == name:
                    quantity = int(components[1])
                    price = float(components[2])
                    total += quantity * price
        print(total)
                
    if option == "8":
        os.remove(file_Name)
        break
    else:
        print("Selecciona una de las opciones disponibles.")
