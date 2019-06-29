import life_module
import random


def buy_food(bag):
    bag["gold"] -= 1
    #life_module.life += 1
    return bag


def win_with_ghost(bag):
    bag["armour"] += 1
    bag["gold"] += 2
    life_change = random.randrange(-20, -80)
    return bag, life_change

def lose_with_ghost():
    life_change = -100
    return life_change


def walk_and_cry(bag):
    bag["food"] -= 1
    return bag


def tavern_adventure(bag):
    tavern_file = "tavern.txt"
    with open(tavern_file, 'r') as f:
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
            buy_food(bag)
            return True
        elif user_choice == 2:
            for line in lines[4:7]:
                print(line)
            print("""\_....._
                                   .-'.'.'.'.'.'.`-.
                                 .'.'.'.'.'.'.'.'.'.`.
                                /.'.'               '.\
                                |.'    _.--...--._     |
                                \    `._.-.....-._.'   /
                                |     _..- .-. -.._   |
                             .-.'    `.   ((@))  .'   '.-.
                            ( ^ \      `--.   .-'     / ^ )
                             \  /         .   .       \  /
                             /          .'     '.  .-    \
                            ( _.\    \ (_`-._.-'_)    /._\)
                             `-' \   ' .--.          / `-'
                                 |  / /|_| `-._.'\   |
                                 |   |       |_| |   /-.._
                             _..-\   `.--.______.'  |
                                  \       .....     |
                                   `.  .'      `.  /
                                     \           .'
                              LGB     `-..___..-`""")

            #meet_bad_guy(bag)
            cementary_adventure(bag)
            return True
        else:
            print("Choose again.")
            user_choice = int(input("What do you want to do? 1 - buy food, 2 - ADVENTURE"))


def cementary_adventure(bag):
    with open("cementary.txt", 'r') as f:
        lines = f.readlines()
    print(lines[0])
    choose_action = int(input("What would you like to do: 1 - Walk around and cry, 2 - ADVENTURE"))
    if choose_action == 1:
        print(lines[2])
        walk_and_cry(bag)
    elif choose_action == 2:
        print(lines[3])
        fight_result = random.choice(["win", "lose"])
        if fight_result == "win":
            print("You won")
            win_with_ghost(bag)
        else:
            print("you lose")
            lose_with_ghost()
    return bag, 0

#przy śmierci nie wyświetla paska


