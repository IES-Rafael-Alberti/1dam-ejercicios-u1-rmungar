total=int(input("¿Cuántas notas vas a introducir? "))
while 1>total or total>100:
    print("Error - el número de notas debe ser un número entre 1 y 100")
    print("¿Cuántas notas va a introducir?")
    total = int(input())
print("Dame las",total,"notas del curso: ")
media = 0
cont = 1
while cont<=total:
    nota = int(input())
    media = media + nota
    cont = cont + 1
media = media/total
print("La media es: ",media)