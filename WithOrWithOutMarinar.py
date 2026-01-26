#Weather Branch

"""
 Returns and gives us a random weather condition
"""

import random

SPEED_LIMIT = 65  # mph
NORMAL_WAKE_TIME = 7 * 60  # 7:00 AM in minutes

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
    "Cloudy": 0.9,
    "Windy": 0.8,
    "Rainy": 0.7,
    "Foggy": 0.6,
    "Snowy": 0.5,
    "Stormy": 0.4
}

# How many minutes earlier the alarm should go off
weather_alarm_adjustment = {
    "Sunny": 0,
    "Cloudy": 5,
    "Windy": 10,
    "Rainy": 15,
    "Foggy": 20,
    "Snowy": 30,
    "Stormy": 45
}

condition = random.choice(list(weather.keys()))

# ----- CAR SYSTEM -----
multiplier = weather_speed_multiplier[condition]
safe_speed = int(SPEED_LIMIT * multiplier)

print(f"📡 Weather Scan complete: {condition}, {weather[condition]}")
print("🚗 Communicating with car systems...Connected")

if safe_speed == SPEED_LIMIT:
    print(f"✅ Conditions are great. You may drive up to {safe_speed} mph.")
elif safe_speed < SPEED_LIMIT * 0.6:
    print(f"🚨 Dangerous conditions detected! Max speed limited to {safe_speed} mph.")
else:
    print(f"⚠️ Reduced traction. Max safe speed is {safe_speed} mph.")

# ----- PHONE ALARM SYSTEM -----
print("\n📱 Communicating with phone alarm...Connected")

alarm_change = weather_alarm_adjustment[condition]
new_wake_time = NORMAL_WAKE_TIME - alarm_change

hour = new_wake_time // 60
minute = new_wake_time % 60

if alarm_change == 0:
    print("⏰ Weather is favorable. Alarm unchanged.")
else:
    print(f"⏰ Poor weather detected. Alarm moved earlier by {alarm_change} minutes.")
    print(f"🔔 New wake-up time: {hour}:{minute:02d} AM")
