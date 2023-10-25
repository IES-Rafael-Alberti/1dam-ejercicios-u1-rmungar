num=3
numT=int(input("Dime cuantos numeros debe tener la serie"))
cont=1
while (cont<=numT):
    print(num, end=" ")
    if (cont<numT):
        print(end=" ")
    num = num+3
    cont=cont+1