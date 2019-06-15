import generator_imienia as gi
import woods


#generator imienia:
def generate_characters_name():
    first_letter = input("choose first letter of the name:")
    name_length = int(input("choose length of the name:"))
    gender = input("choose gender m/w/n")
    name = gi.generate_name(first_letter, name_length, gender)
    full_name = gi.add_title(name)
    print(full_name)



bag = {
    "food": 1,
    "gold": 1,
    "armour": 1
}


bag_added = woods.pick_berries(bag)
print(bag_added)
# woods.fight_with_wolf(bag)
# print(woods.bag)

def main():
    generate_characters_name()

if __name__ == "__main__":
    main()






