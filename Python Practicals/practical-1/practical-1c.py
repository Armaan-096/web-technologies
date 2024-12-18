# Write a Python program for Sum of squares of first n natural numbers.
# ==========================================================================

# Step 1: User Input
# Hum user se 'n' ki value lenge. Yeh 'n' bataega ki kitne natural numbers ka sum hum calculate karna hai.
# 'int()' ka use kiya hai taaki hum integer value le sakein.

n = int(input("Enter a number n: "))  # User se 'n' ki value lena, jo bataega ki kitne numbers ka sum calculate karna hai.

# Step 2: Calculate Sum of Squares
# Hum sum of squares ka formula use karenge: 
# Sum of squares of first n natural numbers = 1^2 + 2^2 + 3^2 + ... + n^2
# Isko hum for loop ke through calculate karenge.

sum_of_squares = 0  # Initializing variable to store the sum of squares.

# Loop to calculate sum of squares (loop ek topic hai pura jo easily clear nhi hoga toh yeh line yaad krlena filhaal)
for i in range(1, n + 1):  # 'range(1, n+1)' ensures that we get numbers from 1 to n.
    sum_of_squares += i**2  # Adding square of each number to sum_of_squares.

# Step 3: Display the result
# Hum final result ko print karenge.

print(f"The sum of squares of first {n} natural numbers is: {sum_of_squares}")  

# for eg : user ne number daala 3 to usko calculate krega yeh basically is tarah : 1 ka square 1 hi hota hai then 2 ka square 4 aayega aur last 3 ka square 9 aayega toh 1 + 4 + 9 = 14
