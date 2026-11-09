print("🛒 Welcome to Esosa's File-Saving Mega Mart! 🛒")

cart = []
prices = []

while True:
    print("\nType an item to add to your cart (or type 'checkout' to finish):")
    item = input()
    
    if item == "checkout":
        break
    else:
        cart.append(item)
        print("How much does " + item + " cost? $")
        price = float(input())
        prices.append(price)
        print("✅ Added " + item + " ($" + str(price) + ") to your cart!")

# --- SCRIBBLING INTO OUR DIGITAL NOTEBOOK ---
total_bill = 0.0

# This magic line creates a real "receipt.txt" file on your computer!
with open("receipt.txt", "w", encoding="utf-8") as file:
    file.write("🧾 --- ESOSA'S OFFICIAL MEGA MART RECEIPT --- 🧾\n")
    
    for i in range(len(cart)):
        line = "- " + cart[i] + ": $" + str(prices[i]) + "\n"
        file.write(line) # Put it in the file!
        total_bill = total_bill + prices[i]
        
    file.write("--------------------------------------\n")
    file.write("💰 GRAND TOTAL: $" + str(total_bill) + "\n")
    file.write("Thank you for shopping with us! 🎉\n")

print("\n🚀 SUCCESS! Your receipt has been printed on the screen AND saved to 'receipt.txt'!")

