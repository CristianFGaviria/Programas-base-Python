input(
    "Bienvenido al Juego piedra papel o tijera, Recuerda solo puedes seleccionar alguna de estas 3 opciones Ingresa tu opcion: ")

import random

options = ("piedra", "papel", "tijera")

computer_wins = 0
user_wins = 0
rounds = 1

while True:

    print("*" * 10)
    print("Round", rounds)
    print("*" * 10)

    print("computer_wins", computer_wins)
    print("user_wins", user_wins)

    user_option = input("piedra, papel o tijera: ")
    user_option = user_option.lower()

    rounds += 1

    if not user_option in options:
        print("Esa opcion no es valida")
        continue

    pc_option = random.choice(options)

    print("User option =>", user_option)
    print("Computer option =>", pc_option)

    if user_option == pc_option:
        print("EMPATE!! ")

    elif user_option == "piedra":
        if pc_option == "tijera":
            print("piedra le gana a tijera ")
            print("GANASTE!! ")
            user_wins += 1

        else:
            print("papel gana a piedra")
            print("PERDISTE!! :( ")
            computer_wins += 1

    elif user_option == "papel":
        if pc_option == "piedra":
            print("Papel gana a piedra")
            print("GANASTE!! ")
            user_wins += 1

        else:
            print("tijera gana a papel")
            print("PERDISTE!! :( ")
            computer_wins += 1

    elif user_option == "tijera":
        if pc_option == "papel":
            print("tijera gana a paperl")
            print("GANASTE!! ")
            user_wins += 1
        else:
            print("piedra gana a tijera")
            print("PERDISTE!! :( ")
            computer_wins += 1

    if computer_wins == 2:
        print("El Ganador absoluto es la computadora")
        break

    if user_wins == 2:
        print("El Ganador absoluto eres tu!!!!")
        break