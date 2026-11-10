import os
import shutil

print("🚨 Activating Esosa's Upgraded Emergency Restore System... 🚨\n")

main_room = "."
folders_to_delete = []

# 1. Launch the search radar
for root, dirs, files in os.walk(main_room):
    if root == main_room or ".git" in root:
        continue
        
    print("🕵️ Radar scanning inside folder: " + root)
    
    if root not in folders_to_delete:
        folders_to_delete.append(root)
        
    # 2. Pull all files out to the main floor
    for filename in files:
        current_file_path = os.path.join(root, filename)
        destination_path = os.path.join(main_room, filename)
        
        print("  🚚 Dragging file out: " + filename)
        try:
            shutil.move(current_file_path, destination_path)
        except:
            # If the file is already out here, don't crash!
            pass

print("\n🧹 Disintegrating empty folder boxes from the inside out...")

# 3. 🌟 THE FIX: We reverse the list so deep folders like .\build\app\localpycs 
# get deleted BEFORE parent folders like .\build!
folders_to_delete.reverse()

for folder in folders_to_delete:
    if os.path.exists(folder):
        try:
            os.rmdir(folder)
            print("  💥 Destroyed empty folder: " + folder)
        except Exception as e:
            print("  ⚠️ Could not remove " + folder + " yet.")

print("\n✨ EMERGENCY RESTORE COMPLETE! Everything is back and clean! ✨")
