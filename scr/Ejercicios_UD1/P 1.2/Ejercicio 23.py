print("Dame un correo electrónico: ")
correo=input()
correo_nuevo=correo.split("@")
nomb_correo=correo_nuevo[0]
print(f"{nomb_correo}@ceu.es")