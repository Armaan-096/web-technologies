# Python program to generate a random number using random module
# ===============================================================

# Random number generate karne ke liye random module ko import karenge
import random

# Step 1: Generate random number between 1 and 100
# random.randint(1, 100) ke through hum 1 se 100 ke beech ka random number generate karenge
# Example: Agar hum Ludo game mein 1 se 6 tak random number chahte hain, toh hum is range ko change kar sakte hain.
random_number = random.randint(1, 100)  

# Step 2: Display the random number
print(f"The random number generated between 1 and 100 is: {random_number}")
