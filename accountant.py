print("📊 Activating Esosa's Terminal Data Graphics Bot... 📊\n")

print("🔍 Parsing spreadsheet data...")
print("--------------------------------------------------")

grand_total = 0
products = []
revenues = []

# 1. Open the file and parse the rows
with open("sales_data.csv", "r", encoding="utf-8") as file:
    headers = file.readline()
    
    for line in file:
        parts = line.strip().split(",")
        if len(parts) == 3:
            product = parts[0]
            price = float(parts[1])
            quantity = int(parts[2])
            
            total_revenue = price * quantity
            grand_total = grand_total + total_revenue
            
            # Save our results into our list trains so we can draw them later!
            products.append(product)
            revenues.append(total_revenue)

print("💰 GRAND TOTAL EARNINGS FOR THE SHOP: $" + str(grand_total))
print("--------------------------------------------------\n")

print("📊 --- PRODUCT REVENUE VISUALIZATION CHART --- 📊\n")

# 2. THE GRAPHICS BOT ENGINE
# Walk through every item we tracked and calculate how many graph blocks to draw
for i in range(len(products)):
    # We turn the revenue into a smaller scale (Divide by 50) so the graph bars fit perfectly!
    # Example: $500 / 50 = 10 blocks!
    bar_length = int(revenues[i] / 50)
    
    # We use the special multiplication symbol to print the block character multiple times!
    bar_graphics = "🟩" * bar_length
    
    # Print the name tag followed by its graphic bar box
    print(products[i].ljust(14) + ": " + bar_graphics + " ($" + str(revenues[i]) + ")")

print("\n==================================================")
print("💡 Scale Indicator: Each block (🟩) represents $50.00")
print("==================================================")

