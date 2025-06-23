#VERIFICAR SE UM NUMERO É MAIOR QUE 5!
number = int(input(f"Digite numero 1: "))
number2 = int(input(f"Digite numero 2: "))
number3 = 10

relacao = (number > number3) or (number2 > number3)

print(f"{number} ou {number2} sao maiores que {number3}: {relacao}")
