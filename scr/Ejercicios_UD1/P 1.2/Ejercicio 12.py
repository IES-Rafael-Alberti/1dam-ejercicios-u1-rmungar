print("Dime tu peso:")
print("Dime tu altura:")
peso=float(input())
altura=float(input())
altura/=100
imc = (peso/(altura**2))
print( "Tu índice de masa corporal es: ",round(imc,2))