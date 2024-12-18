#  Python Program to demonstrates operations on dictionary
# =====================================================================

# Step 1: Creating a dictionary
# Hum ek dictionary create karenge jisme kuch initial key-value pairs honge.
my_dict = {
    "name": "Alice",  # Key 'name' with value 'Alice'
    "age": 25,        # Key 'age' with value 25
    "city": "New York" # Key 'city' with value 'New York'
}

# Step 2: Accessing values in the dictionary
# Hum dictionary se values ko keys ke through access kar sakte hain.
# 'get()' method se hum safely value ko access kar sakte hain, agar key nahi mili toh default value return karte hain.
name = my_dict.get("name")  # Access the value for key 'name'
print(f"Name: {name}")  # Output: Alice

# Agar key directly use karna hai toh hum '[]' ka use kar sakte hain.
age = my_dict["age"]  # Access the value for key 'age'
print(f"Age: {age}")  # Output: 25

# Step 3: Adding a new key-value pair
# Hum nayi key-value pair bhi dictionary mein add kar sakte hain.
my_dict["profession"] = "Engineer"  # Adding a new key 'profession' with value 'Engineer'
print(f"Updated Dictionary: {my_dict}")  # Output: {'name': 'Alice', 'age': 25, 'city': 'New York', 'profession': 'Engineer'}

# Step 4: Updating an existing value
# Agar hum kisi key ke liye existing value ko update karna chahte hain, toh directly key ko use karke new value assign kar sakte hain.
my_dict["age"] = 26  # Update the value for key 'age' to 26
print(f"Updated Dictionary after changing age: {my_dict}")  # Output: {'name': 'Alice', 'age': 26, 'city': 'New York', 'profession': 'Engineer'}

# Step 5: Deleting a key-value pair
# Hum 'del' statement ka use karke kisi key-value pair ko delete kar sakte hain.
del my_dict["city"]  # Deleting the key 'city' and its associated value
print(f"Dictionary after deleting city: {my_dict}")  # Output: {'name': 'Alice', 'age': 26, 'profession': 'Engineer'}

# Step 6: Checking if a key exists in the dictionary
# Hum 'in' keyword ka use karke check kar sakte hain ki key dictionary mein exist karti hai ya nahi.
if "age" in my_dict:
    print("Age exists in the dictionary.")  # Output: Age exists in the dictionary.
else:
    print("Age does not exist in the dictionary.")

# Step 7: Iterating over the dictionary
# Hum dictionary ke keys aur values par iterate kar sakte hain.
print("Iterating over keys and values:")
for key, value in my_dict.items():
    print(f"{key}: {value}")

# Step 8: Clearing all elements from the dictionary
# Agar hum dictionary ko completely empty karna chahte hain, toh 'clear()' method ka use karte hain.
my_dict.clear()  # This will remove all key-value pairs from the dictionary
print(f"Dictionary after clearing: {my_dict}")  # Output: {}
