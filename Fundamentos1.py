def nuevoTema(tema):
    print("\n====", tema, "====\n")

nuevoTema("Operadores aritmeticos")
print("Operador division entera(10//3):",10//3)
print("Operador potencia (5**3):",5**3)#
print("\n")
nuevoTema("Operadores logicos")
print("Operador and (True and False):", True and False)#True and False empieza en mayuscula
print("\n")
#Actividad: Imprimir la tabla de verdad de los operadores logicos.
print("Operador and (True and True):", True and True)
print("Operador and (True and False):", True and False)
print("Operador and (False and True):", False and True)
print("Operador and (False and False):", False and False)
print("\n")
print("Operador not (True):",  not True)
print("Operador not (False):",  not False)
print("\n")
print("Operador or (True True):", True or True)
print("Operador or (True False):", True or False)
print("Operador or (False True):", False or True)
print("Operador or (False False):", False or False)
print("\n")
nuevoTema("Operadores de comparacion")
print("2==3", 2 == 3)
print("2<3", 2 < 3)
print("2>3", 2 > 3)
print("2<=3", 2 <= 3)
print("2>=3",2 >= 3)
print("2!=3", 2 != 3)
print("\n")
nuevoTema("Variables")
variable1 = 10
variable2 = 6.2456
variable3 = "Juancho"
dosPalabras = "Hola"
dos_palabras = "Hello"
print(variable1, variable2, variable3, dosPalabras, dos_palabras)
a, b, c = 10, 5.16, "Palabra"
print(a, b, c)

nuevoTema("Enteros")
w = 1353
x = 99999999999
y = -256
z = 0b00110011
h = 0xffa


print(w, type(w))
print(x, type(x))
print(y, type(y))
print(z, type(z))
print(h, type(h))

nuevoTema("Flotantes")
x = 1297.50
print(x, type(x))
y = 0.5345345
print(y, type(y))

nuevoTema("Numeros complejos")
x = -46j
y = 12 + 45j
z = 2j
print(x, type(x))
print(y, type(y))
print(z, type(z))

nuevoTema("Booleanos")
lis = [8]
print(lis, "es", bool(lis))
t = ()
print(t, "es", bool(t))
new = "Hello"
print(new, "es", bool(new))
num = 99
print(num, "es", bool(num))
comp = 1 + 0j
print(comp, "es", bool(comp))
val = None#es el equivalente a NULL
print(val, "es", bool(val))

nuevoTema("Listas")#en python no hay arreglos
a = [10, 20.5, "Lista python"]
print(a)
print(a[1])
a[0] = "Nuevo dato"
print(a)

nuevoTema("Tuplas")#Son como las listas pero no se puede cambiar los valores una vez creada
#es mas rapido que las listas
t = (25, 10.5, "Tupla", 1+20j)
print(t)
print(t[2])
print("t[0:2]:", t[0:2])# rango
#t[1] = 12 operacion no valida en tuplas
 

nuevoTema("Conjuntos")
t = {50, 20, 30, 40, 10, 50}
print("Conjunto t=",t, type(t))

nuevoTema("Diccionario")
d = {1:"Valor1", "Valor2":2j}
print(d, type(d))
print("d[Valor2]:",d["Valor2"])

nuevoTema("Cadenas")
cadena1 = "Cadena con comillas dobles"
cadena2 = 'Cadena con comillas simples'

print(cadena1, type(cadena1))
print(cadena2, type(cadena2))

cadenaMultilinea = '''Esta es una cadena de 
varias lineas    con     tabuladores y 
saltos
de 
linea'''

print(cadenaMultilinea)
print("Segmentacion de cadenas")
print(cadena1[5:11])
print(cadena1[:5])
print(cadena1[7:])
print(cadena1[-8:-1])
print(cadena1[0:18:1])
print(cadena1[0:18:2])
print(cadena1[0:18:3])

cadena1 = "Hola"
cadena4 = (cadena1 + " ") * 5
print(cadena4)
cadena5 = cadena4.upper()
print(cadena5)

print("Hola")




