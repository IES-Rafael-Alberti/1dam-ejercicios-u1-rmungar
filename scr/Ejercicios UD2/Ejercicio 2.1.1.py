def PedirEdad():
    """Pedir la edad"""
    salir= False
    while not salir:
        entrada=input("Introduzca su edad: ")
        if entrada.isnumeric() and 0<int(entrada) <= 125:
            salir = True
        else:
            print("***Error*** edad introducida no válida")
    
    edad = int(entrada)
    return edad

def MayorEdad(edad):
    if edad >= 18:
        MayorEdad = True
    else:
        MayorEdad = False

def main():
    edad = PedirEdad()
    if MayorEdad(edad)==True:
        print("Eres mayor de edad")
    else:
        print("No eres mayor de edad")

if __name__ == "__main__":
    main()
