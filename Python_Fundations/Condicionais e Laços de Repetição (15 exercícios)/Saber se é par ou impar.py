#Saber se impar ou par
while True:
    number1 = int(input(f"Digite o primeiro numero: "))

    resultado = number1 % 2 

    if resultado == 0:
        print(f"{number1} é par!")
    else:
        print(f"{number1} é Impar!")
        pass
