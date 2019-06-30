import generator_imienia as gi
import woods
import tavern
import church
from life_module import Life, bcolors


menu_dict = {
    "TAVERN": 't',
    "WOODS": 'w',
    "CEMETERY": 'c',
    "CHURCH": "h"
}

bag = {
    "food": 1,
    "gold": 10,
    "armour": 1
 }

zycie = Life(100)


def show_pasek(bag):
    Life.show_life(zycie)
    print("".join([k + " : " + str(v) + "  " for k, v in bag.items()]))
    print('\n')


def menu(full_name, bag):
    print("Hello  " + bcolors.BOLD + full_name + bcolors.ENDC + " ! Let's start the journey! \n This is your bag:\n")
    show_pasek(bag)
    while zycie.life > 0:
        print("\n")
        for k, v in menu_dict.items():
            print(bcolors.BOLD + "".join([k + " : " + str(v) + "  " + bcolors.ENDC]))
        menu_choice = input("Choose where do you want to go:")
        if menu_choice == 't':
            bag, life_change = tavern.tavern_adventure(bag)
            print(life_change)
            zycie.update(life_change)
            show_pasek(bag)
        elif menu_choice == 'w':
            bag, life_change = woods.woods_adventure(bag)
            print(life_change)
            zycie.update(life_change)
            show_pasek(bag)
        elif menu_choice == 'c':
            bag, life_change = tavern.cemetery_adventure(bag)
            print(life_change)
            zycie.update(life_change)
            show_pasek(bag)
        elif menu_choice == "h":
            bag, life_change = church.pray_in_church(bag)
            print(life_change)
            zycie.update(life_change)
            show_pasek(bag)
        else:
            print("I'm sure you want to play. Choose one again!")


def main():
    print( bcolors.HEADER + "Welcome in simple RPG Game made by KHN-PY TEAM :)" + bcolors.ENDC)
    print("Generate your name:")
    full_name = gi.generate_characters_name()
    print(full_name)
    menu(full_name, bag)


if __name__ == "__main__":
    main()






