import random  # 1. Open the expansion pack!

# 2. Tell the computer to pick a mystery number between 1 and 10
secret_number = random.randint(1, 10)
attempts = 0

print("--- THE TRUE MYSTERY GAME ---")
print("The computer has chosen a secret number. Good luck!")

while True:
    guess_string = input("Guess a number between 1 and 10: ")
    guess = int(guess_string)
    attempts = attempts + 1

    if guess == secret_number:
        print("🎉 YOU WIN!")
        print("It took you " + str(attempts) + " tries!")
        break
    else:
        # 3. Give a helpful hint!
        if guess < secret_number:
            print("📈 Too low! Try a bigger number.\n")
        else:
            print("📉 Too high! Try a smaller number.\n")
