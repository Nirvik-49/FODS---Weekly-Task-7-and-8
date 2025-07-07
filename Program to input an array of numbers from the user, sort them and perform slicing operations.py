# Taking input from the user
print("Enter at least 10 numbers separated by spaces:")
while True:
    user_input = input().split()
    if len(user_input) >= 10:
        try:
            numbers = [float(num) for num in user_input]
            break
        except ValueError:
            print("Please enter valid numbers only. Try again:")
    else:
        print("Please enter at least 10 numbers. Try again:")

# Sorting the array
sorted_numbers = sorted(numbers)

# Performing slicing operations
slice_2_5 = sorted_numbers[2:6]    # Elements from index 2 to 5 inclusive
slice_5_8 = sorted_numbers[5:9]    # Elements from index 5 to 8 inclusive
slice_2_9 = sorted_numbers[2:10]   # Elements from index 2 to 9 inclusive

# Displaying results

print("\nOriginal numbers:", numbers)
print("Sorted numbers:", sorted_numbers)
print("\nSlicing Results:")
print("Elements from index 2 to 5:", slice_2_5)
print("Elements from index 5 to 8:", slice_5_8)
print("Elements from index 2 to 9:", slice_2_9)
