def check_valid_input(letter_guessed, old_letters_guessed):
    """
    Checks if the input string is valid.
    :param letter_guessed: input character
    :param old_letters_guessed: list that contains the letters guessed so far
    :return: returns True if the input string contains only one alphabet character which not guessed previously, otherwise - returns False
    :rtype: boolean
    """
    letter_guessed_length = len(letter_guessed)
    lower_letter_guessed = letter_guessed.lower()
    if letter_guessed_length > 1 or not lower_letter_guessed.isalpha() or lower_letter_guessed in old_letters_guessed:
        return False
    else:
        return True

def main():
    old_letters = ['a', 'b', 'c']
    print(check_valid_input('C', old_letters))

if __name__ == "__main__":
    main()