# Python Program to Demonstrate Operations on Tuples
# =========================================================

# Step 1: Creating a Tuple
# 'tuple' ek ordered collection hota hai jisme multiple elements store kiye jaate hain.
# Tuples ko parentheses '()' ke andar define kiya jaata hai.
# Yaha par 'fruits' ek tuple hai jisme different fruit names stored hain.

fruits = ("apple", "banana", "cherry")  # Creating a tuple

# Step 2: Accessing Tuple Elements
# Hum tuple ke elements ko index ke through access karte hain.
# Indexing zero-based hoti hai, matlab first element ka index 0, second ka 1, aur so on.
# Agar hum fruits[0] likhenge, toh woh first element "apple" ko return karega.

first_fruit = fruits[0]  # Accessing the first element
print(f"The first fruit is: {first_fruit}")

# Step 3: Slicing a Tuple
# Tuple ko slice karke hum uske ek part ko access kar sakte hain.
# Slicing me hum start index aur end index specify karte hain.
# Example: fruits[1:3] ka matlab hai second element se lekar third element tak, but third element include nahi hota.

sliced_fruits = fruits[1:3]  # Slicing the tuple from index 1 to 3 (excluding index 3)
print(f"Sliced fruits are: {sliced_fruits}")

# Step 4: Checking if an Element Exists in the Tuple
# Hum 'in' keyword ka use kar ke check kar sakte hain ki koi particular element tuple me exist karta hai ya nahi.

is_banana_present = "banana" in fruits  # Checking if 'banana' is in the tuple
print(f"Is banana present in the tuple? {is_banana_present}")

# Step 5: Tuple Concatenation
# Hum tuples ko concatenate kar sakte hain, jisme dono tuples ki values ko combine kiya jaata hai.

more_fruits = ("orange", "grape")  # Another tuple
all_fruits = fruits + more_fruits  # Concatenating two tuples
print(f"All fruits after concatenation: {all_fruits}")

# Step 6: Tuple Repetition
# Hum tuple ko repeat bhi kar sakte hain. Example: fruits * 2 will repeat the tuple twice.

repeated_fruits = fruits * 2  # Repeating the tuple twice
print(f"Repeated fruits are: {repeated_fruits}")

# Step 7: Getting the Length of a Tuple
# Hum 'len()' function ka use kar ke tuple ki length (number of elements) nikal sakte hain.

length_of_fruits = len(fruits)  # Getting the length of the tuple
print(f"The number of fruits in the tuple is: {length_of_fruits}")
