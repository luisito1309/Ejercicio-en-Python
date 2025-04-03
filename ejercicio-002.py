#cadenas

#operaciones

s0="hola "
s1="a todos "
s2="mi nombre "
s3="python"

print(s0+s1)

#repeticion
print(s0 * 4)

#indexcion
print(s1[3])

#porcciones
print(s2[0:5])
print(s1[0:6])
print(s0[0 :4])

#busqueda
print("a" in s0 )
print("f"in s1) 
print("4"in s2)

#remplazo
print(s0.replace("a" ,"x") )
print(s1.replace("o" ,"i") )
print(s2.replace("m" ,"5") )

#mayuscula y minuscula
print(s0.upper())
print(s1.lower())
print(f"hola {s2}es rodrigo".title())
print("hola como estan todos".capitalize())

#formateo
print("saludo:{}, lenguaje:{}".format(s0, s3))

#interpolacion
print(f"saludo:{s0}, lenguaje:{s3}")

#ejercicio
def cadenas(word1: str, word2:str,word3: str, word4: str, word5: str):
    print(f"{word1} es un palindromo?: {word1 == word1[::-1]}")
    print(f"{word2} es un palindromo?: {word2 == word2[::-1]}")
    print(f"{word3} es un palindromo?: {word3 == word3[::-1]}")
    print(f"{word4} es un palindromo?: {word4 == word4[::-1]}")
    print(f"{word5} es un palindromo?: {word5 == word5[::-1]}")

cadenas("espada", "radar", "espada", "locura", "Ana")