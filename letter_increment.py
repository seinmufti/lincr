LETTER = 'A'
RANGE = 30


def main():
    current_letter = LETTER
    letter_i = 0
    root = ''

    sequence = root + current_letter

    skip = 1


    for i in range(RANGE):
        current_letter, bool_add_root = increment_letter(sequence[-1])

        if skip == 0:
            root += '#'

            skip = 1

        if bool_add_root:
            current_letter = 'A'
            skip -= 1
        
        sequence = root + current_letter

        print(sequence)


def increment_letter(letter):
    current_letter = chr(ord(letter) + 1)

    if current_letter == 'Z':

        bool_add_root = True
        
    else:
        bool_add_root = None

    return current_letter, bool_add_root


if __name__ == "__main__":
    main()