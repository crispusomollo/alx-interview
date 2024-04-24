#!/usr/bin/python3


def rotate_2d_matrix(matrix):
    n = len(matrix)
    # Iterate through each layer
    for layer in range(n // 2):
        first = layer
        last = n - 1 - layer
        # Iterate through each element in the layer
        for i in range(first, last):
            # Save top element
            top = matrix[first][i]
            # Move left element to top
            matrix[first][i] = matrix[last - (i - first)][first]
            # Move bottom element to left
            matrix[last - (i - first)][first] = matrix[last][last - (i - first)]
            # Move right element to bottom
            matrix[last][last - (i - first)] = matrix[i][last]
            # Move top element to right
            matrix[i][last] = top

# Example usage
if __name__ == "__main__":
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

rotate_2d_matrix(matrix)

# Output the rotated matrix
for row in matrix:
    print(row)
