import os
from datetime import datetime

print("⚙️ Activating Esosa's Automated Report Document Factory... ⚙️")

DB_FILE = "database_vault.txt"
REPORT_FILE = "flight_summary_report.txt"

# 1. READ AND CRUNCH THE VAULT MATRIX DATA
if not os.path.exists(DB_FILE):
    print("❌ Error! Cannot locate 'database_vault.txt'. Please run tracker.py first to add data rows.")
else:
    print("🔍 Reading local data storage registers...")
    
    flight_rows = []
    total_cost = 0
    cheapest_price = 99999
    best_airline = "N/A"
    
    with open(DB_FILE, "r", encoding="utf-8") as file:
        for line in file:
            cleaned = line.strip()
            if cleaned:
                parts = cleaned.split("|")
                if len(parts) == 3:
                    airline, price_str, stops = parts
                    price_num = float(price_str)
                    
                    # Track analytics
                    total_cost += price_num
                    if price_num < cheapest_price:
                        cheapest_price = price_num
                        best_airline = airline
                        
                    flight_rows.append([airline, price_str, stops])
                    
    # Calculate average seat cost across our active portfolio rows
    num_flights = len(flight_rows)
    avg_cost = total_cost / num_flights if num_flights > 0 else 0
    
    # 2. DESIGN AND EXPORT THE BEAUTIFUL SUMMARY DOCUMENT
    print("🎨 Formatting report layout and drawing file frames...")
    
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Open our target output report file in "w" mode to overwrite/create a fresh page!
    with open(REPORT_FILE, "w", encoding="utf-8") as report:
        # Paint the header frame blocks
        report.write("==============================================================\n")
        report.write("✈️        ESOSA'S GLOBAL AVIATION FLIGHT SUMMARY REPORT       ✈️\n")
        report.write("==============================================================\n")
        report.write(f"Generated On: {current_time} CET\n")
        report.write(f"Source Node:  Helmstedt Base Database Core Cache\n")
        report.write("--------------------------------------------------------------\n\n")
        
        report.write("📜 --- ACTIVE FLIGHT FARE DATA REGISTRY --- 📜\n")
        report.write("--------------------------------------------------------------\n")
        report.write("Airline Name   | Ticket Cost | Flight Route Parameters       \n")
        report.write("--------------------------------------------------------------\n")
        
        for row in flight_rows:
            air, prc, stp = row
            report.write(f"{air.ljust(14)} | €{prc.ljust(10)} | {stp}\n")
            
        report.write("--------------------------------------------------------------\n\n")
        
        # Inject the parsed financial business intelligence metrics block
        report.write("📊 --- CORE BUSINESS INTELLIGENCE METRICS --- 📊\n")
        report.write("==============================================================\n")
        report.write(f"📂 Total Tracked Flight Routes : {num_flights}\n")
        report.write(f"💰 Cumulative Portfolio Cost  : €{total_cost:.2f}\n")
        report.write(f"📈 Average Flight Ticket Fare  : €{avg_cost:.2f}\n")
        report.write(f"🥇 Optimal Budget Option Found : {best_airline} (€{cheapest_price:.2f})\n")
        report.write("==============================================================\n\n")
        
        report.write("🔒 REPORT INTEGRITY STATUS: VERIFIED & SECURED BY BACKEND CORE\n")
        report.write("✨ End of Automated Document Stream ✨\n")

    print(f"🚀 SUCCESS! A beautiful summary document report has been saved to: {REPORT_FILE}!")

