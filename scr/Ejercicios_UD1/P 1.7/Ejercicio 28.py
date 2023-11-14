#Inicio
# Escribe: "Dame 2 números"
# Lee n1,n1
# si  (n1=n2):
#   Escribe: "Los números no pueden ser iguales"
# sino:
#   si (n1<n2):
#       Escribe: "El número menor es el n1 y entre ellos existen (n2-n1) números enteros."
#   sino 
#       Escribe: "El número menor es el n2 y entre ellos existen (n1-n2) numeros enteros."
#Fin

n1 = int(input("Dame un número entero:"))
n2 = int(input("Dame otro número entero:"))
resta1=(n1-n2)
resta2=(n2-n1)
if n1==n2:
    print("Los números no pueden ser iguales")
else:
    if n1<n2:
        print("El número menor es el",n1,"y entre ellos existen",resta2,"números enteros")
    else:
        print("El número menor es el",n2,"y entre ellos existen",resta1,"números enteros")
        

