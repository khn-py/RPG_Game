import life_module as life


def show_pasek(bag):
    life.show_life()
    print("".join([k + " : " + str(v) + "  " for k, v in bag.items()]))


show_pasek(bag)
