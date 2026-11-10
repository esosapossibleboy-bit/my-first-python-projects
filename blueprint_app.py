# 1. THE BLUEPRINT (The Cookie Cutter)
class Product:
    # This setup function builds the structural walls of our product object
    def __init__(self, item_name, item_price, item_category):
        self.name = item_name
        self.price = item_price
        self.category = item_category

    # A built-in action card to neatly introduce itself
    def show_details(self):
        print("- 🏷️ " + self.name + " (" + self.category + ") costs $" + str(self.price))

# 2. STAMPING OUT COOKIES (Creating Objects from the Class)
# Instead of typing messy dictionaries, we just use our neat blueprint!
product1 = Product("Laptop", 800, "Tech")
product2 = Product("Sneakers", 100, "Fashion")
product3 = Product("Coffee Mug", 15, "Home")

# 3. PUTTING THE COOKIES IN A JAR (Storing Objects in a List)
cookie_jar = [product1, product2, product3]

print("=== 📐 THE BLUEPRINT & COOKIE APP ===")
print("Reading items stamped out from our custom blueprint class:\n")

# Loop through our jar and tell each object to run its action card!
for item in cookie_jar:
    item.show_details()

