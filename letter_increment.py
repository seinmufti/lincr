LETTER = 'A'
RANGE = 60


def main():
    current_letter = LETTER
    letter_i = 0
    root = ''

    sequence = root + current_letter

    skip = 1


    for i in range(RANGE):
        current_letter, letter_i, bool_add_root = increment_letter(sequence[-1], letter_i)

        if skip == 0:
            root += '#'

            skip = 1

        if bool_add_root:
            skip -= 1

        print(root + current_letter)


def increment_letter(letter, i):
    current_letter = chr(ord(letter) + i)
    letter_i = i + 1

    if current_letter == 'Z':
        letter_i = 0

        bool_add_root = True
        
    else:
        bool_add_root = None

    return current_letter, letter_i, bool_add_root


if __name__ == "__main__":
    main()