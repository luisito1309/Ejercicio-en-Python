"""

recursividad

"""
def contador(number : int):
    if number >=0:
        print(number)
        contador(number - 1)

contador(3)


def factorial(number : int) -> int:
    if number < 0:
        print("Los numeros negativos no son validos")
        return 0
    elif number == 0 :
        return 1
    else:
        return number * factorial(number -1)

print(factorial(7))

def fibonacci(number: int) -> int:
    if number <= 0:
        print("la posicion tiene que ser mayor que cero")
        return 0
    elif number ==1:
        return 0
    elif number ==2:
        return 1
    else:
        return fibonacci(number - 1) + fibonacci(number - 2)
    
print(fibonacci(10))