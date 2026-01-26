#Weather Branch

"""
 Returns and gives us a random weather condition
"""

import random

SPEED_LIMIT = 65  # mph

weather = {
    "Sunny": "Warm and bright",
    "Rainy": "Bring an umbrella",
    "Cloudy": "A bit gloomy",
    "Snowy": "Cold and cozy",
    "Windy": "Hold onto your hat",
    "Stormy": "Brace for a storm",
    "Foggy": "Low visibility"
}

# How much of the speed limit the car is allowed to use
weather_speed_multiplier = {
    "Sunny": 1.0,
    "Cloudy": 1.0,
    "Windy": 0.8,
    "Rainy": 0.7,
    "Foggy": 0.6,
    "Snowy": 0.5,
    "Stormy": 0.4
}

condition = random.choice(list(weather.keys()))

# Calculate safe speed
multiplier = weather_speed_multiplier[condition]
safe_speed = int(SPEED_LIMIT * multiplier)

# Output
print(f"📡 Weather check: {condition}, {weather[condition]}")
print("🚗 Communicating with car systems...Connected")

if safe_speed == SPEED_LIMIT:
    print(f"✅ Conditions are great. You may drive up to {safe_speed} mph.")
elif safe_speed < SPEED_LIMIT * 0.6:
    print(f"🚨 Dangerous conditions detected! Max speed limited to {safe_speed} mph.")
else:
    print(f"⚠️ Reduced traction. Max safe speed is {safe_speed} mph.")

