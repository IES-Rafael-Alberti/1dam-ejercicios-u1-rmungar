# Escribe: "Dame un número inicial, un incremento y un número final"
# lee numI, inc, numF
# crea una lista desde numI hasta numF
# Escribe lista  
#
numI = int(input("Dame un número inicial:"))
inc = int(input("Dame un incremento:"))
numF = int(input("Dame un número final:"))
contador=1
serie= ("Serie=>")
if inc==0 or numF==0:
    print("ERROR")
else:
    while (contador <= numF):
        numI=numI + inc
        contador += contador
        if (contador<numF-1):
            serie=str(str(serie)+str(inc)+"..")
        else:
            if (contador==numF):
                serie=str(str(serie)+str(numI))
            else:
                serie=str(str(serie)+str(numI)+"-")
print(serie)
