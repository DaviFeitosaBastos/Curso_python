from time import sleep

#Definir 5 notas e fazer a media delas
while True:
    note_1_bimonthly = float(input(f"\nAssessment of first bimonthly: "))
    sleep(0.5)
    note_2_bimonthly = float(input(f"\nAssessment of second bimonthly: "))
    sleep(0.5)
    note_3_bimonthly = float(input(f"\nAssessment of third bimonthly: "))
    sleep(0.5)
    note_4_bimonthly = float(input(f"\nAssessment of four bimonthly: "))
    sleep(0.5)
    note_5_bimonthly = float(input(f"\nAssessment of five bimonthly: "))
    sleep(0.5)


    media = (note_1_bimonthly + note_2_bimonthly + note_3_bimonthly + note_4_bimonthly + note_5_bimonthly) / 5


    print(f"\nThe media of math is {round(media):.2f}")
    sleep(1)
    print(f"\nTry again...")
    sleep(1.5)
