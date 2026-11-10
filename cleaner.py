import os
import shutil

print("🧹 Starting Esosa's Automated File Cleaner... 🧹\n")

# 1. Tell the script which folder to clean up!
# We will use your active folder '.' which means "the current directory"
folder_to_clean = "."

# 2. Grab a list of every single file sitting inside this folder
all_files = os.listdir(folder_to_clean)

print("🔍 Scanning files inside your directory...")

for filename in all_files:
    # 3. Find where the extension dot is (like .py or .txt)
    name, extension = os.path.splitext(filename)
    
    # Clean up the extension text (remove the dot and make it lowercase)
    # Example: ".txt" turns into "txt"
    folder_name = extension[1:].lower()
    
    # Ignore the file if it doesn't have an extension (like standard folders)
    # Also ignore our main script so it doesn't move itself!
    if folder_name == "" or filename == "cleaner.py":
        continue
        
    print("- Found a ." + folder_name + " file named: " + filename)
    
    # 4. If the destination folder doesn't exist yet, build it out of Legos!
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
        print("📁 Created a brand new folder named: " + folder_name)
        
    # 5. Pick up the file and slide it cleanly into the new matching folder box
    shutil.move(filename, os.path.join(folder_name, filename))
    print("🚚 Successfully moved " + filename + " into the '" + folder_name + "' folder!")

print("\n✨ Folder system is now perfectly organized and clean! ✨")

