from time import sleep

#Sistema simples que so permite a entrada se a senha estiver correta!
senha = []

def password_register():
    print(f"\nCadastre sua senha\n")
    new_pass = input(f"Digite aqui: ").strip().lower()
    senha.append(new_pass)

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
        except ValueError:
            print(f"Erro, tente digitar 1, 2 ou 3") 
            sleep(1)
            continue
        return option

def main():
    while True:
        option = main_menu()
        if option == 1:
            type_pass = input(f"\nDigite sua senha aqui: ")
            
            if type_pass in senha :
                print(f"\nAcesso liberado")
                break
          
            else:
                print(f"\nSenha nao cadastrada.")
                password_register()
                continue
        elif option == 2:
            exit()
         
main()



