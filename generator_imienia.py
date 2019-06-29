import random



def generate_name(first_letter, name_length, gender):
    string_VOWEL = 'aeiouy'
    string_CONSONANT = "bcdfghjklmnpqrstvwxz"
    name_letters = [first_letter]
    letters = 0

    while letters < name_length - 3:
        if name_letters[letters] in string_VOWEL:
            add_letter = random.choice(string_CONSONANT)
            name_letters.append(add_letter)
            letters = letters + 1
        else:
            add_letter = random.choice(string_VOWEL)
            name_letters.append(add_letter)
            letters = letters + 1

    if gender == 'w':
        last_letters = random.choice(['nna', 'ara', 'ora'])
    elif gender == 'm':
        last_letters = random.choice(['org', 'dor', 'der'])
    else:
        last_letters = random.choice(['day', 'moy', 'foi'])

    name = "".join(name_letters)
    name = name.capitalize() + last_letters
    return name


def add_title(name):
    number_list = ["I", "II", "III", "IV", "V"]
    number = random.choice(number_list)
    title_list = ["The Obese", "The Thief", "The Slayer", "The Worst"]
    title = random.choice(title_list)
    name_with_title = name + " " + number + " " + title
    return name_with_title


def generate_characters_name():
    first_letter = input("choose first letter of the name:")
    name_length = input("choose length of the name:")
    if name_length in ['5', '6', '7', '8', '9', '10']:
        name_length = int(name_length)
    else:
        name_length = input("name length should be a number 5-10! Choose length of the name:")
        name_length = int(name_length)
    gender = input("choose gender m/w/n")
    name = generate_name(first_letter, name_length, gender)
    full_name = add_title(name)
    return full_name

