import math
import sys


class Bcolors:
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
            battery = (Bcolors.OKGREEN + '[ ' + ('▓ ' * (rounded) + Bcolors.ENDC + ('░ ' * int(lost)) + ']' + ' ' + str(self.life) + '%'))
            print(battery)

        elif self.life <= 30:
            battery = (Bcolors.FAIL +'[ ' + ('▓ ' * (rounded) + Bcolors.ENDC + ('░ ' * int(lost)) + ']' + ' ' + str(self.life) + '%'))
            print(battery)

        elif self.life >30 and self.life <70:
            battery = (Bcolors.WARNING +'[ ' + ('▓ ' * (rounded) + Bcolors.ENDC + ('░ ' * int(lost)) + ']' + ' ' + str(self.life) + '%'))
            print(battery)
        else:
            pass

    def update(self, change):
        self.life = self.life + change
        if self.life > 100:
            self.life = 100
        if self.life < 0:
            self.life = 0
            print("You died........... Thank you, next :)")
            self.end_game()

    def print_low_life(self):
        """printing if you have less than 3 life"""
        if self.life <= 30:
            return "You are slowly dying, get some rest at Karczma??"
        else:
            pass

    def end_game(self):
        """if you have no life: printing youre dead"""
        if self.life <= 0:
            print("Your game has finished because of 0% Life, try again by opening game again")
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


# if __name__ == '__main__':
#     zycie = Life(40)
#     print(zycie)
#     zycie.update(-50)
#     print(zycie)
#     print("odpaliłeś jako głowny moduł")
# else:
#     print("odpaliłeś moduł")