"""

pilas y cola

"""

#pilas/stack

pilas = []


pilas.append("12")
pilas.append("30")
pilas.append("10")
print(pilas)


pilas_item = pilas[len(pilas)-1]
del pilas[len(pilas)-1]
print(pilas.pop())
print(pilas)


#cola/queue

queue = []

queue.append("12")
queue.append("30")
queue.append("10")
print(queue)

queue_item = queue[0]
del queue[0]
print(queue_item)
print(queue.pop(0))
print(queue)



"""

ejercicio de web

"""

def primera_pagina_web():
    
    pilas=[]

    while True:

        action = input(
            "añade una url o interactúa con palabras adelante/atras/salir: "
        )

        if action == "salir":
            print("saliendo del navegador web")
            break
        elif action == "adelante":
            pass

        elif action == "atras":
            if len(pilas)> 0:
                pilas.pop()

        else:
            pilas.append(action)
        if len(pilas)> 0:
            print(f"has navegado a la web{pilas[len(pilas)-1]}.")
        else :
            print("estas en la pagina del inicio")