import life_module


def buy_food(bag):
    bag["gold"] -= 1
    life_module.life += 1
    return bag, life_module.life


def meet_bad_guy(bag):
    bag["armour"] += 1
    bag["gold"] += 1
    return bag


def tavern_adventure():
    tavern_file = "tavern.txt"
    with open(tavern_file, "r") as f:
        lines = f.readlines()
    print(lines[0])
    user_choice = int(input("What do you want to do? 1 - buy food, 2 - ADVENTURE"))
    user = False
    while user is False:
        if user_choice == 1:
            for line in lines[1:3]:
                print(line)
            user_choice2 = int(input("1 - stay in Tavern \n2 - leave"))
            if user_choice2 == 1:
                for line in lines[4:7]:
                    print(line)
            if user_choice2 == 2:
                print("What a pity... Bye")
            buy_food(bag, life_module.life)
            return True
        elif user_choice == 2:
            for line in lines[4:7]:
                print(line)
                meet_bad_guy(bag)
            return True
        else:
            print("Choose again.")
            user_choice = int(input("What do you want to do? 1 - buy food, 2 - ADVENTURE"))



