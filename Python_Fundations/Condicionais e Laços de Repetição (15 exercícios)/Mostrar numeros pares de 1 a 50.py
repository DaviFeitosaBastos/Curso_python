from time import sleep

#Mostrar todos os numero pares de 1 a 50
for i in range(1, 50 +1):
    if i % 2 == 0:
        print(f"{i} é par")
        sleep(0.2)
