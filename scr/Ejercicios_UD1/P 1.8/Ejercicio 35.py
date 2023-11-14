print("Escribe 2 números:")
num1=int(input())
num2=int(input())
op=int(input("Introduce una opción (1 = Suma / 2 = Resta / 3 = Multiplicación / 4 = División):"))
if (op<1 or op>4):
    print("Error - No es una opcion correcta")
else:
    if op==1:
        print(num1,"+",num2,"=",num1+num2)
    elif op==2:
        print(num1,"-",num2,"=",num1-num2)
    elif op==3:
        print(num1,"*",num2,"=",num1*num2)
    else:
        if num2==0:
            print("La división por cero no es posible")
        else:
            print(num1,"/",num2,"=",num1/num2)

