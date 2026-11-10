print("✈️ Activating Esosa's Aviation Route Terminal Matrix... ✈️\n")

print("🔍 Compiling Round-Trip (Going & Coming) Fares to Nigeria:")
print("----------------------------------------------------------------------")
print("Departure Hub    | Operator Flight Line | Layovers | Speed     | Cost")
print("----------------------------------------------------------------------")

# 1. The Real-Time Aviation Routing Array
# All prices represent complete round-trip tickets (going and coming!)
flight_matrix = [
    {"hub": "Berlin (BER)   ", "airline": "Air France   ", "stops": "1 Stop ", "duration": "9h 05m", "price": 607},
    {"hub": "Frankfurt (FRA)", "airline": "Lufthansa    ", "stops": "Nonstop", "duration": "6h 35m", "price": 664},
    {"hub": "Frankfurt (FRA)", "airline": "Air France   ", "stops": "1 Stop ", "duration": "9h 30m", "price": 611},
    {"hub": "Hannover (HAJ) ", "airline": "KLM Royal    ", "stops": "1 Stop ", "duration": "14h 10m", "price": 673}
]

lowest_fare = 99999
best_option = {}

# 2. THE DATA CRUNCHING LOGIC LOOP
for fare_tier in flight_matrix:
    print(f"{fare_tier['hub']}  | {fare_tier['airline']}  | {fare_tier['stops']}  | {fare_tier['duration']}  | €{fare_tier['price']}")
    
    # Calculate the pricing index to catch the financial sweet-spot
    if fare_tier["price"] < lowest_fare:
        lowest_fare = fare_tier["price"]
        best_option = fare_tier

print("----------------------------------------------------------------------")
print(f"💰 OPTIMAL BUDGET ROUTE: €{lowest_fare} with {best_option['airline'].strip()} out of {best_option['hub'].split(' ')[0]}")
print("----------------------------------------------------------------------\n")

print("📊 --- ROUND-TRIP PRICING TIER GRAPH --- 📊\n")

# 3. THE RETRO TERMINAL CHART DISPLAY ENGINE
for fare_tier in flight_matrix:
    # Scale math: Each green block represents exactly €50 of round-trip ticket value
    block_scaling = int(fare_tier["price"] / 50)
    bar_graphics = "🟩" * block_scaling
    
    print(f"{fare_tier['airline'].strip().ljust(14)}: {bar_graphics} (€{fare_tier['price']})")

print("\n==================================================================")
print("💡 Scale Indicator: Each block (🟩) represents €50.00 of total bill.")
print("💡 Multi-Hub Tracking: Mapped across Hannover, Berlin & Frankfurt.")
print("==================================================================")
