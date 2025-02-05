LETTER = 'A'
RANGE = 60


def main():
    current_letter = LETTER
    letter_i = 0
    root = ''

    sequence = root + current_letter

    skip = 1

    for i in range(RANGE):
        if i == 0:
            pass

        else:
            current_letter, bool_add_root = increment_letter(sequence[-1])

            #TODO: when the last element of sequence is to add root, only then do we need to itter over
            # the other elements to check if they will also addroot.
            # so list(sequence[:-2]) is where we need to look and increment.
            # but technically you just check element before to increment like ZZZ into AAAA
            # the ending Z increments the ones next to it by domino effect
            # if char == Z then urn into A, and check leading char if also needs increment.
            # if no more left, and first char is Z turned to A, then add an A
            if skip == 0:
                root += '#'
                current_letter = 'A'

                skip = 1

            if bool_add_root:
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


def add_root():
    ...


if __name__ == "__main__":
    main()