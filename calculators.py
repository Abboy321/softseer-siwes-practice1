# Get three numbers from the user
first = float(input("Enter the first number: "))
second = float(input("Enter the second number: "))
third = float(input("Enter the third number: "))

# Perform calculations
sum_result = first + second + third
average_result = sum_result / 3
product_result = first * second * third

# Display the results
print("\n--- Results ---")
print(f"Sum:     {sum_result}")
print(f"Average: {average_result}")
print(f"Product: {product_result}")
input("\nPress Enter to close...")