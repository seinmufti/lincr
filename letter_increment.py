class LetterIncrement():
    def increment_letter(self, input_sequence, incrementation_range):
        # Assign letters sequence
        sequence = input_sequence 
        # Convert sequence into list
        sequence_list = list(sequence)
        # Assign sequence len
        sequence_len = len(sequence) 
        
        # Print first sequence
        print(sequence)

        # increment sequence according to range provided
        for _ in range(incrementation_range): 
            # iterrate over each letter in sequence
            for i, letter in enumerate(reversed(sequence_list), start=1):
                # If not 'Z', increment the selected letter and assign in sequence list
                if letter != 'Z':
                    incremented_letter = chr(ord(letter) + 1)
                    sequence_list[-i] = incremented_letter
                    break
                # Else if 'Z',
                else:
                    # Change current letter to 'A'
                    if i <= sequence_len:
                        new_letter = 'A'
                        sequence_list[-i] = new_letter

                    # And if reached last letter, add 'A' to root, and update sequence len so next itteration itterates over new root
                    if i == sequence_len:
                        sequence_list = ['A'] + sequence_list
                        sequence_len = len(sequence_list)

            # Print incremented sequence
            incremented_sequence = ('').join(sequence_list)
            print(incremented_sequence)