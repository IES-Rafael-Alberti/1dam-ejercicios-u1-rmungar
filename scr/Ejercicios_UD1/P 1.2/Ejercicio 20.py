print("Dame un número de teléfono con el siguiente formato: +34-XXXXXXXXX-YY")
telefono=input()
sep_tel = telefono.split("-")
print(sep_tel[1])