import random
import os
import time


def main():

    mozne_akce = ["Kámen", "Nužky", "Papír"]
    Ty = 0
    Pc = 0

    while Ty < 5 and Pc < 5:
        user_action = input("Zadej Kamen/Nužky/Papír: ")
        computer_action = random.choice(mozne_akce)
        print(
            f"\nTvoje volba {user_action}, Volba počítače {computer_action}.\n")

        if user_action == computer_action:
            print(f"Oba jste vybrali stejný znak {user_action}. Je to remíza!")
        elif user_action == "Kámen" or "kámen" or "Kamen" or "kamen":
            if computer_action == "Nužky":
                print("Kámen tupí nužky! Vyhrál jsi.")
                Ty += 1
            else:
                print("Papír balí kámen! Prohrál jsi!.")
                Pc += 1
        elif user_action == "Papír" or "papír" or "Papir" or "papir":
            if computer_action == "Kámen":
                print("Papír balí kámen! Vyhrál jsi!")
                Ty += 1
            else:
                print("Nužky stříhají papír! Prohrál jsi.")
                Pc += 1
        elif user_action == "Nužky" or "nužky" or "Nuzky" or "nuzky":
            if computer_action == "Papír":
                print("Nužky stříhají papír! Vyhrál jsi.!")
                Ty += 1
            else:
                print("Kámen tupí nužky! Prohrál jsi.")
                Pc += 1
        else:
            print("Neplatná hodnota")
            continue
        print(f"\nTvoje body {Ty}, Body Počítače {Pc}.\n")

    if Pc < Ty:
        print("Máš víc bodů než počítač, vyhrál jsi!")
    elif Ty < Pc:
        print("Máš méně bodů než počítač, prohrál jsi!")
    time.sleep(3)
    os.system("cls")


if __name__ == '__main__':
    main()
