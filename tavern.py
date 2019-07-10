import life
import random


def buy_food(bag):
    bag["gold"] -= 1

    bag["food"] += 1
    life_change = 10
    return bag, life_change


def win_with_ghost(bag):
    bag["armour"] += 1
    bag["gold"] += 2
    life_change = random.randrange(20, 80, 1) * -1
    return bag, life_change


def lose_with_ghost(bag):
    life_change = -100
    return bag, life_change
# tak, wiem, że zmienna bag nic tu nie robi, ale dzięki temu, że ją tu wpisałam wyświetlił się pasek, więc może jest potrzebna

def walk_and_cry(bag):
    bag["food"] -= 1
    life_change = -5
    return bag, life_change


def run_away(bag):
    bag["gold"] -= 1
    life_change = -10
    return bag, life_change

def do_nothing(bag):
    bag["gold"] += 0
    life_change = 0
    return bag, life_change


def cemetery_art():
    print("""
      ,-=-.       ______     _
     /  +  \     />----->  _|1|_
     | ~~~ |    // -/- /  |_ H _|
     |R.I.P|   //  /  /     |S|
  V,,|_____|V,//_____/VvV,v,|_|/,,vhjwv/

""")


def ghost_art():
    print(""""     .-.
   .'   `.
   :g g   :
   : o    `.
  :         ``.
 :             `.
:  :         .   `.
:   :          ` . `.
 `.. :            `. ``;
    `:;             `:'
       :              `.
        `.              `.     .
          `'`'`'`---..,___`;.-' """)


def bad_guy_art():
    print(""" 
                          _....._
                     .-'.'.'.'.'.'.`-.
                   .'.'.'.'.'.'.'.'.'.`.
                   .'.'               '.
                 |.'    _.--...--._     |
                  |   `._.-.....-._.'   |
                  |     _..- .-. -.._   |
               .-.'    `.   ((@))  .'   '.-.
              ( ^ \      `--.   .-'     / ^ )
               \  /         .   .       \  /
               /          .'     '.  .-    \
              ( _.|      (_`-._.-'_)    |._\)
               `-' \   ' .--.          / `-'
                   |  / /|_| `-._.'\   |
                   |   |       |_| |   /-.._
                _..-\   `.--.______.'  |
                     \       .....     |
                      `.  .'      `.  /
                        \           .'
                 LGB     `-..___..-`""")



def tavern_adventure(bag):
    tavern_file = "tavern.txt"
    with open(tavern_file, 'r') as f:
        lines = f.readlines()
    print(lines[0])
    user_choice = int(input("What do you want to do? \n1 - Buy food, \n2 - ADVENTURE \n3 - Back to the city"))
    user = False
    while user is False:
        if user_choice == 1:
            for line in lines[1:3]:
                print(line)
            user_choice2 = int(input("1 - stay in Tavern \n2 - pay and leave"))
            if user_choice2 == 1:
                for line in lines[4:7]:
                    bad_guy_art()
                    print(line)
            if user_choice2 == 2:
                print("What a pity... Bye")
            return buy_food(bag)
            user = True
        elif user_choice == 2:
            for line in lines[4:7]:
                print(line)
            bad_guy_art()
            return cemetery_adventure(bag)
            user = True
        elif user_choice == 3:
            print("ok")
            return do_nothing(bag)

        else:
            print("Choose again.")
            user_choice = int(input("What do you want to do? \n1 - buy food, \n2 - ADVENTURE\n"))

    return bag, 0


def cemetery_adventure(bag):
    with open("cemetery.txt", 'r') as f:
        lines = f.readlines()
    print("\n")
    print(lines[0])
    cemetery_art()
    choose_action = int(input("What would you like to do: \n1 - Walk around and cry \n2 - ADVENTURE\n 3 - Go back to the city"))
    if choose_action == 1:
        print(lines[2])
        return walk_and_cry(bag)
    elif choose_action == 3:
        print("ok")
        return do_nothing(bag)
    elif choose_action == 2:
        print(lines[3])
        choice_leave = input("1 - Yes, I'm sure! I want to fight! \n2 - No,I'll pass")
        if choice_leave == "1":
            print(lines[3])
            fight_result = random.choice(["win", "lose"])
            if fight_result == "win":
                print("You won")
                return win_with_ghost(bag)
            else:
                ghost_art()
                print("The ghost appears to be the Lady With 99 Ghost-Cats And A Parrot. They eat you alive. You're dead.")
                return lose_with_ghost(bag)
        if choice_leave == "2":
            print("You coward! You ran away so fast that you lost some gold.")
            return run_away(bag)
    return bag, 0

