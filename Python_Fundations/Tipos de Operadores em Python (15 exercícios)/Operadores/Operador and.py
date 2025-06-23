#VERIFICAR SE 2 NUMEROS SAO MAIORES QUE UM!
number = int(input(f"Digite numero 1: "))
number2 = int(input(f"Digite numero 2: "))
number3 = 10

relacao = number and number2 > number3

print(f"{number} e {number2} sao maiores que {number3}: {relacao}")
