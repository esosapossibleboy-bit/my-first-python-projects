# Our database of products using Dictionaries inside a List!
# Each {} is a card containing specific information keys.
app_marketplace = [
    {"name": "Laptop", "price": 800, "category": "Tech"},
    {"name": "Phone", "price": 500, "category": "Tech"},
    {"name": "Sneakers", "price": 100, "category": "Fashion"},
    {"name": "Backpack", "price": 50, "category": "Fashion"}
]

print("=== 🔍 WELCOME TO THE SMART MATCH ENGINE ===")

while True:
    print("\n1. 🛍️ View All Products")
    print("2. 💸 Find Products Under a Budget")
    print("3. 🚪 Exit App")
    
    choice = input("\nChoose an option (1-3): ")
    
    if choice == "1":
        print("\n📦 CURRENT INVENTORY:")
        for item in app_marketplace:
            # We look up the secret values inside the item card using ['key']!
            print("- " + item["name"] + " | Price: $" + str(item["price"]) + " (" + item["category"] + ")")
            
    elif choice == "2":
        budget_string = input("What is your maximum budget in dollars? $")
        budget = int(budget_string)
        
        print("\n🎯 MATCHES FOUND FOR YOUR BUDGET ($" + str(budget) + "):")
        matches_found = 0
        
        for item in app_marketplace:
            # The search logic gate checks if the item price fits the budget!
            if item["price"] <= budget:
                print("- ✅ " + item["name"] + " is within budget at $" + str(item["price"]))
                matches_found = matches_found + 1
                
        if matches_found == 0:
            print("❌ Sorry, nothing fits your budget. Try saving up more!")
            
    elif choice == "3":
        print("👋 Closing the matching engine. See you next time!")
        break
    else:
        print("❌ Invalid selection!")
