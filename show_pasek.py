from life_module import Life


def show_pasek(bag):
    Life.show_life()
    print("".join([k + " : " + str(v) + "  " for k, v in bag.items()]))
    print('\n')
