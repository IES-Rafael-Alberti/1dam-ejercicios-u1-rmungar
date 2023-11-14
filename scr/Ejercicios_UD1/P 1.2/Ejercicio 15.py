print("Ingrese su capital: ")
capital=float(input())
n=0
for i in range (3):
    capital = capital*(1+0.04)
    n=n+1
    print("en el ", n, "año, el capital sería: ", round(capital,2))
