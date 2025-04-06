"""
valor y referencia

"""

#tipos de datos por valores

my_int_a = 10
my_int_b = my_int_a
my_int_b = 50
print(my_int_a)
print(my_int_b)

#tipos de datos por referencia
my_lista_a = [10, 20]
my_lista_b = my_lista_a
my_lista_b.append(40)
print(my_lista_a)
print(my_lista_b)

#funcion de datos por valor

int_c = 40

def datos_valor(my_int : int):
    my_int = 20
    print(my_int)
datos_valor(int_c)
print(int_c)

#funcion de datos por referencia

def datos_ref(my_list : list):
    my_list.append(5)

    my_list_d = my_list
    my_list_d.append(40)

    print(my_list)
    print(my_list_d)

my_list_c = [20,30]
datos_ref(my_list_c)
print(my_list_c)

#ejercicio
my_int_e = 4
my_int_f = 1
def ref(value_a : list, value_b : list) -> tuple:
    temp = value_a
    value_a = value_b
    value_b = temp
    value_b.append(43)
    return value_a, value_b
my_list_e = [20, 40]
my_list_f = [10, 25]
ref(my_list_e, my_list_f)
print(my_int_e)
print(my_int_f)