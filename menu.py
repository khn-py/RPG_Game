import woods
import tavern
import show_pasek as sp
import life_module

menu_dict = {
    'tavern': 't',
    'the woods': 'w'
}


def menu(full_name, bag):
    print("Welcome in our game, " + full_name + " ! This is your bag:" )
    sp.show_pasek(bag)
    for k, v in menu_dict.items():
        print("".join([k + " : " + str(v) + "  " ]))
    menu_choice = input("choose where do you want to go:")
    if menu_choice == 't':
        tavern.tavern_adventure()
    if menu_choice == 'w':
        woods.woods_adventure(bag, life)
