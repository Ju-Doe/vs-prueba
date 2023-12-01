# -*- coding: utf-8 -*-

##Variables y sus propiedades--------------------------------------------------------------------------

##Declaración y print
name = "Sanfe"  #string
age = 25    #int
age = 12
number = age + 24
height = 1.81   #float
print("Hello, my name is" , name, number)

PI = 3.14
name2 = "MOVIL"
name3 = name2[0]
longitud = len(name2)
minusculas = name2.lower
mayusculas = name2.upper
variable_nula = None
negative = -15
absolute = abs(number)

print(absolute)
print(type(name))
print(type(age))
print(type(height))

print("Hola " + name + ", ¿tu edad es 25?")
print("Mi edad es " + str(number))  #No se puede concatenar un string y un número, a menos que se transforme éste a string con str()
print("--------------------------------------------------")

##Operadores
x = 5
y = 4
suma = x + y
mult = x * y
resta = x - y
div = x/y
modulo = x%y    #El resto de una división

print(suma)
print(mult)
print(resta)
print(div)
print(modulo)

print(x>y)
print(x,y)

#Condicional
if y<x:
    print("Esta condición es verdadera")


