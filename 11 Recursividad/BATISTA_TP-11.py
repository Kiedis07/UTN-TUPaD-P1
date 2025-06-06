#1) Crea una función recursiva que calcule el factorial de un número.
#Luego, utiliza esa función para calcular y 
#mostrar en pantalla el factorial de todos los números enteros
#entre 1 y el número que indique el usuario

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def mostrar_factoriales():
    num = int(input("Ingrese un número entero positivo: "))
    for i in range(1, num + 1):
        print(f"Factorial de {i}: {factorial(i)}")

#2 Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición indicada. 
# Posteriormente, muestra la serie completa hasta la posición que el usuario especifique.

def fibonacci(posicion):
    if posicion == 0:
        return 0
    elif posicion == 1:
        return 1
    else:
        return fibonacci(posicion - 1) + fibonacci(posicion - 2)

def mostrar_serie_fibonacci():
    n = int(input("Ingrese la posicin final: "))
    for i in range(n + 1):
        print(f"Posición {i}: {fibonacci(i)}")
        
#3 Crea una función recursiva que calcule la potencia de un número base elevado a un exponente, 
# utilizando la fórmula 𝑛𝑚= 𝑛∗𝑛(𝑚−1). Prueba esta función en un algoritmo general.

def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)

def probar_potencia():
    base = float(input("Ingrese la base: "))
    exponente = int(input("Ingrese el exponente ): "))
    print(f"{base} elevado a {exponente} es: {potencia(base, exponente)}")
    
#4 Crear una función recursiva en Python que reciba un número entero positivo en base decimal y devuelva su representación en binario como una cadena de texto.

def decimal_a_binario(n):
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    else:
        return decimal_a_binario(n // 2) + str(n % 2)

def probar_conversion():
    num = int(input("Ingrese un numero entero positivo: "))
    print(f"{num} en binario es: {decimal_a_binario(num)}")

#5 Implementá una función recursiva llamada es_palindromo(palabra) que reciba una cadena de texto #
# sin espacios ni tildes, y devuelva True si es un palíndromo o False si no lo es.

def es_palindrome(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindrome(palabra[1:-1])

def probar_palindromo():
    texto = input("Ingrese una palabra: ").lower()
    if es_palindrome(texto):
        print(f"'{texto}' es un palindromo")
    else:
        print(f"'{texto}' no es un palíndromo")
        
#6 Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un número entero positivo y devuelva la suma de todos sus dígitos

def suma_digitos(n):
    if n < 10:
        return n
    else:
        return n % 10 + suma_digitos(n // 10)

def probar_suma_digitos():
    num = int(input("Ingrese un número entero positivo: "))
    print(f"Suma de dígitos de {num}: {suma_digitos(num)}")
    
#7 Un niño está construyendo una pirámide con bloques. 
# En el nivel más bajo coloca n bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al último nivel con un solo bloque.
# 

def contar_bloques(n):
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1)

def probar_contar_bloques():
    niveles = int(input("Ingrese el número de bloques en el nivel base: "))
    print(f"Total de bloques necesarios: {contar_bloques(niveles)}")
    

#8) Escribí una función recursiva llamada contar_digito(numero, digito)
# que reciba un número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces aparece ese dígito dentro del número.

def contar_digito(numero, digito):
    if numero == 0:
        return 0
    ultimo_digito = numero % 10
    conteo = 1 if ultimo_digito == digito else 0
    return conteo + contar_digito(numero // 10, digito)

def probar_contar_digito():
    num = int(input("Ingrese un número entero positivo: "))
    dig = int(input("Ingrese un dígito a buscar (0-9): "))
    print(f"El dígito {dig} aparece {contar_digito(num, dig)} veces en {num}")
    
