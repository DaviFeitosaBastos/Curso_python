#Converter Celsius para fahrenheit

celsius = float(input(f"Digite quantos graus deseja saber em fahrenheit: "))

fahrenheit = round((celsius * 1.8 + 32),2)

print(f"{celsius} Graus Celsius sao {fahrenheit} Fahrenheit")