def show_hidden_word(secret_word, old_letters_guessed):
    """
    Shows the progress of guessed secret word. 
    :param secret_word: string to guess
    :param old_letters_guessed: list that contains the letters guessed so far
    :return: returns a string contains the letters which guessed correctly, and the missing letters with an underscore
    :rtype: string
    """
    string = ""
    for i in range(len(secret_word)):
        if secret_word[i] in old_letters_guessed:
            string = string + secret_word[i]
            string = string + ' '
        else:
            string = string + '_ '
    return string

def main():
    secret_word = "mammals"
    old_letters_guessed = ['s', 'p', 'j', 'i', 'm', 'k']
    print(show_hidden_word(secret_word, old_letters_guessed))

if __name__ == "__main__":
    main()