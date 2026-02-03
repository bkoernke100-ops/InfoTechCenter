#Gas Branch
import random
import time

# -----------------------------
# Scan gas tank
# -----------------------------
gas_level = random.randint(1, 100)
print("Scanning gas tank... Scan complete.")
print("Gas tank level:", gas_level, "%\n")

# -----------------------------
# If gas is low, search stations
# -----------------------------
if gas_level < 25:
    print("⚠️ Gas level below recommended level!")
    print("Searching for nearby gas stations...\n")

    # Gas station data
    gas_stations = {
        "Circle K": {},
        "The Local Gas Station": {},
        "Certified": {},
        "Chevron": {},
        "Clark Brands": {}
    }

    # Assign random info to each station
    for station in gas_stations:
        gas_stations[station]["distance"] = round(random.uniform(0.5, 10.0), 2)  # miles
        gas_stations[station]["price"] = round(random.uniform(3.20, 4.50), 2)    # $ per gallon
        gas_stations[station]["open"] = random.choice([True, False])             # open or closed
        gas_stations[station]["snacks"] = random.choice([True, False])           # snacks available

    # -----------------------------
    # Find best stations
    # -----------------------------
    nearest_station = min(gas_stations, key=lambda x: gas_stations[x]["distance"])
    cheapest_station = min(gas_stations, key=lambda x: gas_stations[x]["price"])

    # -----------------------------
    # Display station info
    # -----------------------------
    for station, info in gas_stations.items():
        status = "Open" if info["open"] else "Closed"
        snacks = "Snacks Available" if info["snacks"] else "No Snacks"

        print(
            f"{station}: "
            f"{info['distance']} miles | "
            f"${info['price']} | "
            f"{status} | "
            f"{snacks}"
        )

    # -----------------------------
    # Summary
    # -----------------------------
    print("\n🚩 Nearest gas station:", nearest_station)
    print("💰 Cheapest gas:", cheapest_station)

    # -----------------------------
    # Alarm reminder
    # -----------------------------
    print("\n⏰ Alarm set: GET GAS NOW!")
    time.sleep(1)
    print("⏰⏰⏰ BEEP BEEP! Low fuel warning! ⏰⏰⏰")

else:
    print("✅ Gas level is sufficient. No need to stop for gas.")
