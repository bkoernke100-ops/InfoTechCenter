#Gasoline  Branch

# Gasoline Branch
import random 

random_number = random.randint(1, 100)
print("Scanning gas tank... Scan complete. Gas tank level:", random_number, "%")

if random_number < 25:
    print("Gas level below recommended level... please find the nearest gas station")
else:
    print("Gas level is sufficient")

if random_number <25: