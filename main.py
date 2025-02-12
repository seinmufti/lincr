### Program to increment a sequence of letters

from letter_increment import LetterIncrement

INPUT_SEQUENCE = 'A'
RANGE = 1500

def main():
    letter_increment = LetterIncrement()
    letter_increment.increment_letter(INPUT_SEQUENCE, RANGE)

if __name__ == "__main__":
    main()