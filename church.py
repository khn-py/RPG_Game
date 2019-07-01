def pray(bag):
    life_change = 5
    return bag, life_change


def pay_healing(bag):
    bag["gold"] -= 5
    life_change = 50
    return bag, life_change

def fight_the_priest(bag):
    print("You bastard! Attacking the priest is a shame! S H A M E\n You get 5 gold and your life gets -25")
    bag["gold"] += 5
    life_change = - 25
    return bag, life_change

def do_nothing(bag):
    bag["gold"] += 0
    life_change = 0
    return bag, life_change


def church_art():
    print("""   .
            -|-
             |
            /A\
           //^\\
         ,// _ \\,
         |/`/_\`\|
          |  ,  |
          | /^\ |
          |//'\\|
        ,//` _ `\\,
      ,//` .'|'. `\\,
    ,//`   |-|-|   `\\,
  ,//`     [_|_]     `\\,
  |/T                 T\|
    |  _   __ __   _  |
    | /_\ |  |  | /_\ |
    | |_| | .|. | |_| |
    |     |__|__|     |
jgs '----[_______]----'
          =======
         ======
      ======""")


def holy_art():
    print("""                     |                        
   ____________    __ -+-  ____________ 
   \_____     /   /_ \ |   \     _____/   
    \_____    \____/  \____/    _____/  
     \_____                    _____/   
        \___________  ___________/              
                  /____\ """)


def pray_in_church(bag):
    church_art()
    church_file = "church.txt"
    with open(church_file, 'r') as f:
        lines = f.readlines()
    print(lines[0])
    user_choice = int(input("What do you want to do? \n1 - Pray for free (+5 Life) \n2 - Pay for healing (- 5 Gold, +50 Life) \n3 - Fight the priest \n4 - Go back to the city"))
    user = False
    while user is False:
        if user_choice == 1:
            print(lines[1])
            return pray(bag)
            user = True
        elif user_choice == 2:
            for line in lines[2:4]:
                print(line)
            holy_art()
            return pay_healing(bag)
            user = True
        elif user_choice == 3:
            for line in lines[5:6]:
                print(line)
            return fight_the_priest(bag)
        elif user_choice == 4:
            print("Ok")
            return do_nothing(bag)
        else:
            print("Choose again.")
            user_choice = int(input("What do you want to do? \n1 - Pray for free \n2 - Pay for healing \n3-Fight the priest \n4-Go back to the city"))

    return bag, 0