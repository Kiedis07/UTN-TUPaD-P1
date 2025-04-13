#1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
#(incluyendo ambos extremos), en orden creciente, mostrando un número por línea.
for numero in range(0, 101): 
    print(numero)

#2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
#dígitos que contiene
numero = abs(int(input("Ingrese un número entero: ")))  # abs() para manejar negativos
digitos = 0

while numero > 0:
    digitos += 1
    numero = numero // 10 

print("El número tiene", digitos, "dígitos.")

#3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
#dados por el usuario, excluyendo esos dos valores
inicio = int(input("Ingrese el primer número: "))
fin = int(input("Ingrese el segundo número: "))
suma = 0

for i in range(min(inicio, fin) + 1, max(inicio, fin)):
    suma += i

print("La suma es:", suma)

#4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
#secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
#un 0.
suma = 0
while True:
    numero = int(input("Ingrese un número (0 para terminar): "))
    if numero == 0:
        break
    suma += numero

print("Total acumulado:", suma)

# 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
#programa debe mostrar cuántos intentos fueron necesarios para acertar el número.
import random
numero_secreto = random.randint(0, 9)
intentos = 0

while True:
    intento = int(input("Adivina el número (0-9): "))
    intentos += 1
    if intento == numero_secreto:
        print("¡Correcto! Intentos:", intentos)
        break

#6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
#entre 0 y 100, en orden decreciente.
for numero in range(100, -1, -2):  
    print(numero)
    
#7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
#número entero positivo indicado por el usuario.
n = int(input("Ingrese un número positivo: "))
suma = 0

for i in range(n + 1):  # Incluye el número ingresado
    suma += i

print("La suma es:", suma)

#8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
#programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
#negativos y cuántos son positivos

pares = impares = positivos = negativos = 0

for _ in range(100): 
    num = int(input("Ingrese un número: "))
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1
    if num > 0:
        positivos += 1
    elif num < 0:
        negativos += 1

print("Pares:", pares, "| Impares:", impares)
print("Positivos:", positivos, "| Negativos:", negativos)

#9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
#media de esos valores
suma = 0
for _ in range(100):  # Cambiar a 5 para pruebas
    num = int(input("Ingrese un número: "))
    suma += num

media = suma / 100  # Ajustar el divisor si se prueba con menos números
print("Media:", media)

#10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
#usuario.
numero = int(input("Ingrese un número: "))
invertido = 0

while numero > 0:
    digito = numero % 10  
    invertido = invertido * 10 + digito
    numero = numero // 10  
print("Número invertido:", invertido)