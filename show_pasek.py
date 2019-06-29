from life_module import Life
from life_module import bcolors


def show_pasek(bag):
    Life.show_life()
    print("".join([k + " : " + str(v) + "  " for k, v in bag.items()]))
    print('\n')
