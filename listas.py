
##Listas o Arrays-----------------------------------------------------------------------------

#Declaración de una lista. Sus posiciones son 0, 1, 2, 3, 
#etc. Empiezan siempre por 0
fruits = ["apple", "orange", "banana", "tomatos"]

print("Lista de frutas: ", fruits)
print("Un elemento de la lista: ", fruits[2])

#Cambiamos el valor de la posición 0 de la lista
fruits[0] = "manzanas"
#Añadimos un valor a la lista
fruits.append("piñas")
print("Lista de frutas modificada: ", fruits)

#Eliminamos el elemento de la posición 2 de la lista
fruits.pop(2)
print(fruits)

#Eliminamos el elemento 'orange' de la lista
fruits.remove("orange")
print(fruits)

nb_article = len(fruits)
print("Mi lista tiene", nb_article, "artículos")

#Insertamos un elemento en la posición deseada (3) de la lista
fruits.insert(3, "kiwi")
print("Lista con 'kiwi' insertado en la posición 3:", fruits)

#Convertir la lista en un string
cadena = str(fruits)
cadena += "patata"
#cadena = cadena+"patata"
print("La lista convertida en string con un añadido al final:", cadena)

#Bucle en listas. Para cada elemento de la lista:
for fruit in fruits:
    fruit += "2"
    print(fruit)
print(fruits)

#Seleccionar elementos
print(fruits[0:2])  #Elementos del 0 a 2 sin estar incluido el 2

#Mostrar la el elemento elegido por consola
pregunta = "¿Qué fruta quieres ver? Tenemos estas: " + str(fruits)
value_fruits = int(input(pregunta))

while value_fruits > 0:
    print(fruits[int(value_fruits)-1])
    value_fruits = int(input(pregunta))

#En caso de comparaciones, usar el '==' para comparar el valor y el tipo de una variable. Usar 
# el 'is' para comparar el valor y tipo de un objeto. El '=' no sirve en condicionales
a = "1"
b = 1

if int(a) == b:
    print("a y b tienen el mismo valor")