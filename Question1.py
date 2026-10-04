

print('\n1a:', end=' ')
print(Applications_of_numerical_computation, '\n')

print('1b: Solving the following system of equations using Substitution method:\n')

print('''
x + y + z = 6      (1)
2x - y + z = 5     (2)
x + 2y - z = 3     (3)

Eliminate z:
(2) - (1):  x - 2y = -1        ...(A)
(1) + (3):  2x + 3y = 9        ...(B)
From (A): x = 2y - 1, substitute into (B):
  2(2y - 1) + 3y = 9  ->  7y = 11  ->  y = 11/7
''')

y = F(11, 7)
x = 2*y - 1
z = 6 - x - y

print(f"x = {x} = {float(x):.4f}")
print(f"y = {y} = {float(y):.4f}")
print(f"z = {z} = {float(z):.4f}")

print("Check eq1 (=6):", x + y + z)
print("Check eq2 (=5):", 2*x - y + z)
print("Check eq3 (=3):", x + 2*y - z)

# Verify against numpy's solver
A = np.array([[1, 1, 1], [2, -1, 1], [1, 2, -1]], dtype=float)
b = np.array([6, 5, 3], dtype=float)
solution = np.linalg.solve(A, b)
rounded = np.round(solution, 2)
print("numpy solution [x,y,z] =", rounded)

print("\n1c: Solving the following system of equations using jacobi iteration method:")

print('''
10x + y  = 11   ->  x = (11 - y)/10
2x + 10y = 12   ->  y = (12 - 2x)/10
''')

print("Starting iteration with initial guess x=0, y=0 and performing 5 iterations:\n")
x, y = 0.0, 0.0
print(f"{'iter':<5}{'x':<12}{'y':<12}")
print(f"{0:<5}{x:<12.3f}{y:<12.3f}")

for i in range(1, 6):
    x_new = (11 - y) / 10
    y_new = (12 - 2*x) / 10
    x, y = x_new, y_new
    print(f"{i:<5}{x:<12.3f}{y:<12.3f}")

A = np.array([[10, 1], [2, 10]], dtype=float)
b = np.array([11, 12], dtype=float)
exact_x, exact_y = np.linalg.solve(A, b)
print(f"exact x = {exact_x:.3f}, y = {exact_y:.3f}")
