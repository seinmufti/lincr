### Program to increment a sequence of letters,
### Returns list of incremented letter sequences

from letter_increment import LetterIncrement

INPUT_SEQUENCE = 'A'
RANGE = 15


def main():
    letter_increment = LetterIncrement()
    sequences = letter_increment.increment_sequence(INPUT_SEQUENCE)
    print(sequences)


if __name__ == "__main__":
    main()