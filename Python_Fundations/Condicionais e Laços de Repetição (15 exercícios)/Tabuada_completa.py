from time import sleep


def math_table():
    on = True
    while on:
        try:
            number = int(input(f"\nChoose which math table you want to know: "))      
            for i in range(1, 11):
                result = number * i
                print(f"[{number} * {i} = {result}]")
                sleep(0.2)
            print(f"Would you like to choose another?")
            while True:
                try:
                    returning = int(input(f"type 1(yes) or 2(not): "))
                    match returning:
                        case 1:
                            print(f"Returning...")
                            print(f"==========================================]")
                            sleep(1)
                            break
                        case 2:
                            print(f"OK exiting Tables")
                            on = False
                            break    
                        case _:
                            print(f"Type only 1 or 2..\n")
                            sleep(0.5)       
                except ValueError:
                    print(f"\nError try to type a number to know the table!\n")
                    sleep(1)
        except ValueError:
            print(f"\nError try to type a number to know the table!")
            sleep(1)