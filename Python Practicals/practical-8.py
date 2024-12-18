# Python Program to demonstrate operations on List
# =============================================================

# Step 1: Creating a list
# Hum ek list create karenge jo kuch initial elements ke saath ho.
my_list = [1, 2, 3, 4, 5]  # List with elements 1 to 5
print(f"Original List: {my_list}")  # Output: [1, 2, 3, 4, 5]

# Step 2: Accessing list elements
# Hum list ke elements ko index ke through access kar sakte hain. Python mein index 0 se start hota hai.
# my_list[0] will give us the first element.
first_element = my_list[0]  # Access the first element
print(f"First element: {first_element}")  # Output: 1

# Negative indexing se hum list ke elements ko reverse order mein bhi access kar sakte hain.
last_element = my_list[-1]  # Access the last element using negative index
print(f"Last element: {last_element}")  # Output: 5

# Step 3: Modifying list elements
# Hum list ke kisi bhi element ko modify kar sakte hain, bas us index ko target karke.
my_list[2] = 10  # Changing the 3rd element (index 2) from 3 to 10
print(f"List after modification: {my_list}")  # Output: [1, 2, 10, 4, 5]

# Step 4: Adding elements to a list
# Hum list mein new elements ko add kar sakte hain. 'append()' se ek element add hota hai end mein.
my_list.append(6)  # Adding 6 to the end of the list
print(f"List after appending 6: {my_list}")  # Output: [1, 2, 10, 4, 5, 6]

# 'insert()' se hum kisi specific position par element insert kar sakte hain.
my_list.insert(2, 15)  # Inserting 15 at index 2
print(f"List after inserting 15 at index 2: {my_list}")  # Output: [1, 2, 15, 10, 4, 5, 6]

# Step 5: Removing elements from the list
# Hum list se elements ko 'remove()' ya 'pop()' se hata sakte hain.
# 'remove()' se hum specific value ko remove karte hain.
my_list.remove(10)  # Removing the first occurrence of 10
print(f"List after removing 10: {my_list}")  # Output: [1, 2, 15, 4, 5, 6]

# 'pop()' se hum element ko index ke basis par remove kar sakte hain.
popped_element = my_list.pop()  # Removes and returns the last element (6 in this case)
print(f"Popped element: {popped_element}")  # Output: 6
print(f"List after popping: {my_list}")  # Output: [1, 2, 15, 4, 5]

# Step 6: List slicing
# Hum list ke kisi bhi range ko slice kar sakte hain. Slicing se ek nayi list milti hai.
sliced_list = my_list[1:4]  # Getting elements from index 1 to 3 (4th index excluded)
print(f"Sliced list from index 1 to 3: {sliced_list}")  # Output: [2, 15, 4]

# Step 7: List iteration
# Hum 'for' loop ka use karke list ke har element ko iterate kar sakte hain.
print("Iterating through the list:")
for item in my_list:
    print(item)  # Output: 1, 2, 15, 4, 5 (each on a new line)

# Step 8: Checking if an element exists in the list
# Hum 'in' keyword ka use karke check kar sakte hain ki koi specific element list mein hai ya nahi.
if 15 in my_list:
    print("15 is in the list.")  # Output: 15 is in the list.
else:
    print("15 is not in the list.")

# Step 9: List length
# Hum 'len()' function ka use karke list ki length ya size jaan sakte hain.
list_length = len(my_list)  # Getting the number of elements in the list
print(f"Length of the list: {list_length}")  # Output: 5

# Step 10: Sorting a list
# Hum 'sort()' method ka use kar ke list ko ascending order mein sort kar sakte hain.
my_list.sort()  # Sorting the list in ascending order
print(f"Sorted list: {my_list}")  # Output: [1, 2, 4, 5, 15]

# Agar descending order mein sort karna ho toh 'reverse=True' ka use kar sakte hain.
my_list.sort(reverse=True)  # Sorting the list in descending order
print(f"Sorted list in descending order: {my_list}")  # Output: [15, 5, 4, 2, 1]

# Step 11: Reversing a list
# Hum 'reverse()' method ka use karke list ko reverse order mein kar sakte hain.
my_list.reverse()  # Reversing the list
print(f"Reversed list: {my_list}")  # Output: [1, 2, 4, 5, 15]

# Step 12: Clearing the list
# Hum 'clear()' method ka use kar ke list ko completely empty kar sakte hain.
my_list.clear()  # This will remove all elements from the list
print(f"List after clearing: {my_list}")  # Output: []
