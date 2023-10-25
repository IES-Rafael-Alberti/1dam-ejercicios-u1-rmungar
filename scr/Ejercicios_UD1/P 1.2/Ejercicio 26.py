print("Dime los productos de la compra separados por comas")
list=input()
print("Dime el numero de elementos de la lista")
numero=int(input())
lista=list.split(",")
for i in range(numero):
    prod=lista[i]
    print(prod)
