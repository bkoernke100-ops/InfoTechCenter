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
print(f"📡 Weather Scan complete: {condition}, {weather[condition]}")
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
