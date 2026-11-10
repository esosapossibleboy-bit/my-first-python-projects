import os

print("🗄️ Activating Esosa's Persistent Database Vault... 🗄️")

DB_FILE = "database_vault.txt"
data_records = []

# --- 🛰️ THE AUTO-LOAD DATA PIPELINE ---
# The exact split-second the app turns on, it reaches onto the disk to read your history!
if os.path.exists(DB_FILE):
    print("🔄 Syncing with local hard drive data cache...")
    with open(DB_FILE, "r", encoding="utf-8") as file:
        for line in file:
            cleaned_line = line.strip()
            if cleaned_line:
                # Uncouple the text stream back into clean data items!
                data_records.append(cleaned_line)
else:
    print("📭 No previous database file found. Initializing clean vault matrix.")

# --- MAIN INTERACTIVE CORE LOOP ---
while True:
    print(f"\n==========================================")
    print(f"📦 CURRENT VAULT STORAGE: {len(data_records)} RECORDS DETECTED")
    print(f"==========================================")
    
    print("Choose an action: Type 'add', 'view', 'delete', or 'exit':")
    choice = input().lower().strip()
    
    if choice == "exit":
        # --- 💾 THE AUTO-SAVE SAFETY PIPELINE ---
        print("\n💾 Saving master database records permanently to disk...")
        with open(DB_FILE, "w", encoding="utf-8") as file:
            for record in data_records:
                file.write(record + "\n")
        print("🔒 Vault locked and cached safely. Goodbye! 🤫")
        break
        
    elif choice == "add":
        print("Enter the item or note you want to lock into the database:")
        new_item = input().strip()
        if new_item:
            data_records.append(new_item)
            print(f"✅ Successfully cached: '{new_item}'")
            
    elif choice == "view":
        if len(data_records) == 0:
            print("📭 Your database storage vault is completely empty!")
        else:
            print("\n📜 --- CURRENT DATABASE MASTER MANIFEST --- 📜")
            for i in range(len(data_records)):
                # Print out a clean numbered list tracking index locations
                print(f" Slot [{i}]: {data_records[i]}")
            print("--------------------------------------------")
            
    elif choice == "delete":
        if len(data_records) == 0:
            print("❌ Nothing to delete! Vault is empty.")
            continue
            
        print("Enter the Slot number [] you want to incinerate:")
        try:
            slot_index = int(input())
            if 0 <= slot_index < len(data_records):
                removed_item = data_records.pop(slot_index)
                print(f"💥 Successfully incinerated: '{removed_item}' from Slot [{slot_index}]!")
            else:
                print("⚠️ Invalid Slot number! That slot matrix coordinate does not exist.")
        except:
            print("❌ Error! You must type a real slot number.")
            
    else:
        print("❌ Invalid choice! Please type 'add', 'view', 'delete', or 'exit'.")
