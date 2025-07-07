import numpy as np

def input_matrix(rows, cols):
    """Function to input a matrix of given dimensions."""
    
    matrix = []
    print(f"Enter the elements of the {rows}x{cols} matrix row by row:")
    for i in range(rows):
        while True:
            try:
                row = list(map(float, input(f"Row {i + 1}: ").split()))
                if len(row) != cols:
                    raise ValueError(f"Please enter exactly {cols} elements.")
                matrix.append(row)
                break
            except ValueError as e:
                print(e)
    return np.array(matrix)

def main():
    
    # Input dimensions for the first matrix
    
    rows1 = int(input("Enter the number of rows for the first matrix: "))
    cols1 = int(input("Enter the number of columns for the first matrix: "))
    matrix1 = input_matrix(rows1, cols1)

    # Input dimensions for the second matrix
    
    rows2 = int(input("Enter the number of rows for the second matrix: "))
    cols2 = int(input("Enter the number of columns for the second matrix: "))
    matrix2 = input_matrix(rows2, cols2)

    # Perform matrix operations with validation
    try:
        # Addition
        if matrix1.shape == matrix2.shape:
            addition_result = matrix1 + matrix2
            print("\nAddition Result:\n", addition_result)
        else:
            raise ValueError("Matrix addition requires both matrices to have the same dimensions.")

        # Subtraction
        if matrix1.shape == matrix2.shape:
            subtraction_result = matrix1 - matrix2
            print("\nSubtraction Result:\n", subtraction_result)
        else:
            raise ValueError("Matrix subtraction requires both matrices to have the same dimensions.")

        # Multiplication
        if cols1 == rows2:
            multiplication_result = np.dot(matrix1, matrix2)
            print("\nMultiplication Result:\n", multiplication_result)
        else:
            raise ValueError("Matrix multiplication requires the number of columns in the first matrix to equal the number of rows in the second matrix.")

    except ValueError as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
