import requests

print("🕷️ Launching Esosa's Local Data Explorer Bot... 🕷️\n")

# Points directly to our own local port 5000 instead of the outside internet!
url = "http://localhost:5000"

print("🚀 Flying data drone over to your local API satellite server...")

try:
    # 1. Fetch the data package from our server
    response = requests.get(url)
    
    # 2. Activate our JSON decoder ring to turn it into a neat dictionary
    decoded_cabinet = response.json()
    
    print("\n🛰️ Connection established! Decoding local API matrix...")
    print("=========================================================")
    
    # 3. Unlock the weather drawer
    weather_drawer = decoded_cabinet["weather"]
    loc = weather_drawer["location"]
    temp = weather_drawer["temp_C"]
    cond = weather_drawer["condition"]
    
    print("☀️ --- DECODED WEATHER CORE --- ☀️")
    print(f"Target Area: {loc}")
    print(f"Temperature: {temp}°C")
    print(f"Atmosphere:  {cond}")
    print("---------------------------------")
    
    # 4. Unlock the banking rates drawer
    money_drawer = decoded_cabinet["currency_rates"]
    print("\n💰 --- DECODED BANKING MATRIX (Base: 1 USD) --- 💰")
    print(f"Euro (EUR):         {money_drawer['EUR']}")
    print(f"British Pound (GBP): {money_drawer['GBP']}")
    print(f"Japanese Yen (JPY):  {money_drawer['JPY']}")
    print("=========================================================")
    print("\n🚀 DATA MISSION ACCOMPLISHED! You mastered API architectures!")

except Exception as e:
    print("\n❌ Mission failed! Could not find the local API satellite.")
    print("Make sure api_server.py is actively running in another window!")
