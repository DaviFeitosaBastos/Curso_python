#Saber quais numeros sao multiplos de 3, 1 a 100

for i in range(1, 101):
    if i % 3 == 0:
        print(f"{i} é multiplo de 3")