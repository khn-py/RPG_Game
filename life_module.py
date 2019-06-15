#import life
import math
import sys

life = 100

def show_life():
    rounded = int(math.ceil(life / 10.0))
    lost = 10 - rounded
    return print('[ ' + ('▓ ' * (rounded) + ('░ ' * int(lost)) + ']' + ' ' + str(life) + '%'))

def print_low_life():
    if life <= 30:
        return print("You are slowly dying, get some rest at Karczma??")
    else:
        pass

def end_game():
    if life <= 0:
        sys.exit(0)
    else:
        pass

def main():
    if life > 30:
        show_life()
    elif life <= 30 and life > 0:
        show_life()
        print_low_life()
    else:
        print("You died!")
        end_game()
