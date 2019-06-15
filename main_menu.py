#import woods
import tavern
import show_pasek as sp

main_menu_dict = {
    'tavern': 't',
    'the woods': 'w'
}


def main_menu(full_name, bag):
    print("Welcome in our game, " + full_name + " ! This is your bag:" )
    sp.show_pasek(bag)
    for k, v in main_menu_dict.items():
        print("".join([k + " : " + str(v) + "  " ]))
    main_menu_choice = input("choose where do you want to go:")
    if main_menu_choice == 't':
        tavern_adventure()
    #if main_menu_choice == 'w':
    #    woods_adventure()
