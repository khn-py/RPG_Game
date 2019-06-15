#import life
import math
import sys

life = 100

def show_life(life):
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
