print("✈️ Activating Esosa's Enterprise Object-Oriented Flight Engine... ✈️\n")

# ============================================================
# 🏢 THE MASTER BLUEPRINT CLASS (The Manufacturing Mold)
# ============================================================
class Flight:
    # The Constructor Initialization Engine (Sets up the variables for EVERY new flight)
    def __init__(self, flight_number, destination, baseline_fare):
        self.number = flight_number
        self.dest = destination
        self.fare = baseline_fare
        self.passenger_manifest = []  # Running list tracking booked flyers

    # An Internal Method (A capability utility built right into the blueprint!)
    def display_flight_manifest(self):
        print(f"\n📊 --- ROUTE LOG FOR FLIGHT {self.number} --- 📊")
        print(f"Destination : {self.dest}")
        print(f"Seat Cost   : €{self.fare}")
        print(f"Total Flyers: {len(self.passenger_manifest)} booked")
        print(f"Manifest    : {', '.join(self.passenger_manifest) if self.passenger_manifest else 'Empty empty seat array'}")
        print("-----------------------------------------")

    def book_passenger(self, passenger_name):
        self.passenger_manifest.append(passenger_name)
        print(f"🎟️ SUCCESS! Seat locked for {passenger_name} on Flight {self.number}!")


# ============================================================
# 🏭 THE MANUFACTURING FLOOR (Creating Independent Objects)
# ============================================================

print("🛠️ Manufacturing individual flight objects from our master class blueprint...")

# We spawn two completely separate, independent flight engines out of the same mold!
flight_alpha = Flight("LH564", "Lagos, Nigeria", 664)
flight_beta = Flight("AF123", "Abuja, Nigeria", 607)

# --- OPERATING FLIGHT ALPHA ---
flight_alpha.book_passenger("Esosa")
flight_alpha.book_passenger("Amara")
flight_alpha.display_flight_manifest()

# --- OPERATING FLIGHT BETA ---
# Notice how flight_beta remains completely untouched by alpha's passengers!
flight_beta.display_flight_manifest()

print("\n✨ Object-Oriented setup architecture executed successfully! ✨")
