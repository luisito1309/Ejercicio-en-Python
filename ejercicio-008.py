"""

EXCEPCIONES

"""

try:
    print(10/1)
    print([1, 2, 3, 4][4])
except Exception as e:
    print(f"se ha produccido un error: {e}")


#ejercicio
def process_params_a(parameters: list):

    print(parameters[2])

process_params_a([1, 2, 3])


def process_params_a(parameters: list):

    if len(parameters)<3:
        raise IndexError()
    elif parameters[1] ==0:
        raise ZeroDivisionError()

    print(parameters[2])
    print(parameters[0]/parameters[1])

try:
    process_params_a([1, 2, 3])
except:
    print("se ha producciodo un error")


print("el programa finaliza")