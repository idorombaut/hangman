def check_win(secret_word, old_letters_guessed):
    """
    Checks if the secret word guessed correctly 
    :param secret_word: string to guess
    :param old_letters_guessed: list that contains the letters guessed so far
    :return: returns True if all letters in the secret word appear in the list, otherwise - returns False
    :rtype: boolean
    """
    for char in secret_word:
        if not char in old_letters_guessed:
            return False
    return True

def main():
    secret_word = "yes"
    old_letters_guessed = ['d', 'g', 'e', 'i', 's', 'k', 'y']
    print(check_win(secret_word, old_letters_guessed))

if __name__ == "__main__":
    main()