#generator imienia:
import generator_imienia as gi


def generate_characters_name():
    first_letter = input("choose first letter of the name:")
    name_length = int(input("choose length of the name:"))
    gender = input("choose gender m/w/n")
    name = gi.generate_name(first_letter, name_length, gender)
    full_name = gi.add_title(name)
    print(full_name)


generate_characters_name()