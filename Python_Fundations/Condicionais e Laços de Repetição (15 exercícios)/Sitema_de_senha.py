from time import sleep

#Sistema simples que so permite a entrada se a senha estiver correta!
senha = []

def password_register():
    print(f"\nCadastre sua senha\n")
    new_pass = input(f"Digite aqui: ").strip().lower()
    senha.append(new_pass)

def login():
    while True:
        password = input(f"\nDigite sua senha: ")

        if password in senha:
            print(f"Acesso liberado!")   
            break 
        else:
            print(f"\nEssa senha não está cadastrada")
            sleep(1)
            password_register()
  
def main_menu():
    while True:
        print(f"""
=========================          
BEM VINDO AO NOSSO SITE
=========================
                    
1 - login
2 - exit              
""")
        sleep(0.5)
        try:
            option = int(input(f"Escolha uma opção: "))  
            if option in [1, 2]:
                return option 
            else:
                print(f"Opção incorreta")
        except ValueError:
            print(f"Erro, tente digitar 1, 2 ou 3") 
            sleep(1)
            continue
       
def main():
    while True:
        option = main_menu()
        
        if option == 1:
            login()
            break
        elif option == 2:
            print(f"Ok saindo")
            exit()

         
main()



