import numpy as np

# Create a random array of 10 integers between 1 and 100.
random_array = np.random.randint(1, 100, size=10)
print("Original random array:", random_array)

# Sort the array
sorted_array = np.sort(random_array)
print("\nSorted array:", sorted_array)

# Reshape the array into different dimensions
try:
    # Reshape to 2x5
    reshaped_2x5 = sorted_array.reshape(2, 5)
    print("\nReshaped to 2x5 matrix:\n", reshaped_2x5)
    
    # Reshape to 5x2
    reshaped_5x2 = sorted_array.reshape(5, 2)
    print("\nReshaped to 5x2 matrix:\n", reshaped_5x2)
    
except ValueError as e:
    print("\nError:", e)
    print("Cannot reshape array of size", len(sorted_array), 
          "into the requested dimensions")

print("\nAdditional reshaping examples:")
try:
    # Reshaping with 12 elements
    larger_array = np.random.randint(1, 100, size=12)
    sorted_larger = np.sort(larger_array)
    print("\nArray with 12 elements:", sorted_larger)
    
    # Possible reshapes for 12 elements
    print("\nReshaped to 3x4:\n", sorted_larger.reshape(3, 4))
    print("\nReshaped to 4x3:\n", sorted_larger.reshape(4, 3))
    print("\nReshaped to 6x2:\n", sorted_larger.reshape(6, 2))
    
except ValueError as e:
    print("Reshaping error:", e)
