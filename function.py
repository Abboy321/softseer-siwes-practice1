# Function 1: Add two numbers
def add(a, b):
    return a + b
 
# Function 2: Greet a person
def greet(name):
    print("Hello, " + name + "!")
 
# Function 3: Check if a number is even
def is_even(number):
    if number % 2 == 0:
        print(str(number) + " is even")
    else:
        print(str(number) + " is odd")
 
# Function 4: Find the larger of two numbers
def find_largest(x, y):
    if x > y:
        return x
    else:
        return y
 
# Function 5: Print a number times table
def times_table(n):
    print("Times table for " + str(n) + ":")
    for i in range(1, 6):
        print(str(n) + " x " + str(i) + " = " + str(n * i))
 
 
# --- Invoking all five functions ---
 
greet("Abubakar")
 
result = add(8, 5)
print("8 + 5 =", result)
 
is_even(4)
is_even(7)
 
biggest = find_largest(20, 35)
print("The largest number is", biggest)
 
times_table(3)