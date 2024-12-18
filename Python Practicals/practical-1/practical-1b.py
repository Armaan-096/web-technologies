# Write a Python program to calculate Simple Interest and Compound Interest.
# ==========================================================================

# Step 1: User Input
# Hum user se 3 inputs lenge: Principal amount, Rate of interest, aur Time period.
# 'float()' ka use kiya hai taki values decimal ho sakti hain, jaise 1000.50 ya 5.5%.
# Principal: Initial amount jo invest ya borrow kiya gaya hai.
# Rate: Annual interest rate.
# Time: Duration (in years) jiske liye interest calculate karna hai.

principal = float(input("Enter the Principal amount: "))
rate = float(input("Enter the Rate of interest (in %): "))
time = float(input("Enter the Time (in years): "))

# Step 2: Calculate Simple Interest
# Formula: SI = (Principal × Rate × Time) / 100
# Simple Interest ko calculate karne ke liye directly formula ka use kiya gaya hai.

simple_interest = (principal * rate * time) / 100

# Step 3: Calculate Compound Interest
# Formula: CI = Principal × (1 + Rate/100)^Time - Principal
# Compound Interest calculate karne ke liye hum exponentiation operator (`**`) ka use karte hain.

compound_interest = principal * ((1 + rate / 100) ** time) - principal

# Step 4: Display the Results
# Output ko f-string ke through display kiya gaya hai, taki result clear aur readable ho.

print(f"Simple Interest is: {simple_interest}")
print(f"Compound Interest is: {compound_interest}")
