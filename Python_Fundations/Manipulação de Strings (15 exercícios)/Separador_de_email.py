email = input(f"Digite seu email: ")

email_repartido = email.split('@')

usuario = email_repartido[0]
dominio = email_repartido[1]

print(f"O usuario do email é {usuario} e o dominio {dominio}")