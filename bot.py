import requests

print("🕷️ Launching Esosa's Upgraded Decoded Web Bot... 🕷️\n")

# 🛰️ THE FULL AND EXACT DATA COORDINATES:
url = "http://api.open-notify.org/astros.json"

print("🚀 Flying drone out to the space station file room...")

try:
    response = requests.get(url)
    
    # --- OUR SECRET DECODER RING ---
    space_dictionary = response.json()
    
    total_astronauts = space_dictionary["number"]
    
    print("\n🛰️ Drone returned and decoded the space report!")
    print("====================================================")
    print("👨‍🚀 TOTAL PEOPLE IN SPACE RIGHT NOW: " + str(total_astronauts))
    print("====================================================\n")
    
    astronaut_list = space_dictionary["people"]
    
    print("Here is the official list of space travelers:")
    
    for astronaut in astronaut_list:
        name = astronaut["name"]
        spaceship = astronaut["craft"]
        print("- " + name + " (Riding inside the: " + spaceship + ")")
        
    print("====================================================")

except:
    print("❌ Mission failed! The drone couldn't decode the internet data.")

print("\nSpace spy mission completed! 🌟")
