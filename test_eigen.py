from eigen_module import compute_eigen

# Dummy matrix (you can change this)
A = [
    [1, 2],
    [3, 4]
]

values, vectors = compute_eigen(A)

print("Eigenvalues:")
print(values)

print("\nEigenvectors:")
print(vectors)