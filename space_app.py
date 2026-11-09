import tkinter as tk
import requests

# 🛰️ THE MAGIC DRONE MACHINE WITH THE API SUBDOMAIN FIX
def refresh_space_data():
    base_url = "http://api.open-notify.org"
    secret_room = "/astros.json"
    url = base_url + secret_room
    
    status_label.config(text="🚀 Drone flying to orbit... Please wait...", fg="blue")
    window.update() 
    
    try:
        response = requests.get(url)
        space_dictionary = response.json()
        total_astronauts = space_dictionary["number"]
        astronaut_list = space_dictionary["people"]
        
        count_label.config(text="👨‍🚀 Total People in Space Right Now: " + str(total_astronauts))
        
        report_display.delete("1.0", tk.END)
        
        for astronaut in astronaut_list:
            name = astronaut["name"]
            spaceship = astronaut["craft"]
            report_display.insert(tk.END, "- " + name + " (" + spaceship + ")\n")
            
        status_label.config(text="✅ Data Synced Successfully with Orbit!", fg="darkgreen")
        
    except:
        status_label.config(text="❌ Mission Failed! Check your internet connection.", fg="red")

# --- DESIGNING THE GRAPHICAL INTERFACE ---
window = tk.Tk()
window.title("Esosa's Live Space Dashboard")
window.geometry("500x500")

# Header Title Label
title_lbl = tk.Label(window, text="🛰️ Live Space Station Tracker 🛰️", font=("Arial", 16, "bold"))
title_lbl.pack(pady=15)

# Synchronize Data Button
sync_button = tk.Button(window, text="📡 Fetch Live Astronaut Report", font=("Arial", 12, "bold"), bg="darkblue", fg="white", command=refresh_space_data)
sync_button.pack(pady=10)

# Status Indicator
status_label = tk.Label(window, text="Click the button above to launch drone.", font=("Arial", 10, "italic"), fg="gray")
status_label.pack(pady=5)

# Count Display Label
count_label = tk.Label(window, text="👨‍🚀 Total People in Space: Waiting...", font=("Arial", 12, "bold"))
count_label.pack(pady=10)

# Visual Scrollable Text Box
report_display = tk.Text(window, font=("Arial", 11), width=50, height=12)
report_display.pack(pady=10)

window.mainloop()
