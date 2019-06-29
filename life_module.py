#import life
import math
import sys
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
#bcolors.(np)Header + ... + bcolors.ENDC

#life = 100

def show_life(life):
    life = 100
    rounded = int(math.ceil(life / 10.0))
    lost = 10 - rounded
    print('[ ' + ('▓ ' * (rounded) + ('░ ' * int(lost)) + ']' + ' ' + str(life) + '%'))

def print_low_life(life):
    if life <= 30:
        print("You are slowly dying, get some rest at Karczma??")
    else:
        pass

def end_game(life):
    if life <= 0:
        sys.exit(0)
    else:
        pass

def main(life):
    if life > 30:
        show_life(life)
    elif life <= 30 and life > 0:
        show_life(life)
        print_low_life(life)
    else:
        print("You died!")
        end_game(life)
