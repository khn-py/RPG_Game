import generator_imienia as gi
import woods
import main_menu as mm





bag = {
    "food": 1,
    "gold": 1,
    "armour": 1
}



#bag_added = woods.pick_berries(bag)
#print(bag_added)
# woods.fight_with_wolf(bag)
# print(woods.bag)

def main():
    print("Generate your name:")
    full_name = gi.generate_characters_name()
    life = 100
    print(mm.menu(full_name, bag))
    # print(show_woods_story(full_name))




if __name__ == "__main__":
    main()






