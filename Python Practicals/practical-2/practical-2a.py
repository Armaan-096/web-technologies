# Write a python program to demonstrate use of recursive function.
# ================================================================


# Normal Function : ko hum define karte hain taaki ek baar likhkar use multiple baar call kar sakein. Yeh ek reusable code block hota hai jo specific task ko perform karta hai.____

# eg : Socho aapke paas ek magic box hai. Aap kuch daalte ho us box mein, aur woh box aapko kuch dekar wapas kar deta hai. Jab bhi aap wahi cheez us box mein daaloge, woh hamesha aapko wahi cheez dega......
# Jaise maan lo, aapne ek magic box banaya hai jo aapka naam lene par "Hello, [aapka naam]!" bolta hai. Har baar jab aap apna naam daalte ho, woh box waise hi bolta hai.

# Recursive function : wo function hota hai jo apne aap ko call karta hai. Isme ek base case hota hai, jaha recursion band hoti hai, aur ek recursive case hota hai jaha function apne aap ko chhote input ke sath call karta hai.___

# eg : Ab socho, ek aur magic box hai, lekin yeh box thoda alag hai. Yeh box apne aap ko call karta hai! Jaise agar aapko ek se lekar kisi number tak ginti karni ho, toh yeh box apne aap ko chhoti ginti ke saath phir se call karega.
# Maan lo, aapko staircase ke steps count karne hain, toh har step ko count karne ke baad, har step apne aap ko next step ke liye call karega. Jab tak wo last step nahi aa jata!

# Step 1: Define the recursive function to calculate factorial
def factorial(n):
    # Step 2: Base Case - agar n 0 ya 1 ho toh return 1 (kyunki 0! = 1! = 1)
    if n == 0 or n == 1:
        return 1
    else:
        # Step 3: Recursive Case - function apne aap ko call karega n-1 ke sath
        return n * factorial(n - 1)

# Step 4: Take input from the user
num = int(input("Enter a number to find its factorial: "))  # User se number lena

# Step 5: Call the recursive factorial function and display the result
result = factorial(num)  # factorial function ko call karke result lena
print(f"The factorial of {num} is: {result}")  # Result ko print karna
