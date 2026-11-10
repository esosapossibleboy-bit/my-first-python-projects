import os
import sys

print("🔒 SYSTEM INITIALIZATION... SECURING PERIMETER... 🔒")

# --- ENCRYPTION MACHINES ---
def encrypt_text(plain_text):
    scrambled_pieces = []
    for char in plain_text:
        scrambled_pieces.append(chr(ord(char) + 3))
    return "".join(scrambled_pieces)

def decrypt_text(encrypted_text):
    original_pieces = []
    for char in encrypted_text:
        original_pieces.append(chr(ord(char) - 3))
    return "".join(original_pieces)

# --- 🌟 THE ANONYMOUS GATEKEEPER 🌟 ---
# Step 1: If there is no master file yet, let the real owner set it up!
if not os.path.exists("master_key.txt"):
    print("\n👋 Welcome, Owner! This is your first time setting up the vault.")
    print("Please choose your secret Master Password now:")
    new_master = input()
    
    # Scramble it immediately before saving to the file!
    with open("master_key.txt", "w", encoding="utf-8") as key_file:
        key_file.write(encrypt_text(new_master))
    print("✅ Master Password locked away securely in a separate file. Restarting app...")

# Step 2: Read the scrambled master password out of its hidden text drawer
with open("master_key.txt", "r", encoding="utf-8") as key_file:
    scrambled_master = key_file.read().strip()
    REAL_MASTER_PASSWORD = decrypt_text(scrambled_master)

# Step 3: Demand the key before revealing anything!
attempts = 3
while attempts > 0:
    print("\nEnter Master Password to unlock your vault (Attempts left: " + str(attempts) + "):")
    user_input = input()
    
    if user_input == REAL_MASTER_PASSWORD:
        print("🔓 ACCESS GRANTED! Welcome back. ✨")
        break
    else:
        attempts = attempts - 1
        print("❌ WRONG PASSWORD! Access Denied.")

if attempts == 0:
    print("\n🚨 TOO MANY WRONG ATTEMPTS! SYSTEM LOCKDOWN. 🚨")
    sys.exit()

# --- MAIN VAULT LOOP ---
while True:
    print("\nChoose an option: Type 'add' to save a password, 'view' to read your vault, or 'exit':")
    choice = input().lower()
    
    if choice == "exit":
        print("Vault locked securely. Goodbye! 🤫")
        break
        
    elif choice == "add":
        print("What application is this for? (e.g., Netflix, Roblox):")
        app_name = input()
        print("Enter the password to store:")
        password = input()
        
        encrypted_app = encrypt_text(app_name)
        encrypted_pass = encrypt_text(password)
        
        with open("vault_data.txt", "a", encoding="utf-8") as file:
            file.write(encrypted_app + "," + encrypted_pass + "\n")
            
        print("✅ Account securely encrypted and added to vault!")
        
    elif choice == "view":
        if not os.path.exists("vault_data.txt"):
            print("📭 Your vault is completely empty!")
            continue
            
        print("\n🔒 --- OPENING VAULT (DECRYPTED REPORT) --- 🔒")
        with open("vault_data.txt", "r", encoding="utf-8") as file:
            for line in file:
                parts = line.strip().split(",")
                if len(parts) == 2:
                    real_app = decrypt_text(parts[0])
                    real_pass = decrypt_text(parts[1])
                    print("- " + real_app + ": " + real_pass)
        print("------------------------------------------")
        
    else:
        print("❌ Invalid choice! Please type 'add', 'view', or 'exit'.")
