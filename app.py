import tkinter as tk

# ➕ ADD MACHINE
def do_addition():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        result = num1 + num2
        label_result.config(text="✨ Result: " + str(result), fg="darkgreen")
    except:
        label_result.config(text="❌ Type real numbers!", fg="red")

# ➖ SUBTRACT MACHINE
def do_subtraction():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        result = num1 - num2
        label_result.config(text="✨ Result: " + str(result), fg="darkgreen")
    except:
        label_result.config(text="❌ Type real numbers!", fg="red")

# ✖️ MULTIPLY MACHINE
def do_multiplication():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        result = num1 * num2
        label_result.config(text="✨ Result: " + str(result), fg="darkgreen")
    except:
        label_result.config(text="❌ Type real numbers!", fg="red")


# --- DESIGNING THE VISUAL SCREEN ---
window = tk.Tk()
window.title("Esosa's Visual Wizard Calculator")
window.geometry("450x400")

# Header Title
title_label = tk.Label(window, text="🧙‍♂️ Wizard Calculator 🧙‍♂️", font=("Arial", 16, "bold"))
title_label.pack(pady=15)

# Number 1 Box
lbl1 = tk.Label(window, text="Enter First Number:", font=("Arial", 11))
lbl1.pack()
entry_num1 = tk.Entry(window, font=("Arial", 12), justify="center")
entry_num1.pack(pady=5)

# Number 2 Box
lbl2 = tk.Label(window, text="Enter Second Number:", font=("Arial", 11))
lbl2.pack()
entry_num2 = tk.Entry(window, font=("Arial", 12), justify="center")
entry_num2.pack(pady=5)

# Instruction for Buttons
lbl_btn = tk.Label(window, text="Choose Your Magic Symbol:", font=("Arial", 11, "italic"))
lbl_btn.pack(pady=10)

# --- BUTTONS SECTION ---
# Plus Button
btn_plus = tk.Button(window, text=" ➕ ADD ", font=("Arial", 12, "bold"), bg="lightblue", command=do_addition)
btn_plus.pack(pady=2)

# Minus Button
btn_minus = tk.Button(window, text=" ➖ SUBTRACT ", font=("Arial", 12, "bold"), bg="lightpink", command=do_subtraction)
btn_minus.pack(pady=2)

# Multiply Button
btn_multiply = tk.Button(window, text=" ✖️ MULTIPLY ", font=("Arial", 12, "bold"), bg="lightyellow", command=do_multiplication)
btn_multiply.pack(pady=2)

# Grand Output Answer Label
label_result = tk.Label(window, text="✨ Result: Waiting for Spell...", font=("Arial", 14, "bold"))
label_result.pack(pady=25)

window.mainloop()
