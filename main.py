import generator_imienia as gi
import woods
import tavern
from life_module import Life
from life_module import bcolors

menu_dict = {
    'tavern': 't',
    'the woods': 'w'
}

bag = {
    "food": 1,
    "gold": 1,
    "armour": 1
 }
zycie = Life(100)

def show_pasek(bag):
    Life.show_life(zycie)
    print("".join([k + " : " + str(v) + "  " for k, v in bag.items()]))
    print('\n')


def menu(full_name, bag):
    print("Welcome in our game, " + full_name + " ! This is your bag:")
    show_pasek(bag)
    for k, v in menu_dict.items():
        print("".join([k + " : " + str(v) + "  "]))
    menu_choice = input("choose where do you want to go:")
    if menu_choice == 't':
        bag,life_change = tavern.tavern_adventure(bag)
        print(life_change)
        zycie.update(life_change)
        show_pasek(bag)
    if menu_choice == 'w':
        bag,life_change = woods.woods_adventure(bag)
        print(life_change)
        zycie.update(life_change)
        show_pasek(bag)





#bag_added = woods.pick_berries(bag)
#print(bag_added)
# woods.fight_with_wolf(bag)
# print(woods.bag)

def main():
    print("Generate your name:")
    full_name = gi.generate_characters_name()
    #life = 100


    print(full_name)
    menu(full_name, bag)





if __name__ == "__main__":
    main()






