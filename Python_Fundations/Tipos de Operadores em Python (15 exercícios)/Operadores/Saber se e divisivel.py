from time import sleep

#Saber se o segundo numero é divisivel pelo primeiro
print(f"\nSaber se o segundo numero é divisivel pelo primeiro", end ="\n\n")
sleep(0.5)
number1 = int(input(f"Digite o numero base: "))
print(f"\nAgora digite o numero que deseja saber\nse é divisivel por {number1} ou nao", end ="\n\n")
sleep(0.5)
number2 = int(input(f"Numero desejado: "))

result = number2 % number1 == 0

print(f"\nO {number2} é divisivel por {number1}?: > {result}")