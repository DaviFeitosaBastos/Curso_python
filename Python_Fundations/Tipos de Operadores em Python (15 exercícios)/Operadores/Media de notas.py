from random import randint

#Calcular a media
number1 = randint(1, 10)
number2 = randint(1, 10)
number3 = randint(1, 10)

media = (number1 + number2 + number3) / 3

print(f"A media das notas, [{number1}, {number2}, {number3}] é de {media}")