import numpy as np

R = int(input("Enter the number of rows:"))
C = int(input("Enter the number of columns:"))

print("Enter the entries in a single line (separated by space): ") # User input of entries in a
entries1 = list(map(int, input().split()))

print("Enter the equation answers in a single line (separated by space): ")
entries2 = list(map(int, input().split()))

matrix = np.array(entries1).reshape(R, C)
ans_matrix = np.array(entries2).reshape(R, 1)

# the calculations
X = np.linalg.inv(matrix).dot(ans_matrix)

print("Your matrix entered was...")
print(matrix)
print()
print(X)

