from time import sleep
from random import randint
from Tabuada_completa import math_table



while True:
    print(f"\n           <Bem-Vindo>           ")
    print(f"===================================")
    print(f"\nEscolha 1 opção abaixo", end ="\n")
    print(f"1 ➔ Mostrar um numero aleatorio")
    print(f"2 ➔ Mostrar a tabuada")
    print(f"3 ➔ Sair")
    sleep(0.2)
    escolhas = int(input(f"\nDigite aqui ➔ "))

    if escolhas in [1, 2, 3]:
        if escolhas == 1:      
            numero = randint(-999999999, 999999999)
            print(f"E o numero aleatorio foi o ➔ ({numero})\n")
            sleep(1)
        elif escolhas == 2:
            math_table()
            break
        elif escolhas == 3:
            exit()
    else:
        print(f"Invalid option!")
        sleep(1)
        