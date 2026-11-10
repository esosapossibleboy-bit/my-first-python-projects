import tkinter as tk

# 📝 Magic Recipe 1: What happens when you click the button?
def button_clicked():
    # Grab the text from the input box
    user_text = input_box.get()
    # Change the label text to shout a greeting!
    result_label.config(text="🚀 App Idea Saved: " + user_text, fg="#00FF00")

# 🏛️ Setup the Main Window Window
window = tk.Tk()
window.title("Esosa's Desktop App Factory")
window.geometry("400x300")
window.configure(bg="#1e1e1e") # Dark mode background!

# 1. Add a Big Title Label
title_label = tk.Label(window, text="🌟 DESKTOP DASHBOARD 🌟", font=("Arial", 16, "bold"), bg="#1e1e1e", fg="white")
title_label.pack(pady=20)

# 2. Add an Input Field (The Microphone Box)
input_box = tk.Entry(window, font=("Arial", 12), width=30)
input_box.pack(pady=10)

# 3. Add a Clickable Button
submit_button = tk.Button(window, text="Submit App Idea", font=("Arial", 12, "bold"), bg="#007ACC", fg="white", command=button_clicked)
submit_button.pack(pady=10)

# 4. Add a Label to show the success message
result_label = tk.Label(window, text="Waiting for your input...", font=("Arial", 11), bg="#1e1e1e", fg="#888888")
result_label.pack(pady=20)

# Turn the desktop window loop on! Keep it open.
window.mainloop()
