# Python program to accept 20 elements from the user for arrays and print the sum of all odd numbers
# ==================================================================================================

# Step 1: Initialize an empty list to store user input
# Hum 'numbers' list create kar rahe hain jisme user ke input ko store karenge.
# Yeh ek empty list hai, jisme hum numbers ko ek-ek karke add karenge.
numbers = []

# Step 2: Accept 20 elements from the user
# 'for' loop ka use kar rahe hain jisme hum 20 elements input karenge.
for i in range(20):
    # Har bar user se ek number input karenge.
    # 'input()' function se user se value milegi, aur 'int()' se us value ko integer type me convert karenge.
    num = int(input(f"Enter element {i+1}: "))  # User ko prompt dikhaye jaega, jisme wo element number dekh sakte hain (1 to 20)
    numbers.append(num)  # Har ek number ko 'numbers' list me add karenge. list.append() function ka use karte hain.

# Step 3: Initialize variable to calculate the sum of all odd numbers
# Hum 'sum_of_odds' naam ka ek variable initialize kar rahe hain jisme odd numbers ka sum store karenge.
# Initially, sum_of_odds ko 0 set kar rahe hain.
sum_of_odds = 0

# Step 4: Loop through each number in the list and check if it is odd
# Ab hum list ke har element ko check karenge ki kya wo odd hai ya nahi.
for num in numbers:
    # Odd number ka check karne ke liye hum modulus operator (%) ka use karte hain.
    # Agar num % 2 != 0 hota hai, toh number odd hai (yani remainder 1 aata hai).
    if num % 2 != 0:  # Agar number odd hai (yani 2 se divide karne par remainder 1 aata hai)
        sum_of_odds += num  # Agar number odd hai, toh us number ko sum_of_odds me add karenge.

# Step 5: Display the result
# Jab sum_of_odds me sare odd numbers ka sum ho jayega, tab usko print karenge.
# Hum f-string ka use kar rahe hain taaki variable ko string me directly include kar sakein.
print(f"The sum of all odd numbers is: {sum_of_odds}")  # Result ko print karenge.
