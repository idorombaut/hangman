guess_a_letter = input("Guess a letter: ")
str_length = len(guess_a_letter)
if str_length > 1 and guess_a_letter.isalpha():
    print("E1")
elif str_length == 1 and not guess_a_letter.isalpha():
    print("E2")
elif str_length > 1 and not guess_a_letter.isalpha():
    print("E3")
else:
    print(guess_a_letter.lower())