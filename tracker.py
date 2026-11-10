import os

print("🗄️ Activating Esosa's Column-Delimited Database Vault... 🗄️")

DB_FILE = "database_vault.txt"
data_records = []  # 🌟 FIXED HERE!

# --- 🛰️ THE AUTO-LOAD COLUMN SPLITTER PIPELINE ---
if os.path.exists(DB_FILE):
    print("🔄 Syncing and parsing local column matrices...")
    with open(DB_FILE, "r", encoding="utf-8") as file:
        for line in file:
            cleaned_line = line.strip()
            if cleaned_line:
                parts = cleaned_line.split("|")
                if len(parts) == 3:
                    data_records.append(parts)
else:
    print("📭 No previous database file found. Initializing clean column matrix.")

# --- MAIN INTERACTIVE CORE LOOP ---
while True:
    print(f"\n==========================================")
    print(f"📦 CURRENT VAULT STORAGE: {len(data_records)} FLIGHT RECORDS")
    print(f"==========================================")
    
    print("Choose an action: Type 'add', 'view', 'delete', or 'exit':")
    choice = input().lower().strip()
    
    if choice == "exit":
        print("\n💾 Compressing and saving column data rows permanently to disk...")
        with open(DB_FILE, "w", encoding="utf-8") as file:
            for record in data_records:
                raw_line = "|".join(record)
                file.write(raw_line + "\n")
        print("🔒 Vault locked and cached safely. Goodbye! 🤫")
        break
        
    elif choice == "add":
        print("Enter Airline Name (e.g., Lufthansa):")
        airline = input().strip()
        print("Enter Round-Trip Price (€):")
        price = input().strip()
        print("Enter Stops/Layovers (e.g., Nonstop or 1 Stop):")
        stops = input().strip()
        
        if airline and price and stops:
            data_records.append([airline, price, stops])
            print(f"✅ Successfully cached row: {airline} | €{price} | {stops}")
            
    elif choice == "view":
        if len(data_records) == 0:
            print("📭 Your delimited database vault is completely empty!")
        else:
            print("\n📜 --- CURRENT SPREADSHEET MASTER MANIFEST --- 📜")
            print("------------------------------------------------------------")
            print("Slot  | Airline        | Price   | Flight Routing Parameter ")
            print("------------------------------------------------------------")
            for i in range(len(data_records)):
                row = data_records[i]
                print(f"[{i}]".ljust(5) + " | " + row[0].ljust(14) + " | €" + row[1].ljust(6) + " | " + row[2])
            print("------------------------------------------------------------")
            
    elif choice == "delete":
        if len(data_records) == 0:
            print("❌ Nothing to delete! Vault is empty.")
            continue
            
        print("Enter the Slot number you want to incinerate:")
        try:
            slot_index = int(input())
            if 0 <= slot_index < len(data_records):
                removed_row = data_records.pop(slot_index)
                print(f"💥 Successfully incinerated data row for '{removed_row[0]}' from Slot [{slot_index}]!")
            else:
                print("⚠️ Invalid Slot number! Coordinate out of bounds.")
        except:
            print("❌ Error! You must type a real slot number.")
            
    else:
        print("❌ Invalid choice! Please type 'add', 'view', 'delete', or 'exit'.")
