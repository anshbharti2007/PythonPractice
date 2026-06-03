secret_word = "global" # creating a variable for storing the secret word 
guessed_word = [] # creating a variable and assigning a empty list for storing guessed word 
attempts_left = 10 # created a variable for giving how many attempts are for guessing 

while attempts_left > 0: # looping until the attempt is greater than 0
    display = "" # creating a variable for storing string of char which are correct in the word 

    for letter in secret_word: # looping through each char in secreat word
        if letter in guessed_word: # conditioning if char in gussed word 
            display += letter + " " # then add character and a blankspace 
        else: # OR 
            display += "_ " # if char not in the letter add a under score next to it 

    print(f"\nWord to guess: {display}") # print function print in new line and show the how many char are guessed

    if "_" not in display: # if condition for if there is no underscore mean the word is guessed 
        print("LFG 🔥 You are insane at this man! Correct") # print function for tell you have guessed 
        break # breaks the while loop if condition met 

    guess = input("Guess the letter: ").lower() #input variable for guess word 
    if len(guess) != 1: # it will check if the guess is 1 char or not 
        print("Bro one letter at a time ! ") # if greater than 1 char it will print 
        continue #continue fucntion

    # Check repeated guess
    if guess in guessed_word: 
        print("You already guessed it 😭")
        continue

    guessed_word.append(guess)

    # Correct / wrong guess
    if guess in secret_word:
        print("LFG 🔥 Correct guess")
    else:
        attempts_left -= 1
        print(
            f"Bro lock TF in 😭 You only have {attempts_left} attempts left"
        )

if attempts_left == 0:
    print(f"You ran out of attempts 💀 The word was '{secret_word}'")
