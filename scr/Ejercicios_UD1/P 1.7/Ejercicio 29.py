# Escribe: "Dame un nombre y una edad"
# Lee nombre, edad
# si longitud(nombre)=0:
#   nombre= "DESCONOCIDO"
# si edad<0 o 125<edad:
#   Escribe: "Error"
#   Escribe: "Vuelve a escribir tu edad:"
#   edad=edad
# sino
#   Escribe: "Te llamas (nombre) y tienes (edad) años, te quedan aun (125-edad) años por cumplir"
#
nombre = input("Dame un nombre:")
edad = int(input("Dime la edad:"))
if len(nombre)==0:
    nombre = "DESCONOCIDO"
else:
    nombre = nombre
while edad<0 or 125<edad:
    print("ERROR")
    edad= int(input(("Vuelve a escribir tu edad:")))
print("Te llamas",nombre,"y tienes",edad,"años, te quedan aún",(125-edad),"años por cumplir")   