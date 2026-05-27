secret_word = "global"
guessed_word = []
attempts_left = 10

while attempts_left > 0:
    display = ""

    for letter in secret_word:
        if letter in guessed_word:
            display += letter + " "
        else:
            display += "_ "

    print(f"\nWord to guess: {display}")

    if "_" not in display:
        print("LFG 🔥 You are insane at this man! Correct")
        break

    guess = input("Guess the letter: ").lower()
    if len(guess) != 1:
        print("Bro one letter at a time ! ")
        continue

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
