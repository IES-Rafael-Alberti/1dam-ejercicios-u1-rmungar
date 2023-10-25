print("Dame 3 números")
num1=int(input())
num2=int(input())
num3=int(input())
if (num1<num2 and num1<num3):
    if (num2<num3):
        print(num1,"es menor que",num2,"que es menor que",num3)
    else:
        print(num1,"es menor que",num3,"que es menor que",num2)
else:
    if (num2<num1 and num2<num3):
        if (num1<num3):
            print(num2,"es menor que",num1,"que es menor que",num3)
        else:
            print(num2,"es menor que",num3,"que es menor que",num1)
    else:
        if (num3<num1 and num3<num2):
            if (num1<num2):
                print(num3,"es menor que",num1,"que es menor que",num2)
            else:
                print(num3,"es menor que",num2,"que es menor que",num1)
