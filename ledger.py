import os

print("🗄️ Activating Esosa's Relational Ledger Engine... 🗄️")

DB_FILE = "database_vault.txt"
master_ledger = []

# --- 🛰️ THE ENTERPRISE BOOT LOAD PIPELINE ---
if os.path.exists(DB_FILE):
    print("🔄 Decompressing hard drive registry logs...")
    with open(DB_FILE, "r", encoding="utf-8") as file:
        for line in file:
            cleaned = line.strip()
            if cleaned:
                parts = cleaned.split("|")
                if len(parts) == 3:
                    # Reconstruct the text line into a structured data dictionary!
                    master_ledger.append({
                        "item": parts[0],
                        "cost": parts[1],
                        "tag": parts[2]
                    })
else:
    print("📭 Clean slate detected. Initializing new system array matrices.")

# --- INTERACTIVE CONTROL CORE LOOP ---
while True:
    print(f"\n==========================================")
    print(f"📂 TOTAL LEDGER ENTRIES: {len(master_ledger)} ROWS ACTIVE")
    print(f"==========================================")
    
    print("Choose an action: Type 'add', 'view', 'delete', or 'exit':")
    action = input().lower().strip()
    
    if action == "exit":
        print("\n💾 Committing memory matrices permanently to hard disk...")
        with open(DB_FILE, "w", encoding="utf-8") as file:
            for entry in master_ledger:
                # Flatten the dictionary card back into a single piped line string
                flat_line = f"{entry['item']}|{entry['cost']}|{entry['tag']}"
                file.write(flat_line + "\n")
        print("🔒 Ledger fully cached and encrypted. System shut down safely. 🤫")
        break
        
    elif action == "add":
        print("Enter Item Description (e.g., Flight Ticket, Tech Gear):")
        item_desc = input().strip()
        print("Enter Cost Value (€) or Priority Rank:")
        cost_val = input().strip()
        print("Enter Category Tag (e.g., Travel, Savings, Personal):")
        tag_cat = input().strip()
        
        if item_desc and cost_val and tag_cat:
            # Inject a brand new structured dictionary record row into our master tracker list
            master_ledger.append({
                "item": item_desc,
                "cost": cost_val,
                "tag": tag_cat
            })
            print(f"✅ Row successfully mapped into ledger cache!")
            
    elif action == "view":
        if len(master_ledger) == 0:
            print("📭 Your relational database ledger is completely empty!")
        else:
            print("\n📜 --- MASTER REGISTRY SYSTEM MANIFEST --- 📜")
            print("------------------------------------------------------------")
            print("Slot  | Description    | Cost/Rank | Category Tag           ")
            print("------------------------------------------------------------")
            for i in range(len(master_ledger)):
                entry = master_ledger[i]
                print(f"[{i}]".ljust(5) + " | " + entry["item"].ljust(14) + " | " + entry["cost"].ljust(9) + " | " + entry["tag"])
            print("------------------------------------------------------------")
            
    elif action == "delete":
        if len(master_ledger) == 0:
            print("❌ Operation aborted! No entries exist inside the vault framework.")
            continue
            
        print("Enter the Slot number index you want to destroy:")
        try:
            target_slot = int(input())
            if 0 <= target_slot < len(master_ledger):
                purged_row = master_ledger.pop(target_slot)
                print(f"💥 Destroyed row entry for '{purged_row['item']}' at Slot [{target_slot}]!")
            else:
                print("⚠️ Boundary error! That slot index coordinate does not exist.")
        except:
            print("❌ Fault detected! You must input a valid slot number.")
            
    else:
        print("❌ Unknown command! Please use 'add', 'view', 'delete', or 'exit'.")

