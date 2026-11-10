# --- FUNCTION 1: Save tasks to the hard drive ---
def save_to_hard_drive(tasks):
    # Open (or create) a file called tasks.txt in 'w' (write) mode
    file = open("tasks.txt", "w")
    for item in tasks:
        file.write(item + "\n")  # \n puts each task on a brand new line
    file.close()  # Always close the notebook when you are done writing!

# --- FUNCTION 2: Load tasks from the hard drive ---
def load_from_hard_drive():
    try:
        file = open("tasks.txt", "r")
        # Read the lines and clean up the extra spaces
        tasks = [line.strip() for line in file.readlines()]
        file.close()
        return tasks
    except:
        # If the file doesn't exist yet, start with a default list
        return ["Buy groceries", "Clean room"]

# 1. When the app starts, load our saved notebook list!
todo_list = load_from_hard_drive()

while True:
    print("\n===============================")
    print("🌟 THE PERMANENT TO-DO APP 🌟")
    print("===============================")
    print("1. 📊 View To-Do List")
    print("2. ➕ Add New Task")
    print("3. 🚪 Exit App")
    
    choice = input("\nSelect an option (1-3): ")
    
    if choice == "1":
        print("\n📝 YOUR CURRENT TASKS:")
        for task in todo_list:
            print("- " + task)
            
    elif choice == "2":
        new_task = input("What task do you want to add? ")
        todo_list.append(new_task)
        # 2. Save it immediately to the hard drive!
        save_to_hard_drive(todo_list)
        print("✅ Saved '" + new_task + "' permanently to tasks.txt!")
        
    elif choice == "3":
        print("👋 Goodbye! Your data is safe.")
        break
    else:
        print("❌ Invalid option!")
