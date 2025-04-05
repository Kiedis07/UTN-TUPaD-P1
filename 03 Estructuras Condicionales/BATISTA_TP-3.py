#Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
#deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.
edad= int(input("Ingrese su edad"))
if edad >= 18:
    print("Es mayor de edad")
    
#2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá mostrar por pantalla un mensaje que diga “Aprobado”;
# en caso contrario deberá mostrar el mensaje “Desaprobado”.
nota= int(input("Ingrese su nota"))
if nota >= 6:
    print ("Aprobado")
else:
    print ("Desaprobado")

#3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso contrario, imprimir por pantalla "Por favor, ingrese un número par".
#Nota: investigar el uso del operador de módulo (%) en Python para evaluar si un número es par o impar.
numero = int(input("Ingrese un número par: "))

if numero % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")

#4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las siguientes categorías pertenece:
#Niño/a: menor de 12 años. ● Adolescente: mayor o igual que 12 años y menor que 18 años. ● 
#Adulto/a joven: mayor o igual que 18 años y menor que 30 años. ● Adulto/a: mayor o igual que 30 años.
edad = int(input("Ingrese su edad: "))

if edad < 12:
    print("Pertenece a la categoría Niños")
elif 12 <= edad < 18:
    print("Pertenece a la categoría Adolescente")
elif 18 <= edad < 30:
    print("Pertenece a la categoría Adulto joven")
else:
    print("Pertenece a la categoría Adulto")

print("Gracias. Chau")

#5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres (incluyendo 8 y 14).
# Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en pantalla el mensaje 
# "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". 
# Nota: investigue el uso de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal como una lista o un string.
contraseña = input("Ingrese una contraseña (8-14 caracteres): ")

if 8 <= len(contraseña) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")
    
#6) El paquete statistics de python contiene funciones que permiten tomar una lista de números y calcular la moda, la mediana y la media de dichos números
import random
from statistics import mode, median, mean

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)

# Determinar el tipo de sesgo
if media > mediana and mediana > moda:
    sesgo = "Sesgo positivo (a la derecha)"
elif media < mediana and mediana < moda:
    sesgo = "Sesgo negativo (a la izquierda)"
else:
    sesgo = "Sin sesgo (distribución normal)"

print(f"Media: {media:.2f}")
print(f"Mediana: {mediana}")
print(f"Moda: {moda}")
print(f"\nConclusión: {sesgo}")

#7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado termina con vocal, 
# añadir un signo de exclamación al final e imprimir el string resultante por pantalla;
# en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla.
entrada = input("Ingrese una frase o palabra: ")

if len(entrada) > 0 and (entrada[-1] == 'a' or entrada[-1] == 'e' or entrada[-1] == 'i' or entrada[-1] == 'o' or entrada[-1] == 'u'):
    print(f"{entrada}!")
else:
    print(entrada)

#8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 dependiendo de la opción que desee:
#1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
#2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
#3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
nombre = input ("Ingrese su nombre")
opcion= input ("Ingrese la opcion para transformar su nombre a: 1 MAYUSCULA, 2 minuscula, 3 Titulo")

if opcion == "1":
        print (nombre.upper())
elif opcion == "2":
    print (nombre.lower())
elif opcion == "3":
    print (nombre.title())
else:
    print ("Ingrese una opcion valida")
    
#9) Escribir un programa que pida al usuario la magnitud de un terremoto, 
# clasifique la magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado por pantalla:
#Menor que 3: "Muy leve" (imperceptible).
#● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
#● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero generalmente no causa daños).
#● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras débiles).
#● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
#● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).
magnitud= float(input("Ingrese la magnitud"))
if magnitud < 3:
    print("Muy leve")
elif magnitud >= 3 and magnitud < 4:
    print ("Ligeramente perceptible")
elif magnitud >= 4 and magnitud < 5:
    print ("Moderado")
elif magnitud >= 5 and magnitud < 6:
    print ("Fuerte")
elif magnitud >= 6 and magnitud < 7:
    print ("Muy fuerte")
elif magnitud >= 7:
    print ("Extremo")
else:
    print ( "Ingrese un valor valido")
    
#10) Utilizando la información aportada en la siguiente tabla sobre las estaciones del año
hemisferio = input("Ingrese el hemisferio: N para norte, S para sur: ").upper()
mes = int(input("Ingresa el mes 1 al 12: "))
dia = int(input("Ingresa el día 1 al 31: "))

if hemisferio == "N":
    if (mes == 12 and dia >= 21) or (mes == 1) or (mes == 2) or (mes == 3 and dia <= 20):
        estacion = "Invierno"
    elif (mes == 3 and dia >= 21) or (mes == 4) or (mes == 5) or (mes == 6 and dia <= 20):
        estacion = "Primavera"
    elif (mes == 6 and dia >= 21) or (mes == 7) or (mes == 8) or (mes == 9 and dia <= 20):
        estacion = "Verano"
    else:
        estacion = "Otoño"
elif hemisferio == "S":
    if (mes == 12 and dia >= 21) or (mes == 1) or (mes == 2) or (mes == 3 and dia <= 20):
        estacion = "Verano"
    elif (mes == 3 and dia >= 21) or (mes == 4) or (mes == 5) or (mes == 6 and dia <= 20):
        estacion = "Otoño"
    elif (mes == 6 and dia >= 21) or (mes == 7) or (mes == 8) or (mes == 9 and dia <= 20):
        estacion = "Invierno"
    else:
        estacion = "Primavera"
else:
    estacion = "Hemisferio no válido"

print(f"Estacion actual: {estacion}")