import generator_imienia

def pick_berries(bag):
    bag["food"] += 1
    return bag


def fight_with_wolf(bag, life):
    bag["food"] += 2
    "life" -= 10
    return bag


def lose_life(life):
    "life" -= 100
    return life

#zaimportuj imię z generatora imienia, cos mi sie imie podświetla
name = ''
print( generator_imienia.add_title(name) + "went to the woods, choose what" + generator_imienia.add_title(name) + "want to do:")
print("1. Pick the berries to get 1 food")
print("2. Fight with wolfs to get more 2 foods.")


with open('woods.txt', 'r') as fopen:
  lines = fopen.readlines()


def choose_phrase():
    phrase = input("Write 1 or 2")
     if phrase == 1:
        print('woods.txt'[1])
        fight_with_wolf(bag, life)
    elif phrase == 2:
        print('woods.txt'[2])
        pick_berries(bag)
    else:
        print("This is not what i expected! Choose 1 or 2")
        choose_phrase()
