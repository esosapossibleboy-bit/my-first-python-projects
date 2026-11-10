# --- RECIPE 1: The App Dashboard ---
def open_dashboard(username):
    print("\n===============================")
    print("🌟 WELCOME TO YOUR DASHBOARD, " + username.upper() + "! 🌟")
    print("===============================")
    print("1. 📊 View App Data")
    print("2. ⚙️ App Settings")
    print("3. 🚪 Log Out")
    
    choice = input("\nSelect an option (1-3): ")
    if choice == "1":
        print("📁 Loading your data... Everything looks great!")
    elif choice == "2":
        print("🔧 Opening settings menu...")
    elif choice == "3":
        print("👋 Logging out safely. See you next time!")
    else:
        print("❌ Invalid button pressed!")

# --- RECIPE 2: The Login Gate ---
def start_app():
    print("🔒 SECURITY GATE: PLEASE LOGIN")
    correct_password = "supersecret123"
    
    while True:
        password_guess = input("Enter your secret password: ")
        
        if password_guess == correct_password:
            print("\n✅ Access Granted!")
            # Shout the dashboard recipe card name to open it!
            open_dashboard("Esosa") 
            break
        else:
            print("❌ Wrong password! Try again.\n")

# --- START THE APP ---
# This single line calls our recipe card and turns the app machine on!
start_app()
