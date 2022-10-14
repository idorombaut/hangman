def is_valid_input(letter_guessed):
    """Checks if the input string is valid.
    :param letter_guessed: input character
    :type letter_guessed: string
    :return: returns True if the input string contains only one alphabet character, otherwise - returns False
    :rtype: boolean
    """
    letter_length = len(letter_guessed)
    if letter_length > 1 or not letter_guessed.isalpha():
        return False
    else:
        return True

def main():
    print(is_valid_input("app$"))

if __name__ == "__main__":
    main()