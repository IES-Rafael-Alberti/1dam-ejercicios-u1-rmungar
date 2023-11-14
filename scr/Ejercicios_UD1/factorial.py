def factorial(num : int):
    if num<0:
        return -1

    if num <= 1:
        return 1
    
    total = 1
    while num > 0:
        total *= num
        num -= 1
    return total

numero=int(input("Dame un número: "))
print(str(numero) + "! => " )
while numero>1:
    print(numero, end="* ")
    numero=numero-1
print (str(factorial(numero)))
