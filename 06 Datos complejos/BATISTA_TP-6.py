#1) Dado el diccionario precios_frutas

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
precios_frutas['Naranja'] = 1200  
precios_frutas['Manzana'] = 1500  
precios_frutas['Pera'] = 2300    
print("Diccionario :", precios_frutas)


# 2)- precios_frutas atualizado
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700 
precios_frutas['Melón'] = 2800   
print("Diccionario actualizado:", precios_frutas)

#3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
#desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los
#precios.

lista_frutas = list(precios_frutas.keys()) 
print("Lista de frutas:", lista_frutas)