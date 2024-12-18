# Write a Python program to convert Celsius to Fahrenheit.
# =========================================================

# Step 1: User input
# yaha par jo 'celsius' likha hai yeh ek variable hai. Jaise hum JS ke time samajhte the, variable ek box jaisa hota hai jo data store karta hai.
# 'input()' ka use hum user se temperature poochhne ke liye karte hain.
# Note: 'input()' se jo value milti hai, woh string (text) hoti hai. 
# Hum 'float()' ka use isliye karte hain, taki user decimal value bhi de sake (e.g., 36.6). Agar aapko sirf whole number chahiye ho to 'int()' use karte hain.

celsius = float(input("Enter temperature in Celsius: "))

# Step 2: Conversion Formula
# Celsius se Fahrenheit convert karne ka simple formula hota hai: (°C × 9/5) + 32
# 'fahrenheit' ek variable hai jo calculate karega aur result store karega. 
# Humare paas do variables hain:
# 1. 'celsius': Yeh user ke input ko store karta hai.
# 2. 'fahrenheit': Yeh formula ke result ko store karega.

fahrenheit = (celsius * 9/5) + 32

# Step 3: Output Display
# 'print()' function ka use hum result display karne ke liye karte hain.
# f-string: Jab bhi hume variables ko ek string ke andar include karna hota hai, hum 'f-string' ka use karte hain.
# Example: Agar celsius ki value 25 hai, toh output hoga: "25.0°C is equal to 77.0°F"

print(f"{celsius}°C is equal to {fahrenheit}°F")
