# Python program to demonstrate string functions.

# Python program to demonstrate string functions
# ===========================================================

# Strings kya hai?
# String ek sequence hota hai characters ka. Matlab, koi bhi cheez jo text form mein ho, jaise "Hello", "Python", "123", etc., woh sab strings hote hain.
# String ko hum single quotes (' ') ya double quotes (" ") ke andar likhte hain.

# Step 1: Creating a string
my_string = "Hello, Python!"  # yeh ek string hai jisme characters hain "H", "e", "l", "l", "o", ",", " " (space), "P", "y", "t", "h", "o", "n", "!"

# Step 2: Length of string using len()
string_length = len(my_string)  # len() function string ke andar kitne characters hain woh count karta hai.
print(f"Length of the string: {string_length}")  # Output: 'Length of the string: 14', kyunki "Hello, Python!" mein 14 characters hain.

# Step 3: Convert string to lowercase using lower()
lowercase_string = my_string.lower()  # lower() function string ko small letters mein convert kar deta hai.
print(f"String in lowercase: {lowercase_string}")  # Output: 'hello, python!' - Sab characters small ho gaye hain.

# Step 4: Convert string to uppercase using upper()
uppercase_string = my_string.upper()  # upper() function string ko capital letters mein convert kar deta hai.
print(f"String in uppercase: {uppercase_string}")  # Output: 'HELLO, PYTHON!' - Sab characters capital ho gaye hain.

# Step 5: Replace a substring using replace()
replaced_string = my_string.replace("Python", "World")  # replace() function kisi word ko doosre word se replace karta hai.
print(f"Replaced string: {replaced_string}")  # Output: 'Hello, World!' - 'Python' ko 'World' se replace kiya gaya hai.

# Step 6: Check if string starts with a specific substring using startswith()
starts_with_hello = my_string.startswith("Hello")  # startswith() function check karta hai ki string 'Hello' se start hoti hai ya nahi.
print(f"Does the string start with 'Hello'? {starts_with_hello}")  # Output: 'True' - string 'Hello, Python!' 'Hello' se start hoti hai.

# Step 7: Check if string ends with a specific substring using endswith()
ends_with_exclamation = my_string.endswith("!")  # endswith() function check karta hai ki string '!' se end hoti hai ya nahi.
print(f"Does the string end with '!'? {ends_with_exclamation}")  # Output: 'True' - string 'Hello, Python!' '!' pe end hoti hai.

# Step 8: Find the position of a substring using find()
position = my_string.find("Python")  # find() function substring ke first occurrence ki position return karta hai.
print(f"Position of 'Python' in the string: {position}")  # Output: 'Position of 'Python' in the string: 7' - 'Python' 'Hello, ' ke baad 7th position par start hota hai.

# Step 9: Split string into a list of substrings using split()
split_string = my_string.split(",")  # split() function string ko ek specific separator ke basis par split karta hai aur list return karta hai.
print(f"String after split: {split_string}")  # Output: ['Hello', ' Python!'] - string ko ',' ke basis par split kiya gaya hai.

# Step 10: Strip leading/trailing spaces using strip()
string_with_spaces = "   Hello, Python!   "  # String ke dono sides pe spaces hain.
stripped_string = string_with_spaces.strip()  # strip() function leading (starting) aur trailing (ending) spaces ko hata deta hai.
print(f"String after stripping spaces: '{stripped_string}'")  # Output: 'Hello, Python!' - spaces ko hata diya gaya hai.