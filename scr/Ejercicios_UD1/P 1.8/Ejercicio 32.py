num1=int(input("Introduce un número:"))
num2=int(input("Introduce otro:"))
if num1>= num2:
    numIni=num2
    numFin=num1
else:
    numIni=num1
    numFin=num2
for i in range(numIni, numFin+1):
    if (i==numFin):
        print(i, end="")
    else:
        print(i,end="-")
