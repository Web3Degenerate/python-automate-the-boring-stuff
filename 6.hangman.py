import random
word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

# TODO-1: - Use a while loop to let the user guess again.
game_over = False

# TODO-38: Create a List to preserve correctly guessed letters (8th)
correct_letters_list = []

while not game_over:
    guess = input("Guess a letter: ").lower()

    #moved into while game_over false loop
    # guess = input("Guess a letter: ").lower()

    display = ""

    # TODO-2: Change the for loop so that you keep the previous correct letters in display.

    # display_error_message = False
    # display_success_message = False
    # wrong_guess_letter = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters_list.append(letter)
            # display_success_message = True
        elif letter in correct_letters_list:
            display += letter
        else:
            display += "_"
            # display_error_message = True
            # wrong_guess_letter = guess

    # if display_error_message == True:
    # # I think you could just use 'guess' here
    #     print(f"sorry mate, {wrong_guess_letter} is not in the mystery word. Have another crack at it.")
    #     display_error_message = False
    #     wrong_guess_letter = ""
    # # else:
    # if display_success_message == True:
    #     print(f"Good Guess homie, letter {guess} is correct. Keep going mate!")
    #     display_success_message = False


    # for letter in chosen_word:
    #     if letter == guess:
    if guess in chosen_word:
        print(f"Good Guess homie, letter {guess} is correct. Keep going mate!")
    else:
        print(f"sorry mate, {guess} is not in the mystery word. Have another crack at it.")


    print("\n***Current Status**")
    print(f"   {display}")
    print("\n***************")

    #### IMPORTANT PYTHON FUNCTION - in and NOT in ###############
### not in
    if "_" not in display:
        game_over = True
        print(f'Congrats, you guessed the word {chosen_word}\n You win!')