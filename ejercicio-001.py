#estructura  de datos
 
lista=["amarrillo", "rojo", "azul", "negro", "verde", "morado","blanco"]
print(lista)
lista.append("dorado")
print(lista)
lista.extend("colores")
print(lista)
lista.sort()
print(lista)
lista.remove("rojo")
print(lista)

#diccionario

my_diccionario: dict = {
    "name": "luis",
    "apellido": "aguilar",
    "gmail":"rodrigoaguilar@gmail.com",
    "edad": "20"
}
my_diccionario["alias"] = "luis@gmail.com" #insercion de un nuevo dato
print(my_diccionario)
del my_diccionario["apellido"]#eliminacion de dato
print(my_diccionario)
print(my_diccionario["name"]) #acceso
print(my_diccionario)
my_diccionario["edad"]="21" #reemplazar un dato
print(my_diccionario)
print(type(my_diccionario))


#ejercicio en consola

def agenda_Nombres_Apellido_edad():
    agenda = {}

    while True:
        print("\n//")
        print("1. Agregar su nombre")
        print("2. Agregar su apellido y edad")
        print("3. Agregar su carrera")
        print("4. Mostrar agenda")
        print("5. Salir")

        option = input("\nSeleccione un número del 1 al 5: ")

        match option:
            case "1":
                name = input("Introduce tu nombre: ").strip()
                if name.isalpha():  # Verifica que solo haya letras
                    agenda["nombre"] = name
                    print(f"Nombre guardado: {name}")
                else:
                    print("Error: El nombre solo debe contener letras.")

            case "2":
                apellido = input("Introduce tu apellido: ").strip()
                if not apellido.isalpha():
                    print("Error: El apellido solo debe contener letras.")
                    continue

                edad = input("Introduce tu edad: ").strip()
                if not edad.isdigit():
                    print("Error: La edad solo debe contener números.")
                    continue

                agenda["apellido"] = apellido
                agenda["edad"] = int(edad)
                print(f"Apellido y edad guardados: {apellido}, {edad} años")

            case "3":
                carrera = input("Introduce tu carrera: ").strip()
                if carrera.isalpha():
                    agenda["carrera"] = carrera
                    print(f"Carrera guardada: {carrera}")
                else:
                    print("Error: La carrera solo debe contener letras.")

            case "4":
                if agenda:
                    print("\nSu agenda está completa. Usted es:")
                    print(f"Nombre: {agenda.get('nombre', 'No registrado')}")
                    print(f"Apellido: {agenda.get('apellido', 'No registrado')}")
                    print(f"Edad: {agenda.get('edad', 'No registrada')}")
                    print(f"Carrera: {agenda.get('carrera', 'No registrada')}")
                else:
                    print("La agenda está vacía.")

            case "5":
                print("Saliendo de la agenda.")
                break

            case _:
                print("Seleccione un número del 1 al 5.")

# Ejecutar la función
agenda_Nombres_Apellido_edad()
 

