hero_weapon = "Laser Sword"
hero_health = 100

# 🧙‍♂️ THE MAGIC MACHINE WITH A SAFETY NET
def run_calculator():
    print("\n[🔮 A holographic wizard appears from the lock!]")
    print("Wizard: 'To pass, you must solve my math spell!'")
    
    print("Enter your first number: ")
    # --- START OF SAFETY NET ---
    try:
        num1 = int(input())
    except:
        print("❌ That wasn't a real number! The wizard zaps you and forces a 0!")
        num1 = 0
    # --- END OF SAFETY NET ---

    print("Enter your second number: ")
    num2 = int(input())
    
    # ... (the rest of your calculator code stays exactly the same!)


    if trick == "+":
        ans = num1 + num2
    elif trick == "-":
        ans = num1 - num2
    else:
        ans = num1 * num2
        
    print("✨ The wizard yells: ALAKAZAM! The answer is " + str(ans))
    print("[🔒 CLICK! The puzzle door unlocks! 🔓]\n")

# --- THE ACTUAL GAME LOOP ---
print("Welcome, Brave Hero!")

while hero_health > 0:
    print("\n--- NEW TURN ---")
    print("Your current health is: " + str(hero_health))
    print("You enter a dark cave holding a " + hero_weapon)
    print("You see paths ahead! Type 'left', 'right', 'door', or 'exit': ")
    player_choice = input()

    if player_choice == "left":
        print("Yay! You found a chest full of shiny gold! 💰")
        
    elif player_choice == "door":
        # 🚀 CALLING OUR MACHINE HERE!
        print("You approach a massive golden door with a digital combination lock...")
        run_calculator() 
        print("You walk through the unlocked door into a beautiful paradise garden! 🌸")
        
    elif player_choice == "exit":
        print("🌟 Victory! You escaped the dark cave safely! You win!")
        break
        
    else:
        print("Oh no! A scary dragon jumps out! 🐉")
        print("The dragon breathes fire on you!")
        hero_health = hero_health - 30
        print("Ouch! Your health dropped to " + str(hero_health))

print("\nThank you for playing Esosa's Mega-Game! 🌟")
