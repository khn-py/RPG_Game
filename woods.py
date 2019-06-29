import generator_imienia
import life_module


def pick_berries(bag):
    bag["food"] += 1
    return bag


def fight_with_wolf(bag, life):
    bag["food"] += 2
    life_module.life -= 10
    return bag


def lose_life(life):
    life_module.life -= 100
    return life

def show_woods_story(full_name):
    name = ''
    print( generator_imienia.add_title(full_name) + " went to the woods, choose what" + generator_imienia.add_title(full_name) + " want to do:")
    print("1. Pick the berries to get 1 food")
    print("2. Fight with wolfs to get more 2 foods.")


def open_woods():
    with open('woods.txt', 'r') as fopen:
        lines = fopen.readlines()


def woods_adventure(bag, life):
    phrase = int(input("Write 1 or 2: "))
    if phrase == 1:
        print(lines[0])
        fight_or_run = print(int(input("Do you want to fight (1) or run (2)?")))
        while fight_or_run == 1:
            print(lines[2])
            fight_with_wolf(bag, life)
            return bag
    elif phrase == 2:
        print(lines[3])
        pick_berries(bag)
        return bag
    else:
        print("This is not what i expected! Choose 1 or 2")

