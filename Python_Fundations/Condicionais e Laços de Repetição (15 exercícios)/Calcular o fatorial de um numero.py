#Calcular o fatorial de um numero

numero = int(input(f"Digite um numero: "))

fatorial = 1

for i in range(1, numero + 1):
    fatorial *= i

print(f"O fatorial de {numero} é {fatorial}")