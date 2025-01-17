import church
import name_genarator as gi
from life import Life, Bcolors
import tavern
import woods


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

actual_life = Life(100)


def show_status(bag):
    Life.show_life(actual_life)
    print("".join([k + " : " + str(v) + "  " for k, v in bag.items()]))
    print('\n')


def menu(full_name, bag):
    print("Hello  " + Bcolors.BOLD + full_name + Bcolors.ENDC + " ! Let's start the journey! \n This is your bag:\n")
    show_status(bag)
    while actual_life.life > 0:
        print("\n")
        for k, v in menu_dict.items():
            print(Bcolors.BOLD + "".join([k + " : " + str(v) + "  " + Bcolors.ENDC]))
        menu_choice = input("Choose where do you want to go:")
        if menu_choice == 't':
            bag, life_change = tavern.tavern_adventure(bag)
            print(life_change)
            actual_life.update(life_change)
            show_status(bag)
        elif menu_choice == 'w':
            bag, life_change = woods.woods_adventure(bag)
            print(life_change)
            actual_life.update(life_change)
            show_status(bag)
        elif menu_choice == 'c':
            bag, life_change = tavern.cemetery_adventure(bag)
            print(life_change)
            actual_life.update(life_change)
            show_status(bag)
        elif menu_choice == "h":
            bag, life_change = church.pray_in_church(bag)
            print(life_change)
            actual_life.update(life_change)
            show_status(bag)
        else:
            print("I'm sure you want to play. Choose one again!")


def main():
    print(Bcolors.HEADER + "Welcome in simple RPG Game made by KHN-PY TEAM :)" + Bcolors.ENDC)
    print("Generate your name:")
    full_name = gi.generate_characters_name()
    print(full_name)
    menu(full_name, bag)


if __name__ == "__main__":
    main()






