# Write a python program to check Armstrong Number using function.

# Armstrong Number: Ek Armstrong number wo number hota hai jisme us number ki har digit ka cube (ya square ya kisi power ka) le kar un sab ka sum us number ke barabar hota hai.
# eg : Agar 153 ko lein:

# 1 ka cube = 1
# 5 ka cube = 125
# 3 ka cube = 27 
# Sum = 1 + 125 + 27 = 153 
# Toh 153 ek Armstrong number hai. matlab add karne pr 3no number same aagaye 1 5 aur 3 jo cube hum liye the toh inhe armstrong number kehte hai!!

# Armstrong Number check karne ka function
def is_armstrong(number):
    # Step 1: Number ko string mein convert karenge taaki har digit ko alag se access kar sakein
    digits = str(number)
    num_digits = len(digits)  # Total digits ki ginti karenge
    
    # Step 2: Har digit ka power le kar sum karenge
    sum_of_powers = 0
    for digit in digits:
        sum_of_powers += int(digit) ** num_digits  # Har digit ko power ke saath add karenge
    
    # Step 3: Agar sum_of_powers aur original number barabar hain, toh Armstrong number hai
    if sum_of_powers == number:
        return True
    else:
        return False

# Step 4: User se number lena
num = int(input("Enter a number to check if it is an Armstrong number: "))

# Step 5: Function ko call karke result dikhana
if is_armstrong(num):
    print(f"{num} is an Armstrong number!")
else:
    print(f"{num} is not an Armstrong number.")
