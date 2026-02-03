#Gasoline  Branch

# Gasoline Branch
import random 

random_number = random.randint(1, 100)
print("Scanning gas tank... Scan complete. Gas tank level:", random_number, "%")

if random_number < 25:
    print("Gas level below recommended level... please find a local gas station")
else:
    print("Gas level is sufficient")

if random_number <25:
    import random

    words = ["Cicle K", "The Local gas station", "Gas", "date", "elderberry"]

    chosen_words = random.sample(words, 3)

    print(chosen_words)
