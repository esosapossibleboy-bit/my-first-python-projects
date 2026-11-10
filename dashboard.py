import requests

print("🌍 Launching Esosa's Live Global Data Dashboard... 🌍\n")

# ==========================================
# 🛰️ PIPELINE 1: LIVE LOCAL WEATHER RADAR
# ==========================================
# We target Helmstedt, Germany and request the format=j1 to get clean JSON data!
weather_url = "https://wttr.in"

print("📡 Connecting to global weather satellites for Helmstedt, Germany...")

try:
    weather_response = requests.get(weather_url, timeout=10)
    weather_data = weather_response.json()
    
    # Unlock the JSON filing cabinet layers piece by piece!
    current_state = weather_data["current_condition"][0]
    temp_c = current_state["temp_C"]
    condition = current_state["weatherDesc"][0]["value"]
    humidity = current_state["humidity"]
    
    print("\n☀️ --- LIVE WEATHER REPORT --- ☀️")
    print(f"Location:  Helmstedt, Germany")
    print(f"Condition: {condition}")
    print(f"Temperature: {temp_c}°C")
    print(f"Humidity:    {humidity}%")
    print("----------------------------------")

except Exception as e:
    print("❌ Weather Radar Sync Failed! Server timed out.")

# ==========================================
# 💱 PIPELINE 2: REAL-TIME CURRENCY MATRIX
# ==========================================
# We connect to an open, live currency rate exchange stream
currency_url = "https://er-api.com"

print("\n📡 Syncing with global banking exchange matrices...")

try:
    currency_response = requests.get(currency_url, timeout=10)
    currency_data = currency_response.json()
    
    # Grab the full exchange rates dictionary box
    rates = currency_data["rates"]
    
    # Extract specific global rates relative to 1 USD
    eur_rate = rates["EUR"]
    gbp_rate = rates["GBP"]
    jpy_rate = rates["JPY"]
    
    print("\n💰 --- LIVE CURRENCY EXCHANGE (Base: 1 USD) --- 💰")
    print(f"🇪🇺 Euro (EUR):       {eur_rate:.2f}")
    print(f"🇬🇧 British Pound:   {gbp_rate:.2f}")
    print(f"🇯🇵 Japanese Yen:    {jpy_rate:.2f}")
    print("-------------------------------------------------")
    print("🚀 Data Feed Status: SUCCESS! Real-time matrices mapped.")

except Exception as e:
    print("❌ Currency Sync Failed! Bank network blocked connection.")

print("\n✨ Global data streaming mission completed! ✨")
