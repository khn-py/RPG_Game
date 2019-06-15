def pick_berries(bag):
    bag["food"] += 1
    return bag


def fight_with_wolf(bag, life):
    bag["food"] += 2
    "life" -= 10
    return bag


def loose_life(life):
    "life" -= 100
    return life