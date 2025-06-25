palavra = input(f"Digite uma palavra: ").lower()

vogal = ['a','e','i','o','u']
contador = 0

for letra in palavra:
    if letra in vogal:
        contador += 1
        
print(f"{contador}")