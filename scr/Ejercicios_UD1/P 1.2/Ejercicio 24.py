print("Dime el precio:")
precio = (input())
precio_sep = precio.split(",")
print("Nº de euros:",len(precio_sep[0]), "y nº de centimos:",len(precio_sep[1]))
