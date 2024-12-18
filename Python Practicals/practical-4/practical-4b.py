# Python program to remove punctuation from string
# ======================================================

import string  # Importing string module which contains punctuation characters

# Step 1: Define a string with punctuation
my_string = "Hello, World! How's everything going? Good; I hope."

# Step 2: Use string.punctuation to get all punctuation characters
punctuation = string.punctuation  # string.punctuation gives a string containing all punctuation characters like !, ", #, $, %, etc.

# Step 3: Remove punctuation from the string using a loop and list comprehension
clean_string = ''.join(char for char in my_string if char not in punctuation)  # Checking each character, and if it's not a punctuation, add it to the result

# Step 4: Display the cleaned string
print(f"Original string: {my_string}")
print(f"String after removing punctuation: {clean_string}")
