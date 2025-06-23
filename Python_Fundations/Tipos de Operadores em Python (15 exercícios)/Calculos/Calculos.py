from time import sleep

#Some dois numeros
def soma_dois_numeros():
    
    print(f"Soma de dois numeros\n")
    number = float(input(f"Digite um numero: "))
    sleep(0.5)
    number2 = float(input(f"Digite outro numero: "))
    sleep(0.5)

    result = number + number2

    print(f"A soma de {number} + {number2} = >> {result}", end ="\n\n")

#Multiplique dois numeros
def multiplaçao():

    print(f"Multiplique de dois numeros\n")
    number = float(input(f"Digite um numero: "))
    sleep(0.5)
    number2 = float(input(f"Digite outro numero: "))
    sleep(0.5)

    result = number * number2

    print(f"A multiplicaçao de {number} * {number2} = >> {result}", end ="\n\n")

#Subtraçao
def subtracao():

    print(f"Subtraia dois numeros\n")
    number = float(input(f"Digite um numero: "))
    sleep(0.5)
    number2 = float(input(f"Digite outro numero: "))
    sleep(0.5)

    result = number - number2

    print(f"A subtraçao de {number} - {number2} = >> {result}", end ="\n\n")

#Divisao
def divisao():

    print(f"Divida dois numeros\n")
    number = float(input(f"Digite um numero: "))
    sleep(0.5)
    number2 = float(input(f"Digite outro numero: "))
    sleep(0.5)

    result = number - number2

    print(f"A divisao de {number} / {number2} = >> {result}", end ="\n\n")

#Potenciaçao
def potencia():

    print(f"Digite um numero e a sua potenciaçao\n")
    number = float(input(f"Digite um numero: "))
    sleep(0.5)
    number2 = float(input(f"Digite outro numero: "))
    sleep(0.5)

    result = number ** number2

    print(f" {number2} sobre {number} = >> {result}", end ="\n\n")

#Resto da divisao
def resto_divisao():

    print(f"Digite um numero e a sua potenciaçao\n")
    number = float(input(f"Digite um numero: "))
    sleep(0.5)
    number2 = float(input(f"Digite outro numero: "))
    sleep(0.5)

    result = number % number2

    print(f"O resto de {number} dividido por {number2} = >> {result}", end ="\n\n")

#Executador das funções
def main():
    soma_dois_numeros()
    multiplaçao()
    subtracao()
    divisao()
    potencia()
    resto_divisao()


main()





