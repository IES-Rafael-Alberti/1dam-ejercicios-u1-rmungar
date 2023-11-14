def tempt():
    celsius = float(input("Ingresa la temperatura en grados Celsius: "))
    fahrenheit = (celsius * 9/5) + 32 
    return fahrenheit
print("Serían",tempt(),"grados fahrenheit")
