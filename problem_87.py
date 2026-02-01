# Problem 87: Generate Pascal's triangle
# Find and fix the error

def pascals_triangle(n):
    triangle = []
    for i in range(n):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i-1][j-1] + triangle[i-1][j]
        triangle.append(row)
    return triangle


print(f"Pascal's triangle (5 rows): {pascals_triangle(5)}")
