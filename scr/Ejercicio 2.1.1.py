edad=int(input("Dime tu edad: "))

def MayorEdad():
    if edad >= 18:
        return "Eres mayor de edad"
    else:
        return "Eres menor de edad"
print(MayorEdad())