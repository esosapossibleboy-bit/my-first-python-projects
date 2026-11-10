import random
import string

print("🔐 Welcome to Esosa's Secure Password Generator! 🔐\n")

# 1. Ask the user how long they want their secret password to be
print("Enter the desired password length (e.g., 12 or 16): ")
try:
    password_length = int(input())
except:
    print("⚠️ That wasn't a valid number! Forcing a secure length of 12.")
    password_length = 12

# 2. Mix our character buckets together into a giant soup!
letters = string.ascii_letters
numbers = string.digits
symbols = string.punctuation

character_soup = letters + numbers + symbols

# 3. Create a blank container to hold our password pieces
password_list = []

# 4. Scoop out random characters from the soup loop-by-loop
for i in range(password_length):
    random_char = random.choice(character_soup)
    password_list.append(random_char)

# 5. Glue the character list together into a single unbreakable word!
secure_password = "".join(password_list)

print("\n✨ Your Secure Password Has Been Generated: ✨")
print("==============================================")
print(secure_password)
print("==============================================")
print("\nKeep this password safe and secret! 🤫")

