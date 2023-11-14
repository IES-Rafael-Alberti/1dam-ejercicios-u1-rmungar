
def total():
    precio_sin_iva = float(input("Ingresa el precio: "))
    porcentaje_iva = float(input("Ingresa el porcentajede IVA: "))
    precio_final = precio_sin_iva * (1 + porcentaje_iva / 100)
    print(precio_final)
