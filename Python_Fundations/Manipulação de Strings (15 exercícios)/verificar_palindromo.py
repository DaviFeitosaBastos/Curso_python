# Verificar palindromo

frase = input(f"Escreva um palindromo: ").lower().strip()

if frase[::-1] == frase:
    print(f"({frase}) é um palindromo")
else:
    print(f"Não é um palindromo")