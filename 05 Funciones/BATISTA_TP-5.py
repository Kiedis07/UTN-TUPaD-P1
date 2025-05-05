#Trabajo Practico 5- Arrays/Listas
#1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función range.
lista= list(range(1,100,4))
print(lista)
#2) Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el penúltimo.
lista_5=["Perro",7, 7.5, "Gato", 3.14]
print(lista_5[-2])
#3) Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por pantalla.
lista_vacia = []
lista_vacia.append("Programacion")
lista_vacia.append("Python")
lista_vacia.append("Ejercicios")
print(lista_vacia)
#4) Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”, respectivamente
#Imprimir la lista resultante por pantalla. ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el indexing con números negativos!
animales = ["perro", "gato", "conejo", "pez"]
animales[1] = "loro"
animales[-1] = "oso"
print(animales)
#5) Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza.
#Lo que sucede es lo siguiente: esta haciendo referencia a la variable numeros, se utiliza la funcion remove, y lo siguiente es ejecutar la funcion max sobre la lista numeros
#lo que hara que elija el mayor valor de la lista y lo elimine, luego se imprime la lista sin el mayor valor. En este caso el 22.

#6) Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por pantalla los dos primeros.
lista= list(range(10, 31, 5))
print (lista[:2])
#7) Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores cualesquiera.
autos = ["sedan", "polo", "suran", "gol"]
autos[1] = "Amarok"
autos[2]="tiguan"
print(autos)
#8) Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append directamente. Imprimir la lista resultante por pantalla.
lista=[]
lista.append(5*2)
lista.append(10*2)
lista.append(15*2)
print(lista)
#9) Dada la lista “compras”, cuyos elementos representan los productos comprados por diferentes clientes:
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
compras[2].append("jugo")
compras[1][1]="tallarines" 
compras[0].remove("pan")
print(compras)
#10) Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos:
lista_anidada = [[15],[True], [25.5, 57.9, 30.6], [False]]
print(lista_anidada)
