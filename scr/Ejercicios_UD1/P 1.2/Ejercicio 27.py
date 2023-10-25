print("Nombre del producto:")
nombre= input()
print("Precio del producto:")
precio= float(input())
print("Nº de unidades:")
uds= int(input())
total=precio*uds
final= "{} tiene un precio unitario de {:>9.2f}, {03d} unidades tienen un precio de {:>11.2f}".format(nombre,precio,uds,total)
print(final)