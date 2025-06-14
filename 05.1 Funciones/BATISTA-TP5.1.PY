#1pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el
#1Crear una función llamada imprimir_hola_mundo que imprima por
#1programa principal.

def imprimir_hola_mundo():
    print("Hola Mundo!")

imprimir_hola_mundo()

#2 Crear una función llamada saludar_usuario(nombre) que reciba
#como parámetro un nombre y devuelva un saludo personalizado.
#Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver:
#“#Hola Marcos!”. Llamar a esta función desde el programa
#principal solicitando el nombre al usuario.#

def saludar_usuario(nombre):
    return f"Hola {nombre}!"

nombre_usuario = input("Por favor, ingresa tu nombre: ")
print(saludar_usuario(nombre_usuario))

#3. Crear una función llamada informacion_personal(nombre, apellido,
#edad, residencia) que reciba cuatro parámetros e imprima: “Soy
#[nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir
#los datos al usuario y llamar a esta función con los valores ingresados.

def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

nombre = input("Ingresa tu nombre: ")
apellido = input("Ingresa tu apellido: ")
edad = input("Ingresa tu edad: ")
residencia = input("Ingresa tu lugar de residencia: ")

informacion_personal(nombre, apellido, edad, residencia)

#4 Crear dos funciones: calcular_area_circulo(radio) que reciba el radio
#como parámetro y devuelva el área del círculo. calcular_perimetro_
#circulo(radio) que reciba el radio como parámetro y devuelva
#el perímetro del círculo. Solicitar el radio al usuario y llamar ambas
#funciones para mostrar los resultados.#

import math

def calcular_area_circulo(radio):
    return math.pi * radio ** 2

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

radio = float(input("Ingresa el radio del círculo: "))

print(f"area del círculo: {calcular_area_circulo(radio):.2f}")
print(f"Perimetro del círculo: {calcular_perimetro_circulo(radio):.2f}")

#5 #Crear una función llamada segundos_a_horas(segundos) que reciba
#una cantidad de segundos como parámetro y devuelva la cantidad
#de horas correspondientes. Solicitar al usuario los segundos y mostrar
#el resultado usando esta función

def segundos_a_horas(segundos):
    return segundos / 3600

segundos = float(input("Ingresa la cantidad de segundos: "))

print(f"{segundos} segundos equivalen a {segundos_a_horas(segundos):.2f} horas")

#6 Crear una función llamada tabla_multiplicar(numero) que reciba un
#número como parámetro y imprima la tabla de multiplicar de ese
#número del 1 al 10. Pedir al usuario el número y llamar a la función.#

def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

numero = int(input("Ingresa un nmero para ver su tabla de multiplicar: "))

tabla_multiplicar(numero)

#7 Crear una función llamada operaciones_basicas(a, b) que reciba
#d#os números como parámetros y devuelva una tupla con el resultado
#de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados
#de forma clara.#

def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else "No se puede dividir por cero"
    return (suma, resta, multiplicacion, division)

num1 = float(input("Ingresa el primer numero: "))
num2 = float(input("Ingresa el segundo numero: "))

resultados = operaciones_basicas(num1, num2)

print(f"Suma: {resultados[0]}")
print(f"Resta: {resultados[1]}")
print(f"Multiplicación: {resultados[2]}")
print(f"División: {resultados[3]}")

#8 Crear una función llamada calcular_imc(peso, altura) que reciba el
#peso en kilogramos y la altura en metros, y devuelva el índice de
#masa corporal (IMC). Solicitar al usuario los datos y llamar a la función
#para mostrar el resultado con dos decimales.#

def calcular_imc(peso, altura):
    return peso / (altura ** 2)

peso = float(input("Ingresa tu peso en kg: "))
altura = float(input("Ingresa tu altura en metros: "))

print(f"Tu IMC es: {calcular_imc(peso, altura):.2f}")

#9 Crear una función llamada celsius_a_fahrenheit(celsius) que reciba
#una temperatura en grados Celsius y devuelva su equivalente en
#Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el
#resultado usando la función.#

def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

celsius = float(input("Ingresa la temperatura en grados Celsius: "))

print(f"{celsius}°C equivalen a {celsius_a_fahrenheit(celsius):.2f}°F")

#10 Crear una función llamada calcular_promedio(a, b, c) que reciba
#tres números como parámetros y devuelva el promedio de ellos.
#S#olicitar los números al usuario y mostrar el resultado usando esta
#función.#

def calcular_promedio(a, b, c):
    return (a + b + c) / 3

num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))
num3 = float(input("Ingresa el tercer número: "))

print(f"El promedio es: {calcular_promedio(num1, num2, num3):.2f}")