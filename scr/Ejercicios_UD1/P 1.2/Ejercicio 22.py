
print("Dime una frase y una vocal")
frase=input()
vocal=input()
v=vocal.capitalize()
frase.find(vocal)
frase=frase.replace(vocal,v)
print(frase)
