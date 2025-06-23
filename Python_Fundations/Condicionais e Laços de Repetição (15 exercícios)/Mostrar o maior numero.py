#Mostrar o maior numero
while True:
    number1 = int(input(f"Digite um numero: "))
    number2 = int(input(f"Digite o segundo numero: "))

    if number1 > number2:
        print(f"{number1} é o numero maior")
    elif number2 > number1:
        print(f"{number2} é o numero maior")
