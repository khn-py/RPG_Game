def buy_food(bag):
    bag["gold"] -= 1
    life += 1
    return bag, life


def meet_bad_guy(bag):
    bag["armour"] += 1
    bag["gold"] += 1
    return bag
