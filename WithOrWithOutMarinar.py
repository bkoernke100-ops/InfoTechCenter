#Main Branch

#BetaTestDev

# -------------------------------------------------
# Welcome Branch
# Simulates a boot-up sequence with colored text
# Developer: Brennen Koernke
# -------------------------------------------------

# Libraries Imported Here
import sys      # Used for writing to the terminal without new lines
import time     # Used to create delays (sleep)

# -------------------------------------------------
# ANSI color codes for terminal text styling
# These allow colored and bold text output
# -------------------------------------------------
RESET = "\033[0m"     # Resets text color/style back to default
GREEN = "\033[92m"   # Green text (success messages)
CYAN = "\033[96m"    # Cyan text (titles)
YELLOW = "\033[93m"  # Yellow text (loading animation)
RED = "\033[91m"     # Red text (errors or warnings)
BOLD = "\033[1m"     # Bold text style

# -------------------------------------------------
# Display welcome and version information
# -------------------------------------------------
print(f"\n{CYAN}{BOLD}Welcome Branch - Developer: Brennen Koernke{RESET}")
print(f"\n{GREEN}Welcome to Info Tech Center v.1.0{RESET}")

# -------------------------------------------------
# Initialize loop counters
# x controls how long the boot animation runs
# ellipsis controls how many dots appear (.)
# -------------------------------------------------
x = 0
ellipsis = 0

# -------------------------------------------------
# Boot-up animation loop
# Runs until x reaches 20 iterations
# -------------------------------------------------
while x != 20:
    x += 1  # Increment loop counter

    # Build the boot message with animated dots
    ellipsisMessage = f"{YELLOW}InfoTechCenter OS Booting{'.' * ellipsis}{RESET}"
    ellipsis += 1

    # Write the message on the same line (carriage return)
    # \r moves cursor to start of line
    # \033[K clears the line
    sys.stdout.write("\r\033[K" + ellipsisMessage)
    sys.stdout.flush()  # Forces the output to display immediately

    # Pause to control animation speed
    time.sleep(0.5)

    # Reset dot count after reaching 3 dots
    if ellipsis == 4:
        ellipsis = 0

    # -------------------------------------------------
    # Final message once boot sequence is complete
    # -------------------------------------------------
    if x == 20:
        print(f"\n{GREEN}{BOLD}Operating System Booted Up - Retina Scanned - Access Granted{RESET}")



# Weather Branch
# This program simulates how weather conditions affect driving speed
# and wake-up time using random selection.

"""
Returns and gives us a random weather condition
"""

import random  # Used to randomly select a weather condition

# ---------------- CONSTANTS ----------------

SPEED_LIMIT = 65  # Maximum legal driving speed in mph
NORMAL_WAKE_TIME = 7 * 60  # Normal wake-up time (7:00 AM) stored in minutes

# ---------------- WEATHER DATA ----------------

# Dictionary that maps weather conditions to short descriptions
weather = {
    "Sunny": "Warm and bright",
    "Rainy": "Bring an umbrella",
    "Cloudy": "A bit gloomy",
    "Snowy": "Cold and cozy",
    "Windy": "Hold onto your hat",
    "Stormy": "Brace for a storm",
    "Foggy": "Low visibility"
}

# Dictionary that controls how much of the speed limit
# is safe to use based on the weather
weather_speed_multiplier = {
    "Sunny": 1.0,     # Full speed allowed
    "Cloudy": 1.0,
    "Windy": 0.8,     # Reduced speed for safety
    "Rainy": 0.7,
    "Foggy": 0.6,
    "Snowy": 0.5,
    "Stormy": 0.4
}

# Dictionary that determines how many minutes earlier
# the alarm should go off due to bad weather
weather_alarm_adjustment = {
    "Sunny": 0,
    "Cloudy": 0,
    "Windy": 10,
    "Rainy": 15,
    "Foggy": 20,
    "Snowy": 30,
    "Stormy": 45
}

# Randomly select one weather condition from the dictionary keys
condition = random.choice(list(weather.keys()))

# ---------------- CAR SYSTEM ----------------

# Get the speed multiplier for the current weather
multiplier = weather_speed_multiplier[condition]

# Calculate the safe driving speed based on weather
safe_speed = int(SPEED_LIMIT * multiplier)

# Display the selected weather condition and description
print(f"\n📡 Weather Scan complete: {condition}, {weather[condition]}")
print("🚗 Connecting with car systems...Connected")

# Decide which driving message to show based on safe speed
if safe_speed == SPEED_LIMIT:
    print(f"✅ Conditions are great. You may drive up to {safe_speed} mph.")
elif safe_speed < SPEED_LIMIT * 0.6:
    print(f"🚨 Dangerous conditions detected! Max speed limited to {safe_speed} mph.")
else:
    print(f"⚠️ Reduced max speed... Max safe speed is {safe_speed} mph.")

# ---------------- PHONE ALARM SYSTEM ----------------

print("\n📱 Connecting with phone alarm...Connected")

# Get how much earlier the alarm should go off
alarm_change = weather_alarm_adjustment[condition]

# Calculate the new wake-up time in minutes
new_wake_time = NORMAL_WAKE_TIME - alarm_change

# Convert total minutes back into hours and minutes
hour = new_wake_time // 60
minute = new_wake_time % 60

# Output alarm status based on whether the time changed
if alarm_change == 0:
    print("⏰ Weather is favorable. Alarm unchanged.")
else:
    print(f"⏰ Poor weather detected. Alarm moved earlier by {alarm_change} minutes.")
    print(f"🔔 New wake-up time: {hour}:{minute:02d} AM")




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

