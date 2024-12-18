# Python program to accept n elements from the user for arrays and arrange the elements in ascending order
# ==================================================================================================

# Step 1: Accept the number of elements (n) from the user
# Pehle hum user se puchenge ki kitne elements wo input dena chahta hai.
n = int(input("Enter the number of elements you want to input: "))  # 'input()' function se user se value lenge.

# Step 2: Initialize an empty list to store the elements
# Hum ek empty list create karenge jisme user ke input store karenge.
elements = []

# Step 3: Accept n elements from the user
# 'for' loop ka use karke hum 'n' elements ko accept karenge.
for i in range(n):
    # Har bar user se ek element input karenge.
    # 'input()' function se user input lenge, aur 'int()' se use integer mein convert karenge.
    num = int(input(f"Enter element {i+1}: "))  # Element number display hoga, jise user enter karega.
    elements.append(num)  # List me element add karenge.

# Step 4: Sort the elements in ascending order
# 'sort()' method ka use karte hain list ke elements ko ascending order mein arrange karne ke liye.
elements.sort()  # Sort function list ko ascending order mein arrange kar dega.

# Step 5: Display the sorted list
# Sorted list ko print karenge taaki user dekh sake ki elements kaise arrange hue hain.
print(f"The elements in ascending order are: {elements}")  # Final result ko display karenge.
