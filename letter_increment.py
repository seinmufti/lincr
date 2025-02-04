def main():
    LETTER = 'A'
    RANGE = 60

    current_letter = LETTER
    letter_i = 0
    root = ''
    sequence = root + current_letter
    skip = 1

    for i in range(RANGE):
        current_letter, letter_i, bool_add_root = increment_letter(sequence[-1], letter_i)

        if bool_add_root:
            skip -= 1
            
            if skip < 1:
                root += '#'

                skip = 1

        print(root)        


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