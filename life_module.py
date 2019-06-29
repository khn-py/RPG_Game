#import???
import bcolors
import sys
import math

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



class Life:

    def __init__(self, life):
        self.life = life

    def show_life(self):
        """ printing battery"""
        rounded = int(math.ceil(self.life / 10.0))
        lost = 10 - rounded
        if self.life >= 70:
            battery = (bcolors.OKGREEN + '[ ' + ('▓ ' * (rounded) + bcolors.ENDC + ('░ ' * int(lost)) + ']' + ' ' + str(self.life) + '%'))
            print(battery)

        elif self.life <= 30:
            battery = (bcolors.FAIL +'[ ' + ('▓ ' * (rounded) + bcolors.ENDC + ('░ ' * int(lost)) + ']' + ' ' + str(self.life) + '%'))
            print(battery)

        elif self.life >30 and self.life <70:
            battery = (bcolors.WARNING +'[ ' + ('▓ ' * (rounded) + bcolors.ENDC + ('░ ' * int(lost)) + ']' + ' ' + str(self.life) + '%'))
            print(battery)
        else:
            pass


    def print_low_life(self):
        """printing if you have less than 3 life"""
        if self.life <= 30:
            return "You are slowly dying, get some rest at Karczma??"
        else:
            pass

    def end_game(self):
        """if you have no life: printing youre dead"""
        if self.life <= 0:
            print("You're dead :(")
            sys.exit(0)
        else:
            pass

    def __repr__(self):
        """do modules from above"""
        if self.life > 30:
            self.show_life()
            print(self.show_life())
        elif self.life <= 30 and self.life > 0:
            self.show_life()
            self.print_low_life()
            print(self.show_life(), self.print_low_life())
        return " "


if __name__ == '__main__':
    zycie = Life(40)
    print(zycie)
    print("odpaliłeś jako głowny moduł")
else:
    print("odpaliłeś moduł")