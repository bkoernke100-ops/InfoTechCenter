#Weather Branch

"""
 Returns and gives us a random weather condition
"""

import random

weather = {
    "Sunny": "Warm and bright",
    "Rainy": "Bring an umbrella",
    "Cloudy": "A bit gloomy",
    "Snowy": "Cold and cozy",
    "Windy": "Hold onto your hat",
    "Stormy": "Brace for a storm",
    "Foggy": "Low visibility"
}

condition = random.choice(list(weather.keys()))
print(f"The weather today is {condition}, {weather[condition]}")
