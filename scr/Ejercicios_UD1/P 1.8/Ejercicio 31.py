numero=int(input("Introduce un número:"))
while numero<1 or numero>10:
    print("Inténtalo otra vez! (1-10)")
    numero=int(input())
print("Correcto!")