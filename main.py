import generator_imienia as gi
import woods
from tavern import tavern_adventure, buy_food
import show_pasek as sp
import life_module
#dodać wszystkie moduły, usunąć moduły z modułów, dodać atrybuty funkcji w modułach


#class Bag:
#    def __init__(self):
#        food = 1
#        gold = 1
#        armour = 1

menu_dict = {
    'tavern': 't',
    'the woods': 'w'
}

bag = {
    "food": 1,
    "gold": 1,
    "armour": 1
 }


def menu(full_name, bag):
    print("Welcome in our game, " + full_name + " ! This is your bag:")
    sp.show_pasek(bag)
    for k, v in menu_dict.items():
        print("".join([k + " : " + str(v) + "  "]))
    menu_choice = input("choose where do you want to go:")
    if menu_choice == 't':
        tavern_adventure(bag)
        print (bag)
    if menu_choice == 'w':
        woods.woods_adventure(bag)
        print(bag)





#bag_added = woods.pick_berries(bag)
#print(bag_added)
# woods.fight_with_wolf(bag)
# print(woods.bag)

def main():
    print("Generate your name:")
    full_name = gi.generate_characters_name()
    life = 100


    print(full_name)
    menu(full_name, bag)





if __name__ == "__main__":
    main()






