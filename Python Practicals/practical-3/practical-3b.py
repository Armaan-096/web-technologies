# Write a python program to make use of following functions of math module: exp(), floor(), ceil(), factorial(), sqrt(), pow(), cos().
# =========================================================

import math  # Math module ko import karna. Yeh module mathematical operations perform karne ke liye built-in functions provide karta hai.

# Step 1: Exp function (e^x)
exp_result = math.exp(2)  # exp() function Euler's number 'e' ko raise karta hai power '2' tak. Yeh 'e^2' ka result dega.
print(f"exp(2) = {exp_result}")  # Iska output hoga 'exp(2) = 7.3890560989306495' jo e^2 ka result hai.

# Step 2: Floor function (rounds down to the nearest integer)
floor_result = math.floor(4.7)  # floor() function 4.7 ko nearest lower integer tak round karta hai. Yeh 4 dega.
print(f"floor(4.7) = {floor_result}")  # Output: 'floor(4.7) = 4' kyunki floor function fractional part ko discard karta hai.

# Step 3: Ceil function (rounds up to the nearest integer)
ceil_result = math.ceil(4.7)  # ceil() function 4.7 ko nearest upper integer tak round karta hai. Yeh 5 dega.
print(f"ceil(4.7) = {ceil_result}")  # Output: 'ceil(4.7) = 5' kyunki ceil function hamesha fractional part ko next integer tak round karta hai.

# Step 4: Factorial function (calculates x!)
factorial_result = math.factorial(5)  # factorial() function 5 ka factorial calculate karega. 5! = 5 * 4 * 3 * 2 * 1 = 120.
print(f"factorial(5) = {factorial_result}")  # Output: 'factorial(5) = 120', jo 5! ka result hai.

# Step 5: Square root function
sqrt_result = math.sqrt(16)  # sqrt() function 16 ka square root calculate karega. sqrt(16) = 4.
print(f"sqrt(16) = {sqrt_result}")  # Output: 'sqrt(16) = 4.0', jo square root of 16 hai.

# Step 6: Power function (x raised to the power y)
pow_result = math.pow(2, 3)  # pow() function 2 ko 3 tak power karega. 2^3 = 8.
print(f"pow(2, 3) = {pow_result}")  # Output: 'pow(2, 3) = 8.0', jo 2^3 ka result hai.

# Step 7: Cosine function (returns cosine of angle in radians)
cos_result = math.cos(math.pi / 3)  # cos() function 60 degrees ka cosine calculate karega. pi/3 radians = 60 degrees.
print(f"cos(pi/3) = {cos_result}")  # Output: 'cos(pi/3) = 0.5', kyunki cos(60 degrees) ka value 0.5 hota hai.
