import os

print("📊 Activating Esosa's Automated Financial Analytics Engine... 📊\n")

DB_FILE = "database_vault.txt"
master_ledger = []

# 1. BOOT PIPELINE: Load the data from our hard drive into memory
if not os.path.exists(DB_FILE):
    print("📭 Error! No database vault file detected. Run ledger.py first to create records.")
else:
    with open(DB_FILE, "r", encoding="utf-8") as file:
        for line in file:
            cleaned = line.strip()
            if cleaned:
                parts = cleaned.split("|")
                if len(parts) == 3:
                    master_ledger.append({
                        "item": parts[0],
                        "cost": parts[1],
                        "tag": parts[2]
                    })

    print(f"🔍 Successfully loaded {len(master_ledger)} total records into the analytics core.")
    
    # 2. ASK THE USER FOR THE SEARCH FILTER CRITERIA
    print("\nEnter a Category Tag to filter and calculate (e.g., Travel, Nonstop, Personal):")
    search_tag = input().lower().strip()
    
    filtered_records = []
    total_filtered_cost = 0.0
    
    # 3. RUN THE MATRICES SCANNER SEARCH LOOP
    for entry in master_ledger:
        if entry["tag"].lower().strip() == search_tag:
            filtered_records.append(entry)
            try:
                # Convert the text string back into a mathematical decimal number!
                total_filtered_cost += float(entry["cost"])
            except:
                # If the cost value wasn't a standard number, ignore it for the sum math
                pass

    # 4. COMPUTE FINANCIAL STATISTICS REPORT
    num_matches = len(filtered_records)
    
    if num_matches == 0:
        print(f"\n📭 No records found matching the category tag: '{search_tag}'")
    else:
        avg_cost = total_filtered_cost / num_matches if num_matches > 0 else 0
        
        print(f"\n🎯 --- FILTERED ANALYSIS REPORT FOR CATEGORY: '{search_tag.upper()}' --- 🎯")
        print("------------------------------------------------------------")
        print("Slot  | Description    | Cost/Rank | Category Tag           ")
        print("------------------------------------------------------------")
        
        for i in range(num_matches):
            entry = filtered_records[i]
            print(f"[{i}]".ljust(5) + " | " + entry["item"].ljust(14) + " | " + entry["cost"].ljust(9) + " | " + entry["tag"])
            
        print("------------------------------------------------------------")
        print(f"📊 MATCH STATS: Found {num_matches} active row item(s).")
        print(f"💰 FINANCIAL METRICS: Cumulative Category Cost = €{total_filtered_cost:.2f}")
        print(f"📈 BUSINESS INTELLIGENCE: Average Category Cost = €{avg_cost:.2f}")
        print("============================================================")

print("\n✨ Financial data filter mission completed! ✨")
