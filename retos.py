# #Número mayor y menor: 
# # dado dos números decir cuál es mayor y si ambos son iguales

# valores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# def mayor_menor(valores):
#     numero = [int(n) for n in valores]
#     mayor = max(numero)
#     menor = min(numero)
#     return (f"el número mayor es: {mayor} y el número menor es {menor}")
        
# respuesta = mayor_menor(valores)
# print (respuesta)
# print ("hola mundo")

# # genera un número aleatorio
# import random 

# number = random.randrange(1, 100)
# print (number)

# ''' 
# Intervalos: generar un número aleatorio entre 1 y 120, decir si se 
# encuentra en el intrervalo entre 10 y 50, o bien si es mayor de 50 hasta 100 
# o bien si es mayor de 100 o bien si es menor de diez
# '''

# x = random.randrange(121)

# if x < 10:
#     print("número inferior de 10 pero mayor a 0 ")
# elif x < 50:
#     print("número superior a 10 y menor de 50")
# elif x < 100:
#     print("número inferior a 100 y mayor a 50")
# else: 
#     print("es mayor de 100 hata 120")

# #Pares (7) 
# for n in range(10, 20): 
#     if n % 2 == 0:
#         print ({f"{n} es un número par"})
#     else:
#         pass

# # bucles: listar los números del 1 al 10
# for n in range(1, 11):
#     print (n)

# #series:
# total = 0 

# def serie():
#     for n in range (10, 20, 2):
#         total = total + n
#         return total

# value = serie()
# print(value)#Número mayor y menor: 
# # dado dos números decir cuál es mayor y si ambos son iguales

# valores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# def mayor_menor(valores):
#     numero = [int(n) for n in valores]
#     mayor = max(numero)
#     menor = min(numero)
#     return (f"el número mayor es: {mayor} y el número menor es {menor}")
        
# respuesta = mayor_menor(valores)
# print (respuesta)
# print ("hola mundo")

# # genera un número aleatorio
# import random 

# number = random.randrange(1, 100)
# print (number)

# ''' 
# Intervalos: generar un número aleatorio entre 1 y 120, decir si se 
# encuentra en el intrervalo entre 10 y 50, o bien si es mayor de 50 hasta 100 
# o bien si es mayor de 100 o bien si es menor de diez
# '''

# x = random.randrange(121)

# if x < 10:
#     print("número inferior de 10 pero mayor a 0 ")
# elif x < 50:
#     print("número superior a 10 y menor de 50")
# elif x < 100:
#     print("número inferior a 100 y mayor a 50")
# else: 
#     print("es mayor de 100 hata 120")

# #Pares (7) 
# for n in range(10, 20): 
#     if n % 2 == 0:
#         print ({f"{n} es un número par"})
#     else:
#         pass

# # bucles: listar los números del 1 al 10
# for n in range(1, 11):
#     print (n)

# #series:
# total = 0 

# numeros = list(range(10, 21, 2))
# print (numeros)
# suma_number= (sum(numeros))
# print(suma_number)

# #creación de un palindromo: 

# palabra = input("ingresa la palabra que deseas evaluar: ")

# def es_palindromo(palabra: str):
#     palabra  = palabra.lower().replace(" ","") # recordar que con lower todo se vuelve minuscula, y la palabra o frase por medio de replace elimina espacios intermedios
#     if palabra == palabra[::-1]: # en este caso se  está usando el slicing o el agregar a una cadena dde texto, [inicio:fin:paso] permitiendo tomar porciones de una cadena
#         print(f"{palabra} es palindromo")
#     else:
#         print(f"{palabra} no es palidromo")
#     # cuando se pone un -1 en la parte de pasos del sliciing entonces la palabra o frase se voltea

# resultado = es_palindromo(palabra)
# print(resultado)

#generación de una progresión geometrica:
'''calcular cuantos granos de trigo tendríamos que utilizar si por cada 
casilla de un tablero de ajedrez pusiéramos un grano en la primera casilla, 
dos en la lsegunda, cuantro en la tercera
y asi doblando hasta la última. '''


