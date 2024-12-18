
# Python Program to Check whether a string starts and ends with the same character using regex
# =========================================================

# Importing the 're' module to work with regular expressions
import re
# Step 1: Input string
# 'input()' function ka use user se string lene ke liye kiya jaata hai.
# User ko prompt diya gaya hai ki woh ek string enter kare.

string = input("Enter a string: ")

# Step 2: Regular Expression Explanation
# Regular expressions (regex) ek special syntax hota hai jiska use hum strings ko match, search, replace karne ke liye karte hain.
# Regex me hum different patterns define karte hain jo input string se match hote hain.
# Yahan hum check karna chahte hain ki string ke first aur last character same hain ya nahi.
# Humne yeh regex pattern use kiya hai:
# r"^(.)\1$"  
# 'r' ka matlab hai raw string, jo ki regex special characters ko escape karne se bachata hai.
# Pattern '^(.)\1$' ka breakdown:
# 1. '^' - Yeh anchor hota hai jo string ke start ko indicate karta hai.
# 2. '(.)' - Yeh ek capturing group hai jo string ka first character capture karega.
# 3. '\1' - Yeh reference hai jo first captured character ko match karta hai, yani string ka last character.
# 4. '$' - Yeh anchor hai jo string ke end ko indicate karta hai.
# Iska matlab hai: "String ke starting aur ending character ko match karo, aur wo same hone chahiye."

pattern = r"^(.)\1$"  # Defining the regex pattern

# Step 3: Applying the regex pattern to the string
# 're.match()' function ka use hum karte hain ki string ko regex pattern ke saath match kiya jaaye.
# Agar string pattern se match hoti hai, toh 're.match()' object return karega (True).
# Agar match nahi hota, toh 'None' return hota hai (False).

if re.match(pattern, string):
    print("The string starts and ends with the same character.")
else:
    print("The string does not start and end with the same character.")
