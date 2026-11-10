print("🧙‍♂️ Welcome to the Upgraded Wizard Calculator! 🧙‍♂️")

print("Enter your first number: ")
first_number = int(input())

print("Enter your second number: ")
second_number = int(input())

# Ask the wizard what trick they want to do!
print("Choose a magic trick! Type '+', '-', or '*': ")
trick = input()

# --- THE WIZARD'S TRAFFIC LIGHT ---
if trick == "+":
    answer = first_number + second_number
    print("✨ Addition Alakazam! Your total is: " + str(answer))
    
elif trick == "-":
    answer = first_number - second_number
    print("✨ Subtraction Sparkle! Your total is: " + str(answer))
    
elif trick == "*":
    answer = first_number * second_number
    print("✨ Multiplication Magic! Your total is: " + str(answer))
    
else:
    print("🔮 Oops! That wasn't a valid magic spell.")
