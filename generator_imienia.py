#- Konieczność użycia modułu `random`.
import random
#- Program generuje wymawialne(!) imię o zadanej długości (7) i dodaje do niego przydomek (opcjonalnie również tytuł i liczebnik).



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


def main():
    first_letter = input("choose first letter of the name:")
    name_length = int(input("choose length of the name:"))
    gender = input("choose gender m/w")
    name = generate_name(first_letter, name_length, gender)
    print(add_title(name))


if __name__ == "__main__":
    print('Plik uruchomiony bezpośrednio')
    main()
else:
    print('Plik zaimportowano jako moduł')


